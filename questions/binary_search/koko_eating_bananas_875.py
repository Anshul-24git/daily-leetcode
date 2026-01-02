class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:    
        def canFinishInTime(speed):
            total_hours = 0
            
            # Calculate hours needed for each pile
            for pile in piles:
                # Use ceiling division: (pile + speed - 1) // speed
                total_hours += (pile + speed - 1) // speed
                
                # Early termination if already exceeding time limit
                if total_hours > h:
                    return False
                    
            return total_hours <= h
    
        # Initialize binary search boundaries
        left = 1                    # Minimum possible speed
        right = max(piles)          # Maximum speed needed (eat largest pile in 1 hour)
        
        # Binary search for minimum valid speed
        while left < right:
            mid = left + (right - left) // 2    # Avoid potential overflow
            
            # Check if current speed is sufficient
            if canFinishInTime(mid):
                # Speed is valid, try to find smaller speed
                right = mid
            else:
                # Speed is too slow, need faster speed
                left = mid + 1
        
        # Return the minimum valid speed
        return left
