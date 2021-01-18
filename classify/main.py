#!/usr/bin/env python3
import csv
import sys
import io

from classify.classification import classify_files, read_rules


def write_classifications_csv(classifications):
    with io.StringIO() as output:
        csv_writer = csv.writer(output)
        for id, (device_id, classification) in enumerate(classifications.items(), 1):
            csv_writer.writerow([id, device_id, classification])

        return output.getvalue()


def get_classification_as_csv(classification_rules_path, communications_path):
    return write_classifications_csv(classify_files(classification_rules_path, communications_path))


def main():
    if len(sys.argv) != 3:
        print(f'Usage: {sys.argv[0]} <CLASSIFICATION_RULES_PATH> <COMMUNICATIONS_PATH>', file=sys.stderr)
        return 1

    classification_rules_path = sys.argv[1]
    communications_path = sys.argv[2]
    print(get_classification_as_csv(classification_rules_path, communications_path))


if __name__ == '__main__':
    exit(main())
