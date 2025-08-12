# Problem Statement:
#     Lets assume there are 3 assignments and 2 exams, each with max score of 100. 
#     Respective weights are 10%, 10%, 10%, 35%, 35% . 
#     Compute the weighted score based on individual assignment scores. 

a1 = int(input("Enter marks in assignment 1(out of 10): "))
a2 = int(input("Enter marks in assignment 2(out of 10): "))
a3 = int(input("Enter marks in assignment 3(out of 10): "))
mid_exam = int(input("Enter marks in mid exam(out of 35): "))
end_exam = int(input("Enter marks in end exam(out of 35): "))
total = a1+a2+a3+mid_exam+end_exam
print("Total marks scored by the candidate(out of 100) is = ", total)