import pickle as pkl

def dump(obj, handle):
        with open(handle, 'wb') as f:
            pkl.dump(obj, f)


def load(handle):
    with open(handle, 'rb') as f:
        return pkl.load(f)