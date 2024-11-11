import unittest


class Runner:
    def __init__(self, name):
        self.name = name
        self.distance = 0

    def run(self):
        self.distance += 10

    def walk(self):
        self.distance += 5

    def __str__(self):
        return self.name


class RunnerTest(unittest.TestCase):

    def test_walk(self):
        runner = Runner('Adel')
        for i in range(10):
            runner.walk()
        self.assertEqual(runner.distance, 50)

    def test_run(self):
        runner = Runner('Adel')
        for i in range(10):
            runner.run()
        self.assertEqual(runner.distance, 100)

    def test_challenge(self):
        runner = Runner('Adel')
        runner1 = Runner('Adel1')
        for i in range(10):
            runner.run()
            runner.walk()
            runner1.run()
            runner1.walk()
        self.assertEqual(runner.distance, runner1.distance)


if __name__ == '__main__':
    unittest.main()
