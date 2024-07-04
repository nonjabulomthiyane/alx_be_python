# weather_advice.py

def main():
    # Prompt user for weather input
    weather = input("What's the weather like today? (sunny/rainy/cold): ").strip().lower()
    
    # Provide clothing recommendations based on weather input
    if weather == 'sunny':
        print("Recommendation: Wear a t-shirt and sunglasses.")
    elif weather == 'rainy':
        print("Recommendation: Don't forget your umbrella and a raincoat.")
    elif weather == 'cold':
        print("Recommendation: Make sure to wear a warm coat and a scarf.")
    else:
        print("Sorry, I don't have recommendations for this weather.")

if __name__ == "__main__":
    main()

