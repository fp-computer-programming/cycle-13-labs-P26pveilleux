def facorial(n):
    result = 1
    while n > 1:
        result *= n 
        n -= 1
    return result 

def fibonacci(n):
    fibs_sequence = [0,1]
    while len(fibs_sequence) < n:
        next_num = fibs_sequence [-1]+ fibs_sequence[-2]
        fibs_sequence.append(next_num)
    return fibs_sequence

def add_foods(foods):
    sixth_letter = []
    not_foods = []

    for food in foods:

        if food == str:
            if len(food) >= 6:
                sixth_letter.append(food[5])
        
        else:
            not_foods.append(foods)


print("sixth_letter")
print("not_food")

test_inputs = ["apple","peach" ,"fish","cow","chiken","12345",45]
add_foods(test_inputs)

def add_nums(nums):
    try:
        user_input =input("put in number")
        user_input_int = int(user_input)
        print("passed list:",nums)
        print("user input:",(User_input) )
    except: 
        print("Error: Add correct number")

#testing to see if worked
test_case_1 =[1,2,3,4]
add_nums(test_case_1)

test_case_2=[5,10,15,20]
add_nums(test_case_2)