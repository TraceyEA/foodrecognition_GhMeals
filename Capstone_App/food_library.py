import streamlit as st
import os
import base64  # Importing base64 because of my encoding images

# Nutritional content data
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

def app():
    # List of local image file paths
    image_paths = [
        "images/bankuandokro.jpeg",
        "images/bankuandpepper.jpeg",
        "images/fufuandsoup.jpeg",
        "images/yamandstew.jpeg",
        "images/jollof.jpeg",
        "images/friedrice.jpeg",
        "images/riceandstew.jpeg",
        "images/waakye.jpeg",
        "images/beansandplantain.jpeg",
        "images/bankuandsoup.jpeg"
    ]

    # Corresponding descriptions for each image
    descriptions = [
        "Banku and Okro",
        "Banku and Pepper",
        "Fufu and Soup",
        "Yam and Stew",
        "Jollof Rice",
        "Fried Rice",
        "Rice and Stew",
        "Waakye",
        "Beans and Plantain",
        "Banku and Soup"
    ]

    # CSS for styling
    st.markdown(
        """
        <style>
        .image-container {
            display: inline-block;
            width: 100%;
            height:150px;
            margin: 1%;
            border: 2px solid black;
            position: relative;
            overflow: hidden;
        }
        .image-container img {
            width: 100%;
            height: 100%;
            transition: transform 0.3s ease;
        }
        .image-container:hover img {
            transform: scale(1.1);
        }
        .image-container .description {
            position: absolute;
            bottom: 0;
            background: rgba(0, 0, 0, 0.5);
            color: white;
            width: 100%;
            text-align: center;
            padding: 10px;
            opacity: 0;
            transition: opacity 0.3s ease;
        }
        .image-container:hover .description {
            opacity: 1;
        }
        </style>
        """, unsafe_allow_html=True
    )

    # Display the images with descriptions
    st.title("Food Gallery")
    st.write("Gallery of images of Ghanaian foods and their nutritional Contents")
    st.write("Click on the button for more info")
    # Arrange images 3 per line
    for i in range(0, len(image_paths), 3):
        cols = st.columns(3)
        for col, j in zip(cols, range(i, i + 3)):
            if j < len(image_paths):
                with col:
                    with open(image_paths[j], "rb") as image_file:
                        encoded_image = base64.b64encode(image_file.read()).decode()
                    if col.button(f"{descriptions[j]}"):
                        st.sidebar.header(descriptions[j])
                        st.sidebar.write(nutritional_info[descriptions[j]])
                    col.markdown(
                        f"""
                        <div class="image-container">
                            <img src="data:image/jpeg;base64,{encoded_image}" alt="Image {j + 1}">
                            <div class="description">{descriptions[j]}</div>
                        </div>
                        """, unsafe_allow_html=True
                    )

if __name__ == "__main__":
    app()
