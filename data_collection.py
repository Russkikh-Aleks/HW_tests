
def min_max_courses(courses, durations):
    ''' Задание:
    Напишите код, вернет названия самых коротких и самых длинных курсов.
'''
    courses_dict = dict(zip(courses, durations))
    min_length_courses = f"Самый короткий курс(ы): {', '.join(list(filter(lambda x: courses_dict[x] == min(durations), courses_dict.keys())))} - {min(durations)} месяца(ев)"
    max_length_courses = f"Самый длинный курс(ы): {', '.join(list(filter(lambda x: courses_dict[x] == max(durations), courses_dict.keys())))} - {max(durations)} месяца(ев)"

    return min_length_courses, max_length_courses


def sort_courses_by_duration(courses, durations):
    '''Задание:
       Отсортируйте список курсов courses_list по длительности: от самого короткого к самому длинному.
    '''
    m_list = []
    for i in range(len(durations)):
        m_list.append((courses[i], durations[i]))
    m_list.sort(key=lambda x: x[1])
    result = [f'{i[0]} - {i[1]} месяцев' for i in m_list]
    return result


def check_link(courses, mentors, durations):
    '''Задание:
       Вам нужно проверить, зависят ли друг от друга продолжительность курса и количество преподавателей на этом курсе.
       Если отсортировать курсы по продолжительности и по количеству преподавателей и окажется,
       что курсы идут в одном и том же порядке, значит связь есть. Если порядок будет разный – значит связи нет
    '''

    courses_list = []
    for course, mentor, duration in zip(courses, mentors, durations):
        course_dict = {"title": course,
                       "mentors": mentor, "duration": duration}
        courses_list.append(course_dict)

    for i in range(len(courses_list)):
        courses_list[i]['order'] = i
    x1 = sorted(courses_list, key=lambda x: x['duration'])
    x2 = sorted(courses_list, key=lambda x: len(x['mentors']))

    string = "Связь есть" if x1 == x2 else "Связи нет"
    list_1 = [x['order'] for x in x1]
    list_2 = [x['order'] for x in x2]

    return string, list_1, list_2
