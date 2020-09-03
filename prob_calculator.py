# https://repl.it/repls/DiligentLameBinarysearchtree#main.py
import copy
import random


class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        for (k, v) in kwargs.items():
            for i in range(v):
                self.contents.append(k)

    def draw(self, numberOfBalls: int):
        ballsToReturn = []
        if numberOfBalls > (len(self.contents)):
            ballsToReturn = copy.deepcopy(self.contents)
            self.contents = []
            return ballsToReturn

        while(numberOfBalls > 0 and len(self.contents) > 0):
            randomIndex = random.randint(0, len(self.contents) - 1)
            value = self.contents.pop(randomIndex)
            ballsToReturn.append(value)
            numberOfBalls = numberOfBalls - 1
        return ballsToReturn


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):

    num_desired_results = 0

    for i in range(num_experiments):
        hat_copy = copy.deepcopy(hat)

        actual = hat_copy.draw(num_balls_drawn)

        actual_dict = {ball: actual.count(ball) for ball in set(actual)}

        # Compare drawn balls to desired result:
        result = True
        for key, value in expected_balls.items():
            if key not in actual_dict or actual_dict[key] < expected_balls[key]:
                result = False
                break

        if result:
            num_desired_results += 1

    return num_desired_results/num_experiments
