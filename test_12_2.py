from module_12_2 import Runner, Tournament
import unittest


class TournamentTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runner1 = Runner('Усэйн', 10)
        self.runner2 = Runner('Андрей', 9)
        self.runner3 = Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        for key, value in cls.all_results.items():
            print(f"{value}")

    def test_r1_r3(self):
        tournament = Tournament(90, self.runner1, self.runner3)
        results = tournament.start()

        self.all_results[1] = {place: runner.name for place, runner in results.items()}

        last_runner = results[min(results.keys())]  # Получаем объект последнего бегуна
        self.assertNotEqual(last_runner.name, 'Ник')  # Проверяем имя

    def test_r2_r3(self):
        tournament = Tournament(90, self.runner2, self.runner3)
        results = tournament.start()

        self.all_results[2] = {place: runner.name for place, runner in results.items()}

        last_runner = results[min(results.keys())]
        self.assertNotEqual(last_runner.name, "Ник")

    def test_r1_r2_r3(self):
        tournament = Tournament(90, self.runner1, self.runner2, self.runner3)
        results = tournament.start()

        self.all_results[3] = {place: runner.name for place, runner in results.items()}

        last_runner = results[min(results.keys())]
        self.assertNotEqual(last_runner.name, "Ник")



if __name__ == '__main__':
    unittest.main()

