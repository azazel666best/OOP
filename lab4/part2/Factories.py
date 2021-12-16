from lab4.part2.classes import Teacher, LocalCourse, OffsiteCourse


class ICourseFactory:
    def creator(self, course_or_teacher, **kwargs):
        if course_or_teacher == 'course':
            return self.add_course(**kwargs)
        if course_or_teacher == 'teacher':
            return self.add_teacher(**kwargs)
        else:
            raise ValueError

    @staticmethod
    def add_teacher(**kwargs):
        creator = ITeacher()
        return creator.create(**kwargs)

    @staticmethod
    def add_course(**kwargs):
        creator = ICourse()
        return creator.create(**kwargs)


class ITeacher:
    @staticmethod
    def create(**kwargs):
        if 'courses' in kwargs.keys():
            return Teacher(kwargs['name'], kwargs['courses'])
        else:
            return Teacher(kwargs['name'])


class ICourse:
    def create(self, **kwargs):
        if kwargs['type'] == 'Local':
            return self.create_local(**kwargs)
        elif kwargs['type'] == 'Offsite':
            return self.create_offsite(**kwargs)
        else:
            raise ValueError

    @staticmethod
    def create_local(**kwargs):
        course = LocalCourse(kwargs['name'], kwargs['program'], kwargs['teacher'])
        kwargs['teacher'].add_course(course)
        return course

    @staticmethod
    def create_offsite(**kwargs):
        course = OffsiteCourse(kwargs['name'], kwargs['program'], kwargs['teacher'])
        kwargs['teacher'].add_course(course)
        return course
