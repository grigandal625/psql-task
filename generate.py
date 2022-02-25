import os
import random

def generate_file(name="tmp", size=None):
    size = size if size else random.randint(1024*1024*500, 1024*1024*1024)
    with open(name, 'wb') as fout:
        fout.write(os.urandom(size))


if __name__ == '__main__':
    generate_file()