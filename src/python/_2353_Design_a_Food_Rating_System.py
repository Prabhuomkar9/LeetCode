from sortedcontainers import SortedSet

class FoodRatings:
    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.cuisine = {}
        self.rating = {}
        self.famous = defaultdict(SortedSet)

        for food, cuisine, rating in zip(foods, cuisines, ratings):
            self.rating[food] = rating
            self.cuisine[food] = cuisine
            self.famous[cuisine].add((-rating, food))

    def changeRating(self, food: str, newRating: int) -> None:
        self.famous[self.cuisine[food]].remove((-self.rating[food], food))
        self.rating[food] = newRating
        self.famous[self.cuisine[food]].add((-self.rating[food], food))

    def highestRated(self, cuisine: str) -> str:
        return self.famous[cuisine][0][1]

# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)
