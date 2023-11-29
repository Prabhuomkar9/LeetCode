class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        flightStates = [0] * (n + 1)

        for start, last, seats in bookings:
            flightStates[start - 1] += seats
            flightStates[last] -= seats

        flightStates = list(accumulate(flightStates))

        return flightStates[:-1]
