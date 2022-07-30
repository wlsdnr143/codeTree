number_restaurant = int(input())
number_customer_List = input().split()
number_customer_List = list(map(int, number_customer_List))

leader_max, member_max  = map(int,input().split())
number_of_Inspector = 0

for i in range(number_restaurant):
    number_of_Inspector+=1
    if (number_customer_List[i] - leader_max) <= 0 :
        continue
    else:
        number_customer_List[i] -= leader_max
        if number_customer_List[i] % member_max == 0:
            number_member = number_customer_List[i] // member_max
            number_of_Inspector+=number_member
        else:
            number_of_member = number_customer_List[i] // member_max + 1
            number_of_Inspector += number_of_member

print(number_of_Inspector)