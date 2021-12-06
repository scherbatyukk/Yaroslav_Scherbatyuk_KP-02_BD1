def find_Parameters(door):
    reply = ""
    if door == 1:
        while True:
            print()
            print("users - 1\n questions - 2\n answers - 3\n tags - 4\n quit - 0")
            request1 = input("Enter your value: ")
            if request1 == "0":
                print("Quiting..")
                return "0"
            if request1 != "1" and request1 != "2" and request1 != "3" and request1 != "4":
                print("///////////////////////////////////////////////")
                print("Please, follow the rules >Enter the valid input")
                print("///////////////////////////////////////////////")
            else:
                while True:
                    print("insert - 1 update - 2 remove - 3 get back - 0")
                    request2 = input("Enter your value: ")
                    if request2 == "0":
                        print("get_Back processing ..")
                        print("-------------------------")
                        break
                    if request2 != "1" and request2 != "2" and request2 != "3":
                        print("///////////////////////////////////////////////")
                        print("Please, follow the rules >Enter the valid input")
                        print("///////////////////////////////////////////////\n")
                    else:
                        if request2 == "1": reply = "insert into "
                        if request2 == "2": reply = "update the "
                        if request2 == "3": reply = "remove from "

                        if request1 == "1": reply += "users"
                        if request1 == "2": reply += "questions"
                        if request1 == "3": reply += "answers"
                        if request1 == "4": reply += "tags"

                        print("^^^^^^^^^^^^^^^^^^")
                        print(reply + "?")
                        reply2 = input("\n\tYes - Y| No - any another button: ")
                        if reply2 == "Y":
                            return request1 + " " + request2
                        else:
                            print("get_Back processing ..")
                            print("-------------------------")
                            break