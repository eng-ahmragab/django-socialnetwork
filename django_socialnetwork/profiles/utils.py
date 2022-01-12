import uuid


def get_random_code():
    code_length = 8
    uuid_code = str(uuid.uuid4())[:code_length]
    code = uuid_code.replace('-', '').lower()
    return code
