#!/usr/bin/env python3
import sys

try:
    print("Hello, World!")
except OSError as e:
    print(f"Error: failed to write output: {e}", file=sys.stderr)
    sys.exit(1)
