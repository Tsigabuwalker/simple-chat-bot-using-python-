import random
import requests
from datetime import datetime

def chatbot():
    print("Chatbot: Hello! I am your upgraded chatbot. Type 'exit' to end the chat.")
    print("Chatbot: I can help with general queries, tell jokes, provide weather updates, and more!")

    while True:
        user_input = input("You: ").lower()

        # Exit condition
        if user_input in ["exit", "bye"]:
            print("Chatbot: Goodbye! Have a great day!")
            break
        
        # Greetings
        elif "hello" in user_input or "hi" in user_input:
            print("Chatbot: Hi there! How can I assist you?")
        
        # Ask the chatbot's name
        elif "your name" in user_input:
            print("Chatbot: I'm ChatMaster, your friendly chatbot assistant!")
        
        # How are you
        elif "how are you" in user_input:
            print("Chatbot: I'm doing great, thank you! How about you?")
        
        # Tell a joke
        elif "joke" in user_input:
            jokes = [
                "Why don't scientists trust atoms? Because they make up everything!",
                "Why did the scarecrow win an award? Because he was outstanding in his field!",
                "What do you call fake spaghetti? An impasta!"
            ]
            print(f"Chatbot: {random.choice(jokes)}")
        
        # Current time
        elif "time" in user_input:
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            print(f"Chatbot: The current time is {current_time}.")
        
        # Weather information
        elif "weather" in user_input:
            city = input("Chatbot: Please enter your city: ").strip()
            try:
                # OpenWeatherMap API (replace 'your_api_key' with a real API key)
                api_key = "your_api_key"
                url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
                response = requests.get(url)
                weather_data = response.json()

                if weather_data["cod"] == 200:
                    temp = weather_data["main"]["temp"]
                    description = weather_data["weather"][0]["description"]
                    print(f"Chatbot: It's currently {temp}°C with {description} in {city}.")
                else:
                    print("Chatbot: Sorry, I couldn't fetch the weather for that location.")
            except Exception as e:
                print("Chatbot: There was an error retrieving the weather. Please try again later.")
        
        # Basic math operations
        elif any(op in user_input for op in ["add", "subtract", "multiply", "divide"]):
            try:
                print("Chatbot: Let's do some math! (Type 'cancel' to exit math mode)")
                while True:
                    math_input = input("Chatbot (Math): ").lower()
                    if math_input == "cancel":
                        print("Chatbot: Exiting math mode.")
                        break
                    try:
                        result = eval(math_input)
                        print(f"Chatbot: The result is {result}")
                    except Exception:
                        print("Chatbot: That seems like an invalid math operation. Please try again.")
            except Exception as e:
                print("Chatbot: There was an error performing the calculation.")
        
        # Fallback response
        else:
            print("Chatbot: I'm not sure I understand that. Can you please rephrase?")

# Run the chatbot
chatbot()
