
Handwritten Digit Recognition API

This repository hosts a Flask API for predicting handwritten digits utilizing a Convolutional Neural Network (CNN) trained on the MNIST dataset.

Overview
The purpose of this project is to provide a simple and efficient API for recognizing handwritten digits. It utilizes a pre-trained Keras model to perform predictions on input images.

Setup
Clone the Repository: You can clone this repository using Git:

bash
Copy code
git clone https://github.com/your_username/your_repository.git

Install Dependencies: Install the required Python dependencies using pip:
Copy code
pip install -r requirements.txt

Download Pre-trained Model: Download the pre-trained Keras model file (Pridic_hand_writing_via_CNN_MNIST.keras) and place it in the root directory of the project.

Usage

Start the Flask Server: Run the Flask server by executing the following command in your terminal:
Copy code
python app.py

Access the API: Once the server is running, you can access the API at http://127.0.0.1:5000/predict.
Send Requests: Send a POST request to the /predict endpoint with an image file containing a handwritten digit. You can use tools like curl or Postman for testing.Example using curl:
perl

Copy code

curl -X POST -F "image=@path_to_your_image_file" http://127.0.0.1:5000/predict
Replace path_to_your_image_file with the path to your image file.

API Endpoints

GET /predict: Returns a message confirming that the API is working.

POST /predict: Accepts an image file containing a handwritten digit, processes it, and returns the predicted digit.
File Structure

app.py: Main Flask application file containing API routes and model prediction logic.

Pridic_hand_writing_via_CNN_MNIST.keras: Pre-trained Keras model for digit recognition.
requirements.txt: List of Python dependencies required for running the application.
Contributing
Contributions are welcome! If you find any issues or want to add new features, feel free to open a pull request or submit an issue.

License
This project is licensed under the MIT License - see the LICENSE file for details.

