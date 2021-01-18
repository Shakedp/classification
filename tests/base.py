import csv
import os

from classify.classification import classify_files
from classify.main import get_classification_as_csv

CLASSIFICATION_RULES_NAME = 'classification_rules.csv'
COMMUNICATIONS_NAME = 'communications.csv'
CLASSIFICATIONS_NAME = 'classifications.csv'


def base(test_data_path, test_name):
    specific_test_data_path = os.path.join(test_data_path, test_name)
    classification_rules_path = os.path.join(specific_test_data_path, CLASSIFICATION_RULES_NAME)
    communications_path = os.path.join(specific_test_data_path, COMMUNICATIONS_NAME)
    classifications_path = os.path.join(specific_test_data_path, CLASSIFICATIONS_NAME)

    calculated_classifications = classify_files(classification_rules_path, communications_path)
    expected_classifications = {}
    with open(classifications_path, 'r') as classifications_file:
        csv_reader = csv.reader(classifications_file)
        for row in csv_reader:
            expected_classifications[row[1]] = row[2]

    assert calculated_classifications == expected_classifications, f'Failed!\nExpected :{expected_classifications}\nActual   :{calculated_classifications}'
