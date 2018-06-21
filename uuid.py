import uuid

def uuid_generator():
    n = uuid.uuid4()
    m = uuid.uuid4().hex
    print(n)
    print(m)

uuid_generator()