# Question 1.

def print_username(username):
    print(f"hello_{username.upper()}")


# Question 2. 

start = 0

for num in range(200):
    if num % 2 != 0:
        start += 1
        print(f"{start}) {num}")

# Question 3.

def bubble_sort(u_list):
    a_list = u_list.copy()
    for i in range(len(a_list) - 1):
        for j in range(len(a_list) - i - 1):
            if a_list[j] > a_list[j+1]:
                a_list[j], a_list[j+1] = a_list[j+1], a_list[j]
    return a_list[-1]

# Question 4. 
def get_leap_years():
    current_iteration = 1
    year = 2000
    
    while year < 3001:
        if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
            print(f"{current_iteration}) {year}")
            current_iteration += 1
        year += 1
        
get_leap_years()

# Question 5. 


def is_consecutive(a_list):
    for i in range(len(a_list) - 1):
        if a_list[i] + 1 != a_list[i+1]:
            return False
    return True




