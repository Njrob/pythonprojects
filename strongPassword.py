import re

def strongPassword(password):
    capsReg = re.compile(r"[A-Z]")
    lowersReg = re.compile(r"[a-z]")
    digitsReg = re.compile(r"\d")
    if len(password) < 8:
        print("Your password needs to be at least 8 characters long.  Please try again.")
    else:
        if capsReg.search(password) and lowersReg.search(password) and digitsReg.search(password):
            print("You've got a strong password.")
        else:
            print("Your password is not strong, try again.")

password1 = 'abc!@#123ABC<>/.,{}\\|'
password2 = 'lemao'
password3 = 'KrakAtoa12'
strongPassword(password1)
strongPassword(password2)
strongPassword(password3)
