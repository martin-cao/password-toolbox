from password_security.start import clf
import pyperclip

def check(pwd: str):
    return clf(pwd)

def checkJustGenerated():
    print("Secure:", check(pyperclip.paste())[0])

def checker():
    input_pwd: str = input("Please input your password: ")
    print("Secure:", check(input_pwd)[0])
