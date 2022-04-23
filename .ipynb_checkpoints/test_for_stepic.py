import unittest
from main import print_hi

class Test_stepic(unittest.TestCase):


    def test_task(self):
        str_list_first = ["Москва", "Уфа", "Караганда", "Тверь", "Минск", "Казань"]
        str_list_seconf = ["Москв", "Уа", "Краганда", "Тврь", "Минк", "Кзань"]
        str_list_third = ["Мосв", "У", "аганда", "рь", "Ми", "ань"]



        self.assertEqual(print_hi(str_list_first),[6, 3, 9, 5, 5, 6])
        self.assertEqual(print_hi(str_list_seconf),[5, 2, 8, 4, 4, 5])
        self.assertEqual(print_hi(str_list_third),[4, 1, 6, 2, 2, 3])