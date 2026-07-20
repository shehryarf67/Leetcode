class Solution(object):
    def carFleet(self, target, position, speed):
        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int
        """
        stack = []
        cars = sorted(zip(position, speed), reverse=True)

        for i, (pos, spd) in enumerate(cars):
            time = float(target - pos) / spd

            if not stack:
                stack.append(time)
            elif time > stack[-1]:
                stack.append(time)
            
        return len(stack)