#!/usr/bin/env python3
import sys


def classify_files(classification_rules_path, communications_path):
    pass


def main():
    if len(sys.argv) != 3:
        print(f'Usage: {sys.argv[0]} <CLASSIFICATION_RULES_PATH> <COMMUNICATIONS_PATH>', file=sys.stderr)
        return 1

    classification_rules_path = sys.argv[1]
    communications_path = sys.argv[2]
    classifications = classify_files(classification_rules_path, communications_path)

    print(classifications)


if __name__ == '__main__':
    exit(main())
