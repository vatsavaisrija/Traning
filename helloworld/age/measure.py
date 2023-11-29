from datetime import date

def calculateage(birthDate):
    today = date.today()
    age = today.year - birthDate.year - ((today.month, today.day) <
                                         (birthDate.month, birthDate.day))
    print(age)
    return age

