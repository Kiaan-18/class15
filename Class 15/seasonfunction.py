def weather_conditions(season):
    if season=="autum":
        print("the climate is cold but not freezing")
    elif season=="spring":
        print("the climate is warm")
    else:
        print("Enter a proper season")
season=input("Enter a season:")
weather_conditions(season)