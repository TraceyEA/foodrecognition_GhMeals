Project Name: Food Recognition and recommendation system for diabetic patients
Project Overview: To build a food recognition and recommnedation systemf or select Ghanaian meals for diabetic patients
                  to shy away from the tradition where people totally avoid certain foods and are forced to enjoy other meals.

To run the code and the app successfully, 

1. Download the training, validation and testing images appropriately, 
    these are saved as food_images_train, food_images_val and food_images_test.
2. Download the source code (python notebook) saved as TraceyAgbevem_CapstoneFinal.ipynb

    To run the code make sure to have jupyter notebook installed, alternatively you can use google collab.

    Additionally, make sure to install these libraries or packages using the code below
        pip install Pillow torch torchvision scikit-learn seaborn matplotlib numpy opencv-python
    
    Open the code in jupyter notebook or google collab after installation

3. Download the code for the app in the folder Capstone_App.
    to run this code, have a python IDE installed on your PC such as visual studio code and import the streamlit library
    open your terminal and navigate to the location of the app files.
    to run the app, type 
        streamlit run side_bar.python
        you can replace side_bar.py with the file name for any of the app files ypu want to check out
    
    this would open in your browser the web app

4. in the app navigate to the camera hub and take a photo, 
    now run your notebook function that predicts on the image
    if you have not yet run the entire notebook, run all cells in the notebook first. 
    open the hometab to view the predicted class and food portions




