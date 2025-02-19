user_type = input("Enter the user type, Admin, manager, guest\n")
user_type = user_type.lower()
match user_type:
    case "Manger" | "Admin":
        print(" Hello sir ")
    case " guest ":
        print(" Hello guest")
    case _:
        print(" Hello there ")