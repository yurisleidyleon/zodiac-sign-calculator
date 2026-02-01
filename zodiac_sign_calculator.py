birth_month = input("What is your birth month: ").title()

valid_months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

while birth_month not in valid_months:
    print("Incorrect birth month.")
    birth_month = input("Please enter a valid birth month: ").title()

month_31 = ["January", "March", "May", "July", "August", "October", "December"]
month_30 = ["April", "June", "September", "November"]
month_28 = ["February"]                   # February has 29 days every 4 years

if birth_month in month_30:
    max_day = 30
elif birth_month in month_31:
    max_day = 31
else:
    max_day = 28

if birth_month == "February":
    birth_year = int(input("What year were you born: "))
    if (birth_year % 4 == 0 and birth_year % 100 != 0) or (birth_year % 400 == 0):
        max_day = 29
        print("Congrats!!!")
        print("You are extra especial!!!")
    else:
        max_day = 28

birth_day = int(input("What is your birth day: "))

while birth_day < 1 or birth_day > max_day:
    print("Incorrect day of the month.")
    birth_day = int(input("What is your birth day: "))


#Only missing the zodiac sign assigment code

zodiac_traits = {
    "Aries": "Bold, energetic, and confident. You love taking the lead and facing challenges head-on.",
    "Taurus": "Reliable, patient, and practical. You value stability, comfort, and loyalty.",
    "Gemini": "Curious, social, and adaptable. You love learning and communicating with others.",
    "Cancer": "Emotional, caring, and intuitive. You value family, comfort, and deep connections.",
    "Leo": "Confident, passionate, and charismatic. You love being admired and inspiring others.",
    "Virgo": "Detail-oriented, analytical, and hardworking. You enjoy helping and improving things.",
    "Libra": "Balanced, fair, and social. You value harmony, beauty, and strong relationships.",
    "Scorpio": "Intense, loyal, and mysterious. You feel deeply and are very determined.",
    "Sagittarius": "Adventurous, optimistic, and independent. You love freedom and exploration.",
    "Capricorn": "Responsible, disciplined, and ambitious. You work hard to achieve your goals.",
    "Aquarius": "Innovative, independent, and intelligent. You think outside the box.",
    "Pisces": "Compassionate, creative, and emotional. You are very intuitive and empathetic."
}

if (birth_month == "March" and birth_day >= 21) or (birth_month == "April" and birth_day <= 19):
    zodiac_sign = "Aries"
elif (birth_month == "April" and birth_day >= 20) or (birth_month == "May" and birth_day <= 20):
    zodiac_sign = "Taurus"
elif (birth_month == "May" and birth_day >= 21) or (birth_month == "June" and birth_day <= 20):
    zodiac_sign = "Gemini"
elif (birth_month == "June" and birth_day >= 21) or (birth_month == "July" and birth_day <= 22):
    zodiac_sign = "Cancer"
elif (birth_month == "July" and birth_day >= 23) or (birth_month == "August" and birth_day <= 22):
    zodiac_sign = "Leo"
elif (birth_month == "August" and birth_day >= 23) or (birth_month == "September" and birth_day <= 22):
    zodiac_sign = "Virgo"
elif (birth_month == "September" and birth_day >= 23) or (birth_month == "October" and birth_day <= 22):
    zodiac_sign = "Libra"
elif (birth_month == "October" and birth_day >= 23) or (birth_month == "November" and birth_day <= 21):
    zodiac_sign = "Scorpio"
elif (birth_month == "November" and birth_day >= 22) or (birth_month == "December" and birth_day <= 21):
    zodiac_sign = "Sagittarius"
elif (birth_month == "December" and birth_day >= 22) or (birth_month == "January" and birth_day <= 19):
    zodiac_sign = "Capricorn"
elif (birth_month == "January" and birth_day >= 20) or (birth_month == "February" and birth_day <= 18):
    zodiac_sign = "Aquarius"
else:
    zodiac_sign = "Pisces"

print("Your zodiac sign is:", zodiac_sign)

print("Characteristics:")
print(zodiac_traits[zodiac_sign])



