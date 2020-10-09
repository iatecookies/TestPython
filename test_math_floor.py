import unittest
from unittest import mock
from math_floor import math_floor


class TestApplication(unittest.TestCase):
    """
    A mock is a fake, stub or replacement of a class or object. It’s an object that has all properties and methods that you try to call on it, and it will always return a successful response. The trick is that it also keeps track on all methods called on it so that you can later assert the behavior done to your mocked object during your test.
    python3
    import unittest
    help(unittest.TestCase.assertSetEqual)

    mock.patch('package.module.ClassName', return_value='teehee', side_effect=Execption('boom'))
    """

    data = {'username': 'junfei', 'room': 'Kamer1'}
    data2 = {'username': 'junfei', 'room': 'Kamer1'}

    def test_dict(self):
        self.assertDictEqual(self.data, self.data2)

    #OF DIT?

    def test_dict2(self):
        data = {'username': 'junfei', 'room': 'Kamer1'}
        data2 = {'username': 'junfei', 'room': 'Kamer1'}

        self.assertDictEqual(data, data2)


    def test_rooms(self):
        data = {'username': 'junfei', 'room': 'Kamer1'}
        username = data['username']
        room = data['room']
        self.assertEqual (username, 'junfei')
        self.assertEqual (room, 'Kamer1')

        ROOMS = ["Kamer1", "Kamer2"]
        result = len(ROOMS)
        self.assertEqual(result, 2)


    #method1 Decorator
    @mock.patch('math_floor.floor', return_value=3)
    def test_math_exp(self, mock_math_floor):
        self.assertRaises(TypeError, math_floor, 3)
        result = math_floor(x=3.4)
        self.assertEqual(result, 3)

        #this is same as line 48
        with self.assertRaises(TypeError):
            math_floor(2)

        #using mock
        #math_floor(3.3)
        mock_math_floor.floor(2.3)
        mock_math_floor.floor.assert_called_once()


    #method2 Context manager, no need for extra argument
    def test_math_exp2(self):
        with mock.patch('math_floor.floor', return_value=3) as mocked_math_floor:
            result = math_floor(x=3.4)
            self.assertEqual(result, 3)
            self.assertRaises(TypeError, math_floor, 3)

            #using mock
            mocked_math_floor.floor(2.1)
            mocked_math_floor.floor.assert_called_once()
            isinstance(mocked_math_floor,int)


    #method3 Inline, Cleaner way
    def setUp(self):
        self.patcher = mock.patch('math_floor.floor', return_value=3)
        self.patcher.start()

    def test_math_exp3(self):
        result = math_floor(x=3.4)
        self.assertEqual(result, 3)
        self.assertRaises(TypeError, math_floor, 3)

        #using mock Hoe moet dit?
        #self.patcher.floor(3.1)
        #math_floor.floor.assert_called_once()

    def tearDown(self):
        self.patcher.stop()

if __name__ == '__main__':
    unittest.main()
