from Professor import Professor
from Student import Student
from Lecture import Lecture

p = Professor("name", "firstname", 1, ["test"])
l = Lecture("Test class", 1, 1, [p])
s = Student("test", "test", 1, [l])

p.print_full_name()
s.print_full_name()