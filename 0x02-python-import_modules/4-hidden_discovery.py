#!/usr/bin/python3
# 4-hidden_discovery.py
# Brennan D Baraban <375@holbertonschool.com>

if __name__ == "__main__":
    import hidden_4

    names = dir(hidden_4)
    for name in names:
        if not name.startswith("__"):
            print(name)
