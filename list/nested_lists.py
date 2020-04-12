if __name__ == '__main__':

    students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]
    
    #for _ in range(int(input())):
        #name = input()
        #score = float(input())
        #students.append([name, score])


    min_score = min(list(map(lambda x: x[1], students)))
    new_list_students = [students[i] for i in range(len(students)) if min_score != students[i][1]]

    min_score = min(list(map(lambda x: x[1], new_list_students)))

    second_students = [student[0] for student in new_list_students if student[1] == min_score]

    for student in sorted(second_students):
        print(student)