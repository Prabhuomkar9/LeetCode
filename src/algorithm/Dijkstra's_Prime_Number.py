from time import time
from heapq import heappop, heappush


def Dijkstra_Prime_Number(n: int) -> list[int]:
    """
    Dijkstra's Prime Number Algorithm
    //INPUT: Integer n
    //OUTPUT: Prime numbers between [1:n(inclusive)]
    """
    prime_numbers: list[int] = [2] if n >= 2 else []
    pq: list[tuple[int, int]] = [(4, 2)] if n >= 2 else []

    for i in range(3, n + 1):
        limit, prime = heappop(pq)
        if i < limit:
            prime_numbers.append(i)
            heappush(pq, (i * i, i))
        else:
            while pq and i >= limit:
                limit += prime
                heappush(pq, (limit, prime))
                limit, prime = heappop(pq)
        heappush(pq, (limit, prime))

    return prime_numbers


if __name__ == "__main__":
    # Driver Code
    startTime: int = time()
    print("Dijkstra's Prime Number Algorithm")
    print("//INPUT: Integer n")
    print("//OUTPUT: Prime numbers between [1:n(inclusive)]")

    n: int = int(input("Enter the value of n: "))
    prime_numbers: list[int] = Dijkstra_Prime_Number(n)

    print(f"Prime numbers are: {prime_numbers}")

    endTime: int = time()
    print(f"Time taken: {endTime - startTime} s")
