import random

class RandomizedSet:
    def __init__(self):
        self.values = []       # Stores inserted values
        self.indices = {}      # Maps each value to its index in self.values

    def insert(self, val):
        """Insert value if not present. Returns True if inserted."""
        if val in self.indices:
            return False
        self.indices[val] = len(self.values)
        self.values.append(val)
        return True

    def remove(self, val):
        """Remove value if present. Returns True if removed."""
        if val not in self.indices:
            return False
        idx = self.indices[val]
        last_val = self.values[-1]
        self.values[idx] = last_val
        self.indices[last_val] = idx
        self.values.pop()
        del self.indices[val]
        return True

    def getRandom(self):
        """Return a random element with equal probability."""
        return random.choice(self.values) if self.values else None


if __name__ == "__main__":
    a = RandomizedSet()
    a.insert(10)
    a.insert(20)
    a.insert(30)
    a.remove(20)
    print(a.getRandom())  # Randomly prints either 10 or 30
