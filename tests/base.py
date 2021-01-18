import os

from classify.main import classify_files

CLASSIFICATION_RULES_NAME = 'classification_rules.csv'
COMMUNICATIONS_NAME = 'communications.csv'
CLASSIFICATIONS_NAME = 'classifications.csv'


def base(test_data_path, test_name):
    specific_test_data_path = os.path.join(test_data_path, test_name)
    classification_rules_path = os.path.join(specific_test_data_path, CLASSIFICATION_RULES_NAME)
    communications_path = os.path.join(specific_test_data_path, COMMUNICATIONS_NAME)
    classifications_path = os.path.join(specific_test_data_path, CLASSIFICATIONS_NAME)

    calculated_classifications = classify_files(classification_rules_path, communications_path)
    with open(classifications_path, 'r') as classifications_file:
        expected_classifications = classifications_file.read()

    assert calculated_classifications == expected_classifications, 'Calculated classifications don\'t match expected classifications'
