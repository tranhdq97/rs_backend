import hashlib
import os.path
import re
from functools import partial


def check_regex(pattern, input_string):
    return re.match(pattern, input_string)


def str2bool(input_string):
    return str(input_string).lower() in ("yes", "true", "t", "1")


def hash_file(file, block_size=65536):
    hash_handler = hashlib.md5()
    for buf in iter(partial(file.read, block_size), b""):
        hash_handler.update(buf)

    return hash_handler.hexdigest()


def get_file_field_directory(instance, filename):
    _, filename_ext = os.path.splitext(filename)
    return f"{hash_file(instance.file)}{filename_ext}"


def get_thumbnail_directory(instance, filename):
    _, filename_ext = os.path.splitext(filename)
    return f"thumbnail/{hash_file(instance.file)}{filename_ext}"
