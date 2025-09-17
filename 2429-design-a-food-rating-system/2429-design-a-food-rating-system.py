import heapq
from typing import List

class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        # food -> cuisine
        self.foodToCuisine = {}
        # food -> rating
        self.foodToRating = {}
        # cuisine -> heap of (-rating, name)
        self.cuisineToHeap = {}

        for f, c, r in zip(foods, cuisines, ratings):
            self.foodToCuisine[f] = c
            self.foodToRating[f] = r
            if c not in self.cuisineToHeap:
                self.cuisineToHeap[c] = []
            heapq.heappush(self.cuisineToHeap[c], (-r, f))

    def changeRating(self, food: str, newRating: int) -> None:
        # update rating dictionary
        self.foodToRating[food] = newRating
        cuisine = self.foodToCuisine[food]
        # নতুন rating heap-এ push করা
        heapq.heappush(self.cuisineToHeap[cuisine], (-newRating, food))

    def highestRated(self, cuisine: str) -> str:
        heap = self.cuisineToHeap[cuisine]
        # Lazy deletion: invalid top pop করতে হবে
        while heap:
            rating, food = heap[0]   # top element দেখব
            rating = -rating
            if self.foodToRating[food] == rating:
                return food
            else:
                heapq.heappop(heap)  # পুরোনো invalid entry ফেলে দিচ্ছি
