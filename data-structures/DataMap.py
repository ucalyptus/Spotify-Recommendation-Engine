class DataMap:
    _serialVersionUID = 8001

    def __init__(self, capacity=None):
        self.map = {}
        if capacity is not None:
            self.map = dict.fromkeys(range(capacity), [])

    def get(self, key):
        return self.map[key]

    def put(self, key, value):
        if value is None:
            del self.map[key]
        else:
            self.map[key] = value

    def remove(self, key):
        return self.map.pop(key)

    def contains(self, key):
        if key in self.map:
            return True
        return False

    def itemCount(self):
        return len(self.map)

    def iterator(self):
        return iter(self.map)
