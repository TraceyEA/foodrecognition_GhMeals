
import streamlit as st
from PIL import Image

# Nutritional info dictionary
nutritional_info = {
    "Banku and Okro": "High in carbohydrates and fiber. Suitable for diabetes in moderate portions." 
      "**Portion Size for Banku:** About 200g when cooked.\n"
      "**Nutritional Benefits:** High in carbohydrates, calcium and iron.\n"
      "Drink lots of the okro soup accompanying",

    "Banku and Pepper": "High in carbohydrates and fiber. Suitable for diabetes in moderate portions."
    "**Portion Size for Banku:** About 200g cooked.\n"
      "**Nutritional Benefits:** High in carbohydrates, calcium and iron.\n"
      "**Portion Size for protein:** About 30g of protein.\n"
      "Add some chopped vegetables to the pepper, for flavor and to boost nutrition",

    "Fufu and Soup": "High in carbohydrates. Consume with caution for diabetes."
    "**Portion Size for Fufu:** About 200g when cooked.\n"
      "**Nutritional Benefits:** High in carbohydrates, fats and fibre.\n"
      "**Portion Size for protein:** About 30g of protein.\n"
      "Drink lots of the soup accompanying",

    "Yam and Stew": "High in carbohydrates. Consume with caution for diabetes."
    "**Portion Size for Yam:** About 200g when cooked.\n"
      "**Nutritional Benefits:** High in potassium, sodium, vitamins C & B6\n"
      "Eat with lots of stew cooked in little amount of oil",

    "Jollof Rice": "High in carbohydrates. Consume with caution for diabetes."
    "**Portion Size for Jollof:** About 150g cooked.\n"
      "**Nutritional Benefits:** High in Vitamins A & C, iron and magnesium.\n"
      "**Portion Size for Protein:** About 30g when cooked.\n",

    "Fried Rice": "High in carbohydrates and fats. Consume with caution for diabetes."
    "**Portion Size for fried rice:** About 150g cooked.\n"
      "**Nutritional Benefits:** High in fat, calcium, phosphor, iron, Vitamin A & C.\n"
      "**Portion Size for Protein:** About 30g when cooked.\n",

    "Rice and Stew": "High in carbohydrates. Consume with caution for diabetes."
    "**Portion Size for Rice:** About 150g cooked.\n"
      "**Nutritional Benefits:** High in Vitamins A & C, iron, magnesium and fats\n"
      "**Portion Size for Protein:** About 30g when cooked.\n"
      "Eat stew sooked in little amounts of oil",

    "Waakye": "High in carbohydrates and proteins. Suitable for diabetes in moderate portions."
    "**Portion Size for Waakye:** About 200g cooked.\n"
      "**Nutritional Benefits:** High in ron, Vitamin C, Thiamin, Niacin and Folate\n"
      "Eat with lots of vegetables",

    "Beans and Plantain": "High in carbohydrates and fiber. Suitable for diabetes."
    "**Portion Size for Beans:** About 1/2 cup (approximately 130 grams) of cooked beans.\n"
      "**Nutritional Benefits:** High in protein, fiber, vitamins, and minerals.\n"
      "**Portion Size for Plantains:** About 1/3 to 1/2 cup (approximately 75 to 100 grams) of cooked or baked plantains.\n"
      "**Nutritional Benefits:** Provides fiber, vitamins A and C, and potassium.",

    "Banku and Soup": "High in carbohydrates and fiber. Suitable for diabetes in moderate portions."
    "**Portion Size for Banku:** About 250g cooked.\n"
      "**Nutritional Benefits:** High in Vitamins A & C, iron and magnesium.\n"
      "**Portion Size for Protein:** About 30g when cooked.\n"
      "Drink lots of the soup accompanying"

}

def read_predicted_class(file_path):
    # Define a mapping from raw class names to readable names
    class_name_mapping = {
        'banku': 'Banku',
        'banku_and_pepper': 'Banku and Pepper',
        'banku_and_soup': 'Banku and Soup',
        'beans_and_plantain': 'Beans and Plantain',
        'boiled_yam': 'Yam and Stew',
        'fried_rice': 'Fried Rice',
        'fufu': 'Fufu and Soup',
        'jollof': 'Jollof Rice',
        'plain_rice': 'Rice and Stew',
        'rice_and_stew': 'Rice and Stew',
        'waakye': 'Waakye'
    }

    with open(file_path, 'r') as file:
        # Read the predicted class from the file
        content = file.read().strip()
        
        # Remove curly braces and quotes from the string
        if content.startswith("{'") and content.endswith("'}"):
            food_class = content[2:-2]  # Extract the class name from the set-like string
        else:
            # Handle unexpected formats
            food_class = "Unknown"
        
        # Convert the class name to a readable format
        converted_class = class_name_mapping.get(food_class, "Unknown")

    return converted_class
predictedclass= read_predicted_class("output.txt")
# Streamlit app
def app():
    st.title("Welcome Tracey")
    # st.write(str(file.read().strip()))


    # Display the image
    image = Image.open("new_images/captured_image.png")
    st.image(image, caption="Predicted class: " + str(predictedclass))

    # Display meal details when button is clicked
    if st.button("View Details about your meal"):
        st.subheader("Meal Details")
        if predictedclass in nutritional_info:
            st.write(nutritional_info[predictedclass], unsafe_allow_html=True)
        else:
            st.write("No details available for the predicted meal.")

# Run the app
if __name__ == '__main__':
    app()
