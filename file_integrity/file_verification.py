import logging
from file_integrity.hash_utils import generate_hash
file_hashes = {}

def file_verification(filename):
    if filename not in file_hashes:
        logging.warning(f"Verification failed as file {filename} is not present in database.")
        print("File not in database. Add it first and then only verification can be done.")
        return

    h = generate_hash(filename)
    if h == file_hashes[filename]:
        logging.info(f"File verified: {filename} is intact.")
        print("✅ File is intact. Your file is safe, so nothing to worry about!")

    else:
        logging.warning(f"File modified: {filename}")
        print("⚠️ The file that have been added seems to be modified! Was it you or any other? If it was other person, you are definitely in danger. Please review the changes.")
