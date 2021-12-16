class Course:
    def __init__(self, name, program, teacher):
        self.name = name
        self.program = program
        self.teacher = teacher

    @property
    def name(self):
        return self.__name

    @property
    def teacher(self):
        return self.__teacher

    @property
    def program(self):
        return self.__program

    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise TypeError('name should be str')
        self.__name = name

    @teacher.setter
    def teacher(self, teacher):
        if not isinstance(teacher, Teacher):
            raise TypeError('course mast be Course')
        self.__teacher = teacher

    @program.setter
    def program(self, program):
        if not isinstance(program, str):
            raise TypeError('program should be str')
        self.__program = program

    def __str__(self):
        return f'Name: {self.name}\nTeacher: {self.teacher.name}\nProgram: {self.program}'


class LocalCourse(Course):
    def __init__(self, name, teacher, program):
        super(LocalCourse, self).__init__(name, teacher, program)


class OffsiteCourse(Course):
    def __init__(self, name, teacher, program):
        super(OffsiteCourse, self).__init__(name, teacher, program)


class Teacher:
    def __init__(self, name, *courses):
        self.name = name
        self.courses = []
        for i in courses:
            self.add_course(i)

    def add_course(self, course):
        if not isinstance(course, Course):
            raise TypeError('course mast be Course')
        self.courses.append(course)

    @property
    def name(self):
        return self.__name

    @property
    def courses(self):
        return self.__courses

    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise TypeError('name should be str')
        self.__name = name

    @courses.setter
    def courses(self, courses):
        if not all(isinstance(course, Course) for course in courses):
            raise TypeError('course mast be Course')
        self.__courses = courses

    def __str__(self):
        return f'Name: {self.name}\nCourses:\n' + (
            '\n\n'.join(list(map(str, self.courses))) if self.courses else 'no curses')
