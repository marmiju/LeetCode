class Solution:
    def defangIPaddr(self, address: str) -> str:
        st = address.split(".")
        return "[.]".join(st)
        