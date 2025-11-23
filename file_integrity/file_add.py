import logging
from file_integrity.hash_utils import generate_hash
from file_integrity.file_verification import file_hashes

def file_add(filename):
    h = generate_hash(filename)
    if h:
        file_hashes[filename] = h
        logging.info(f"Hash stored for file: {filename}")
        print(f"Stored hash for {filename}")

