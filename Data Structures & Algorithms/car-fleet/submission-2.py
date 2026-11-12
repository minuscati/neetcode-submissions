class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
# 追的定义：speed大而position小
        # Answer = k = len(position)
        # Time = []
        # for i in range(k):
        #     t = (target - position[i])/speed[i]
        #     Time.append(t)
        # Time = set(Time)
        # return len(Time)

        k = len(position)
        Time_stack = []
        mapping = {}
        for i in range(k):
            mapping[position[i]]=speed[i]
        position.sort(reverse = True)
        
        for i in range(k):
            t = (target-position[i])/mapping[position[i]]
            # while t > Time_stack[-1]:
            #     Time_stack.append(t)
            if not Time_stack or t>Time_stack[-1]:
                Time_stack.append(t)

        return len(Time_stack) 