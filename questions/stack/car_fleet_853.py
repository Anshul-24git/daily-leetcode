class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse = True)
        stack = []

        for pos, spd in cars:
            time = (target - pos) / spd

            if not stack or time > stack[-1]:
                stack.append(time)

        return len(stack)
        '''
        n cars - starting at different positions
        cars are traveling to mile target
        pos[i] - starting | spd[i] - mph
        no passing but can catchup & form fleet
        speed of car fleet = speed of slowest car
        car that catches up at target is also considered
        
        Input: target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3]
        Output : 3
        '''
        
