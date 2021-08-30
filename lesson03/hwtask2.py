from datetime import datetime
currentyear = datetime.now().year

def profile_summary(first_name, last_name, birth_year, city, email, phone):
    """Returns user information by single string"""
    print(
        f"{first_name} {last_name}, {currentyear - birth_year} years old from {city}. Contacts: {email}, {phone}")


profile_summary(
    first_name = "Andrew",
    last_name = "Cheremkin",
    birth_year = 1995,
    city = "Yakutsk",
    email = "acheremkin@myma.il",
    phone = "+78003335577"
)
