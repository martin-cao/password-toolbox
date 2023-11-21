from password_security.start import clf


def check(pwd: str):
    return clf(pwd)


def checker():
    input_pwd: str = input("Please input your password: ")
    print("Secure:", check(input_pwd)[0])
