from collections import deque
from typing import List

class Solution:
    def maxCandies(
        self,
        status: List[int],
        candies: List[int],
        keys: List[List[int]],
        containedBoxes: List[List[int]],
        initialBoxes: List[int]
    ) -> int:

        owned_boxes   = set(initialBoxes)                 # boxes we physically hold
        owned_keys    = set()                             # keys collected so far
        processed     = set()                             # boxes already opened
        q = deque(b for b in initialBoxes if status[b])   # start with the open ones

        total = 0

        while q:
            box = q.popleft()
            if box in processed:
                continue
            processed.add(box)

            # collect candies
            total += candies[box]

            # gather keys found inside this box
            for k in keys[box]:
                if k not in owned_keys:
                    owned_keys.add(k)
                    if k in owned_boxes and k not in processed:
                        q.append(k)

            # gather boxes found inside this box
            for inner in containedBoxes[box]:
                if inner not in owned_boxes:
                    owned_boxes.add(inner)
                if (status[inner] == 1 or inner in owned_keys) and inner not in processed:
                    q.append(inner)

        return total
