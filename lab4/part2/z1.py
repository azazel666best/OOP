import sqlite3

from lab4.part2.Factories import ICourseFactory

if __name__ == '__main__':
    try:
        conn = sqlite3.connect('courses.db')
        cur = conn.cursor()
        teachers = cur.execute("""Select * from teachers""").fetchall()
        courses = cur.execute("""Select * from courses""").fetchall()

        cf = ICourseFactory()

        teacher1 = cf.creator('teacher', name=teachers[0][0])
        teacher2 = cf.creator('teacher', name=teachers[1][0])
        teacher3 = cf.creator('teacher', name=teachers[1][0])

        course1 = cf.creator('course', name=courses[0][0], program=courses[0][1], type=courses[0][2], teacher=teacher1)
        course2 = cf.creator('course', name=courses[1][0], program=courses[1][1], type=courses[1][2], teacher=teacher2)
        course3 = cf.creator('course', name=courses[2][0], program=courses[2][1], type=courses[2][2], teacher=teacher2)

        print(teacher1)
        print()
        print(teacher2)
        print()
        print(teacher3)

    except ValueError as e:
        print(f'ValueError\n {e}')
    except TypeError as e:
        print(f'TypeError\n {e}')
