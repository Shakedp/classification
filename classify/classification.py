import csv
from collections import namedtuple

from classify.rules import RULES_VALIDATORS

# TODO - organize rule book  based on types for faster access to the relevant rules
#  (e.g. communication_protocol only cares about argument)

Rule = namedtuple('Rule', ['id', 'type', 'argument', 'classification'])
Communication = namedtuple('Communication', ['id', 'timestamp', 'device_id', 'protocol_name', 'host'])
Classification = namedtuple('Classification', ['device_id', 'classification'])

UNKNOWN_CLASSIFICATION = 'unknown'


def _parse_rule(row):
    return Rule(*row)


def _parse_communication(row):
    return Communication(*row)


def read_rules(classification_rules_path):
    rules = []
    with open(classification_rules_path, 'r') as classification_rules_file:
        csv_reader = csv.reader(classification_rules_file)
        for row in csv_reader:
            rules.append(_parse_rule(row))

    return rules


def classify(rules, communication, applying_rules):
    classification = Classification(communication.device_id, UNKNOWN_CLASSIFICATION)
    for rule in rules:
        if rule.type in RULES_VALIDATORS and RULES_VALIDATORS[rule.type](rule, communication, applying_rules=applying_rules):
            # We don't break if we find the correct one because we want the last rule that applies
            classification = Classification(communication.device_id, rule.classification)
            applying_rules[rule.id] = applying_rules.get(rule.id, set())
            applying_rules[rule.id].add(communication.device_id)

    return classification


def classify_files(classification_rules_path, communications_path):
    classifications = {}
    applying_rules = {}
    rules = read_rules(classification_rules_path)
    with open(communications_path, 'r') as communications_file:
        csv_reader = csv.reader(communications_file)
        for row in csv_reader:
            classification = classify(rules, _parse_communication(row), applying_rules)
            classifications[classification.device_id] = classification.classification
            # We want to update according to the latest device_id we classified

    return classifications
