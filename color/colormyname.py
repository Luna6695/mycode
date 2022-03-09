#!/usr/bin/env python3
"""Lucy | lchen6695@gmail.com
Learning how to use functions"""

## Installs the crayons package.
import crayons


def main():
    """run time code. Always indent under function"""

    # print name in two colors
    print(f"{crayons.cyan('Lucy')} {crayons.green('Chen')}")  


# this condition is only true if our script is run directly
# it is NOT true if our code is imported into another script
if __name__ == "__main__":
    main()

