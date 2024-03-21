import os
if __name__ == '__main__':
    print("welcome to robo speaker made by harsh (enter:-q  to queet)")
    while True:
        x = input("what you want speak :")
        if x == "q":
            os.system("say 'ok . its good to meet you' ")
            break
        command = f"say {x}"
        os.system(command)



