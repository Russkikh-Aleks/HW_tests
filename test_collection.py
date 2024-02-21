from unittest import TestCase, expectedFailure
from data_collection import min_max_courses, sort_courses_by_duration, check_link

courses = ["Java-разработчик с нуля", "Fullstack-разработчик на Python",
           "Python-разработчик с нуля", "Frontend-разработчик с нуля"]
mentors = [
    ["Филипп Воронов", "Анна Юшина", "Иван Бочаров", "Анатолий Корсаков", "Юрий Пеньков", "Илья Сухачев", "Иван Маркитан", "Ринат Бибиков", "Вадим Ерошевичев", "Тимур Сейсембаев", "Максим Батырев",
        "Никита Шумский", "Алексей Степанов", "Денис Коротков", "Антон Глушков", "Сергей Индюков", "Максим Воронцов", "Евгений Грязнов", "Константин Виролайнен", "Сергей Сердюк", "Павел Дерендяев"],
    ["Евгений Шмаргунов", "Олег Булыгин", "Александр Бардин", "Александр Иванов", "Кирилл Табельский", "Александр Ульянцев", "Роман Гордиенко", "Адилет Асканжоев",
        "Александр Шлейко", "Алена Батицкая", "Денис Ежков", "Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Максим Филипенко", "Елена Никитина"],
    ["Евгений Шмаргунов", "Олег Булыгин", "Дмитрий Демидов", "Кирилл Табельский", "Александр Ульянцев", "Александр Бардин",
        "Александр Иванов", "Антон Солонилин", "Максим Филипенко", "Елена Никитина", "Азамат Искаков", "Роман Гордиенко"],
    ["Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Валерий Хаслер", "Татьяна Тен", "Александр Фитискин",
        "Александр Шлейко", "Алена Батицкая", "Александр Беспоясов", "Денис Ежков", "Николай Лопин", "Михаил Ларченко"]
]
durations = [14, 20, 12, 20]


class Test_min_max_courses(TestCase):

    def test_1_equal(self):
        result = "Самый короткий курс(ы): Python-разработчик с нуля - 12 месяца(ев)", "Самый длинный курс(ы): Fullstack-разработчик на Python, Frontend-разработчик с нуля - 20 месяца(ев)"
        self.assertEqual(min_max_courses(courses, durations), result)

    def test_2_not_equal(self):
        result = "Самый короткий курс(ы): Python-разработчик с нуля - 12 месяца(ев)", "Самый длинный курс(ы): Fullstack-разработчик на Python, Frontend-разработчик с нуля - 20 месяца(ев)"
        self.assertNotEqual(min_max_courses(
            courses[:3], durations[:3]), result)

    def test_3_isinstanse(self):
        self.assertIsInstance(min_max_courses(courses, durations), tuple)


class Test_sort_courses(TestCase):

    result = ['Python-разработчик с нуля - 12 месяцев',
              'Java-разработчик с нуля - 14 месяцев',
              'Fullstack-разработчик на Python - 20 месяцев',
              'Frontend-разработчик с нуля - 20 месяцев']

    def test_1_equal(self):
        self.assertListEqual(sort_courses_by_duration(
            courses, durations), self.result)

    def test_2_isinstanse(self):
        self.assertIsInstance(
            sort_courses_by_duration(courses, durations), list)

    @expectedFailure
    def test_3_length_not_equal(self):
        self.assertNotEqual(
            len(sort_courses_by_duration(courses, durations)), len(courses))

    def test_4_number_in_str(self):
        for el in sort_courses_by_duration(courses, durations):
            self.assertRegex(el, r'\d\d')


class Test_check_link(TestCase):

    def test_1_check_link(self):
        self.assertEqual(check_link(
            courses, mentors, durations)[0], 'Связи нет')

    @expectedFailure
    def test_2_list_equal(self):
        _, list_1, list_2 = check_link(courses, mentors, durations)
        self.assertListEqual(list_1, list_2)
