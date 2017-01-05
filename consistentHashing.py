import bisect
import hashlib

class ConsistentHashRing(object):
    """Consistent hashing ring class"""
    def __init__(self):
        self.hashedKeys = []
        self.nodes = {}

    def hashObject(self, key):
        """converting key to hash value using md5"""

        return long(hashlib.md5(key).hexdigest(), 16)

    def __setitem__(self, nodename, node):
        print nodename
        print node
        if nodename in self.nodes:
            raise ValueError("Node name %r is already present " % nodename)
        self.nodes[nodename] = node
        bisect.insort(self.hashedKeys, nodename)

    def __getitem__(self, key):
        """Return a node with the next highest hash value of the object."""
        hash_ = self.hashObject(key)
        nodePosition = bisect.bisect(self.hashedKeys, hash_)
        if nodePosition == len(self.hashedKeys):
            nodePosition = 0
        return self.nodes[self.hashedKeys[nodePosition]]