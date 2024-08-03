def hello():
    print("Hello, user! :)");

def pack(a,b,c):
    return [a,b,c];


# def eat_lunch(my_food):
#     if len(my_food) == 0:
#         print("My lunchbox is empty! :(")
#     else:
#         for i in range(len(my_food)):
#             if i == 0:
#                 print(f"First I eat {my_food[0]}")
#             else:
#                 print(f"Next I eat my {my_food[i]}");

# this way makes more sense to me, refactored ^
def eat_lunch(my_food):
    if not my_food:
        print("My lunchbox is empty! :(")
    else:
        print(f"First I eat {my_food[0]}")
        for food in my_food[1:]:
            print(f"Next I eat my {food}")


hello();
print(pack("a","b","c"));
print(pack(1,2,3));
eat_lunch(["yogurt", "sandwich", "fruit snacks"]);
eat_lunch([]);