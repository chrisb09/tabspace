#!/bin/python3

import argparse, os

ENCODING = "utf-8"  
ZERO = (9).to_bytes(1, "big").decode(ENCODING)         #TAB
ONE = (32).to_bytes(1, "big").decode(ENCODING)         #SPACE

parser = argparse.ArgumentParser(description='Encode files into {tab,space} binary.')

parser.add_argument('source',
                    help='Path of file or folder that serves as source for conversion.')

parser.add_argument('destination',
                    help='Path of folder that serves as target for conversion.')


parser.add_argument('--encode', action='store_true', help="Encode source to destination.")

parser.add_argument('--decode', action='store_true', help="Encode source to destination.")

args = parser.parse_args()

if args.encode == args.decode:
    if args.encode:
        print("Only set --encode OR --decode flag, not both.")
    else:
        print("Please set --encode or --decode flag.")
    exit()

def convert(data):
    if type(data) == str:
        data = data.encode(ENCODING)
    result = ""
    for i in range(len(data)):
        for j in range(7, -1, -1):
            result += ONE if data[i] >> j & 1 else ZERO
    return result

def revert(data):
    result = ""
    b = 0
    for i in range(len(data)):
        b |= (data[i] == ONE) << 7-(i%8)
        if i%8 == 7:
            result += b.to_bytes(1, "big").decode(ENCODING)
            b = 0
    return result

def read_in_chunks(file_object, chunk_size=1024):
    """Lazy function (generator) to read a file piece by piece.
    Default chunk size: 1k."""
    while True:
        data = file_object.read(chunk_size)
        if not data:
            break
        yield data

def write_to_file(file, text):
    with open(file, "a" if os.path.exists(file) else "w") as file2:
        file2.write(text)

def vert_file(source, target, func):
    if os.path.exists(target):
        os.remove(target)
    with open(source) as f:
        for piece in read_in_chunks(f):
            write_to_file(target, func(piece))

def convert_file(source, target):
    vert_file(source, target, convert)

def revert_file(source, target):
    vert_file(source, target, revert)

def vert_files(directory, target_dir, func):
    if not os.path.exists(directory):
        return
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)
    if os.path.isfile(directory):
        func(directory, os.path.join(target_dir, os.path.basename(directory)))
        return
    for root, dirs, files in os.walk(directory):
        for file in files:
            tf = os.path.join(target_dir, file)
            td = os.path.dirname(tf)
            if not os.path.exists(td):
                os.makedirs(td)
            func(os.path.join(root,file), tf)

def convert_files(directory, target_dir):
    vert_files(directory, target_dir, convert_file)


def revert_files(directory, target_dir):
    vert_files(directory, target_dir, revert_file)

if args.encode:
    convert_files(args.source, args.destination)
else:
    revert_files(args.source, args.destination)
