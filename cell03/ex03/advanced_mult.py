#!/usr/bin/env python3

import sys

if len(sys.argv) > 1:
    print("none")
else:
    i = 0
    while i <= 10:
        j = 0
        print(f"Table de {i}:", end="")
        while j <= 10:
            print(f" {i * j}", end="")
            j += 1
        print()
        i += 1