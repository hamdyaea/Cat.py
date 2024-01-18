# Developer : Hamdy Abou El Anein
# hamdy.aea@protonmail.com

# This software is a copy of the famous cat linux software from coreutils.


import sys

def cat(files):
    for file in files:
        try:
            with open(file, 'r') as f:
                print(f.read())
        except FileNotFoundError:
            print(f"The {file} is not found.")
        except IOError as e:
            print(f"Error while openning {file}: {e}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        cat(sys.argv[1:])
    else:
        print("Usage: python3 Cat.py [file ...]")

