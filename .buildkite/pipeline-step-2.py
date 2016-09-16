#!/usr/bin/env python
import yaml
import random

OPTION_ONE = """
steps:
  - command: "echo FAILED"
    label: "Loop again :thumbsdown:"
  - command: ".buildkite/pipeline-step-2.py | buildkite-agent pipeline upload"
    label: "Looping again"
"""

OPTION_TWO = """
steps:
  - command: "echo 'GOOD TO GO'"
    label: "Succeeded! :thumbsup:"
"""


def main():
    print random.choice([OPTION_ONE, OPTION_ONE, OPTION_ONE, OPTION_TWO])


if __name__ == "__main__":
    main()
