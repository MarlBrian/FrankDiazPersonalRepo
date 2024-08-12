from typing import List


# TODO: Make it from left to right
class Solution:
    def collision(self, left, right):
        if self.asteroids[left] * self.asteroids[right] > 0:
            self.i -= 1
        else:
            if abs(self.asteroids[left]) == abs(self.asteroids[right]):
                self.asteroids.pop(left)
                self.asteroids.pop(right)
                self.length = len(self.asteroids) * -1 if len(self.asteroids) else 0
            elif abs(self.asteroids[right]) > abs(self.asteroids[left]):
                self.asteroids.pop(left)
                self.length = len(self.asteroids) * -1
            elif abs(self.asteroids[right]) < abs(self.asteroids[left]):
                self.asteroids.pop(right)
                self.length = len(self.asteroids) * -1

    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        self.asteroids = asteroids
        self.length = len(self.asteroids) * -1
        self.i = -1
        while self.i > self.length:
            self.collision(self.i - 1, self.i)
            if self.length == 0:
                break
        return self.asteroids


print(Solution().asteroidCollision([10,2,-5]))
print(Solution().asteroidCollision([8,-8]))
print(Solution().asteroidCollision([5,10,-5]))