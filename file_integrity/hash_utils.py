import hashlib
import logging
    
def generate_hash(filename, chunk_size=8192):
    try:
        sha256 = hashlib.sha256()
        with open(filename, "rb") as f:
            while True:
                chunk = f.read(chunk_size)
                if not chunk:
                    break
                sha256.update(chunk)  
        return sha256.hexdigest()
    except FileNotFoundError:
        print("File not found!")
        return None
    except PermissionError:
        print("Permission denied!")
        return None

