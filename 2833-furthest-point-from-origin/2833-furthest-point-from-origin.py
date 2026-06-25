class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        data = abs(moves.count("L")-moves.count("R"))
        wildcard = moves.count("_")
        return data+wildcard