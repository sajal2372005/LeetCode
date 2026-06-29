class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        while len(students)>0 or len(sandwiches)>0:
            if students[0] == sandwiches[0]:
                students.pop(0)
                sandwiches.pop(0)
            else:
                if sandwiches[0] not in students:
                    break
                stu = students.pop(0)
                students.append(stu)
        return len(students)