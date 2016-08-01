
class Set(object):

    def __init__(self, value):
        self.value = value
        self.parent = self
        self.rank = 0

index = {}

def make_set(x):
    index[x] = Set(x)
    return index[x]

def find(x):
    return _find(index[x]).value

def union(x, y):
    _find(index[x]).parent = _find(index[y])

def _find(s):
    if s.parent == s:
        return s
    else:
        return _find(s.parent)


if __name__ == "__main__":
    make_set(1), make_set(2), make_set(3)
    print(find(1), find(2), find(3))
    print(find(1) == find(2), find(1) == find(3), find(2) == find(3))
    union(1, 2)
    print(find(1) == find(2), find(1) == find(3), find(2) == find(3))

    make_set("foo"), make_set("bar")
    print(find("foo"), find("bar"))
    print(find("foo") == find("bar"))
    union("foo", "bar")
    print(find("foo") == find("bar"))

