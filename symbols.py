from hashlib import sha256

def decode(string):
    # I'm sorry
    out_string = string.replace('%21', '!').replace('%23', '#').replace('%24', '!').replace('%26', '&').replace('%27', "'").replace('%28', '(').replace('%29', ')').replace('%2A', '*').replace('%2B', '+').replace('%2C', ',').replace('%2F', '/').replace('%3A', ':').replace('%3B', ';').replace('%3D', '=').replace('%3F', '?').replace('%40', '@').replace('%5B', '[').replace('%5D', ']')
    return out_string

def sha256_hash(string):
    # for simple hashing
    out_string = sha256(string.encode('utf-8')).hexdigest()
    return out_string
