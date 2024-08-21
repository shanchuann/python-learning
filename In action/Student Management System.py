from logging import raiseExceptions


class User(object):
    def __init__(self, name, age,gender,id_number):
        self.name = name
        self.age = age
        self.gender = gender
        self.id_number = id_number

    def show_infos(self):
        print('*' * 40)
        print('        name:       ',self.name)
        print('        age:        ',self.age)
        print('       gender:      ',self.gender)
        print('student/work_number:',self.id_number)

class Student(User):
    def __init__(self, name, age,gender,id_number):
        super(Student,self).__init__(name, age,gender,id_number)
        self.courses = []

    def show_infos(self):
        super().show_infos()
        print('      courses:       ',end='')
        if not self.courses:
            print('None')
        else:
            print(' '.join([i.name for i in self.courses]))
        print('*' * 40)

    def add_course(self,course):
        if course in self.courses:
            raise Exception('already have this course')
        else:
            self.courses.append(course)
            return True

class Teacher(User):
    def __init__(self, name, age,gender,id_number,manager,cla):
        super(Teacher,self).__init__(name, age,gender,id_number)
        self.manager = manager
        self.cla = cla

    def show_infos(self):
        super().show_infos()
        print('       manager:      %s' %['No','Yes'][self.manager])
        print('       class:        ',end='')
        if not self.cla:
            print('None')
        else:
            print(' '.join([str(i) for i in self.cla]))
        print('*' * 40)

class Cla(object):
    def __init__(self, name,id_number,teacher,students):
        self.name = name
        self.id_number = id_number
        self.teacher = teacher
        self.students = students

    def show_infos(self):
        print('*' * 17 + '班级信息' + '*' * 16)
        print('   name:      ',self.name)
        print('class_number  ',self.id_number)
        print('  teacher:    ',self.teacher.name)
        print(' students:     ',end='')
        if not self.students:
            print('None')
        else:
            print(' '.join([i.name for i in self.students]))

        print('*' * 40)

    def add_student(self,student):  # 添加学生
        if student in self.students:
            raise (Exception('already have this student'))
        else:
            self.students.append(student)
            return True

    def sub_student(self,student):  # 删除学生
        if student not in self.students:
            raise Exception('no this student')
        else:
            self.students.remove(student)
            return True

class Course(object):
    courses = []  # 类属性
    def __init__(self, name, id_number, teacher, students, type, number):
        self._name = name
        self.id_number = id_number
        self.teacher = teacher
        self.students = students
        self.type = type
        self.number = number
        self.student_number = len(self.students)
        self.valid_number = self.number - self.student_number
        Course.courses.append(self.name)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self,value):
        if not isinstance(value,str):
            raise Exception('name must be str')
        self._name = value

    def show_infos(self):
        print('*' * 17 + '课程信息' + '*' * 16)
        print('    name:        ',self.name)
        print('course_number    ',self.id_number)
        print('   teacher:      ',self.teacher.name)
        print('    type:        ',self.type)
        print('   number:       ',self.number)
        print('student_number:  ',self.student_number)
        print(' valid_number:   ',self.valid_number)
        print('   students:      ',end='')
        if not self.students:
            print('None')
        else:
            print(' '.join([i.name for i in self.students]))
        print('*' * 40)

    def add_student(self,student):
        if student in self.students:
            raise Exception('already have this student')
        elif self.valid_number == 0:
            raise Exception('no more student can add')
        else:
            self.students.append(student)
            self.student_number += 1
            self.valid_number -= 1
            student.add_course(self)
            return True

    def sub_student(self,student):
        if student not in self.students:
            raise Exception('no this student')
        else:
            self.students.remove(student)
            self.student_number -= 1
            self.valid_number += 1
            return True

    @classmethod
    def show_courses(cls):
        return cls.courses
# 创建学生对象
shanchuan = Student('shanchuan',19,'man',2403789)
Fiary = Student('Fiary', 20,'woman',2403791)
Rose = Student('Rose',18,'woman',2403790)

# 创建教师对象
Jack = Teacher('Jack',50,'man',7789,True,['计科1班','网络2班'])
Tom = Teacher('Tom',26,'woman',7795, False, [])

# 创建班级对象
computer_2 = Cla('计科2班', 201, Jack, [])
webnet_2 = Cla('网络2班', 202, Tom, [shanchuan])

# 创建课程对象
python = Course('python', 101, Jack, [shanchuan], 'COMPULSORY', 2)
Java = Course('Java', 102, Tom, [shanchuan,Rose,Fiary], 'ELECTIVE', 3)
# 操作
computer_2.add_student(Rose)
computer_2.sub_student(Rose)
computer_2.add_student(shanchuan)
# computer_2.add_student(shanchuan)
python.add_student(Rose)
# python.show_infos()
# python.add_student(Rose)
# python.add_student(Fiary)
python.sub_student(Rose)
# Rose.show_infos()
# print(Course.show_courses())
python.name = 'python_plus'
# python.show_infos()