class apartmentHunting:
    def __init__(self, blocks, reqs):
        self.blocks = blocks
        self.reqs = reqs

    def solution(self):
        req_distances = []
        for req in reqs:
            distances = {}
            for i in range(len(self.blocks)):
                #distances[i] = 0
                left_distance = 0
                found = False
                leftIdx = i
                rightIdx = i + 1
                left = False
                while leftIdx >= 0 and not found:
                    if req in self.blocks[leftIdx]:
                        if self.blocks[leftIdx][req]:
                            #distances[i] = distances[i] + abs((i - leftIdx))
                            left_distance = left_distance + abs((i - leftIdx))
                            found = True
                            left = True
                    leftIdx -= 1
                found = False
                right_distance = 0
                right = False
                while rightIdx < len(self.blocks) and not found:
                    if req in self.blocks[rightIdx]:
                        if self.blocks[rightIdx][req]:
                            #distances[i] = distances[i] + abs((i - rightIdx))
                            right_distance = right_distance + abs((i - rightIdx))
                            found = True
                            right = True
                    rightIdx += 1
                
                if left and right:
                    distances[i] = min(left_distance, right_distance)
                elif not left:
                    distances[i] = right_distance
                elif not right:
                    distances[i] = left_distance

            req_distances.append(distances)

        all_blocks = {}
        for req_distance in req_distances:
            for k, v in req_distance.items():
                if k not in all_blocks:
                    all_blocks[k] = v
                else:
                    all_blocks[k] = max(all_blocks[k], v)
        
        smallest = float("inf")
        optimal_block = -1
        for block, distance in all_blocks.items():
            if distance < smallest:
                optimal_block = block
                smallest = distance
        
        return optimal_block


# --- Testing the solution -
blocks = [
    {
        "gym": False,
        "school": True,
        "store": False,
    },
    {
        "gym": True,
        "school": False,
        "store": False,
    },
    {
        "gym": True,
        "school": True,
        "store": False,
    },
    {
        "gym": False,
        "school": True,
        "store": False,
    },
    {
        "gym": False,
        "school": True,
        "store": True,
    }
]

reqs = ["gym", "school", "store"]

obj = apartmentHunting(blocks, reqs)
print(obj.solution())
