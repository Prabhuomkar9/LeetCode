class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        seen = set()
        stack = [0]

        while stack:
            roomNumber = stack.pop()

            if roomNumber not in seen:
                for key in rooms[roomNumber]:
                    stack.append(key)

            seen.add(roomNumber)

        return len(seen) == len(rooms)
