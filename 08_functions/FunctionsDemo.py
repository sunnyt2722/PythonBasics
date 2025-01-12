friends_list = ["Rambo", "Rocky", "Stallion"]
def hello():
    print("Hello!!")

def user_age_in_seconds():
    user_age = int(input("Enter your age: "))
    age_in_seconds = user_age * 365 * 24 * 60 * 60
    print(f"Your age is seconds is {age_in_seconds}")

def add_friends_in_list():
    friend_name = input("Enter friend's name to append : ")
    friends_list.append(friend_name)
    print(friends_list)
hello()
user_age_in_seconds()
add_friends_in_list()