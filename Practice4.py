weather_data = {
    'New York': {'temperature': 15, 'humidity': 60, 'condition': 'Cloudy'},
    'Los Angeles': {'temperature': 22, 'humidity': 40, 'condition': 'Sunny'},
    'Chicago': {'temperature': 10, 'humidity': 70, 'condition': 'Rainy'},
    'Miami': {'temperature': 28, 'humidity': 80, 'condition': 'Humid'},
    'San Francisco': {'temperature': 17, 'humidity': 50, 'condition': 'Foggy'}
}

forecast_data = {
    'New York': [15, 16, 14, 13, 12],
    'Los Angeles': [22, 23, 24, 21, 20],
    'Chicago': [10, 12, 14, 13, 11],
    'Miami': [28, 29, 27, 30, 31],
    'San Francisco': [17, 18, 16, 15, 17]
}

print("Welcome to the Weather App Simulation!\n")

while True:
    print("Choose an option:")
    print("1. Check current weather of a city")
    print("2. Compare temperatures of two cities")
    print("3. Get 5-day forecast for a city")
    print("4. Exit")
    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        city = input("Enter city name: ").title()
        if city in weather_data:
            weather = weather_data[city]
            print(f"The current weather in {city} is:")
            print(f"Temperature: {weather['temperature']}°C")
            print(f"Humidity: {weather['humidity']}%")
            print(f"Condition: {weather['condition']}\n")
        else:
            print("City not found in the database.\n")

    elif choice == "2":
        city1 = input("Enter the first city: ").title()
        city2 = input("Enter the second city: ").title()
        if city1 in weather_data and city2 in weather_data:
            temp1 = weather_data[city1]['temperature']
            temp2 = weather_data[city2]['temperature']
            print(f"The temperature in {city1} is {temp1}°C.")
            print(f"The temperature in {city2} is {temp2}°C.")
            if temp1 > temp2:
                print(f"{city1} is warmer than {city2}.\n")
            elif temp1 < temp2:
                print(f"{city2} is warmer than {city1}.\n")
            else:
                print(f"{city1} and {city2} have the same temperature.\n")
        else:
            print("One or both cities not found in the database.\n")

    elif choice == "3":
        city = input("Enter city name: ").title()
        if city in forecast_data:
            print(f"The 5-day forecast for {city} is:")
            for i, temp in enumerate(forecast_data[city]):
                print(f"Day {i+1}: {temp}°C")
            print()
        else:
            print("City not found in the database.\n")

    elif choice == "4":
        print("Thank you for using the Weather App Simulation. Goodbye!")
        break

    else:
        print("Invalid choice. Please select a valid option.\n")
