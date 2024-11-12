import unittest
from tests_12_3 import RunnerTest, TournamentTest


suite = unittest.TestSuite()
loader = unittest.TestLoader()
suite.addTest(loader.loadTestsFromTestCase(RunnerTest))
suite.addTest(loader.loadTestsFromTestCase(TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(suite)
