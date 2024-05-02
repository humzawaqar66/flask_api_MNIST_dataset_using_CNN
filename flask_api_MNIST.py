from flask import Flask, request, jsonify
import keras
import numpy as np
import cv2

app = Flask(__name__)

model = keras.models.load_model('Pridic_hand_writing_via_CNN_MNIST.keras')

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'GET':
        return jsonify({'message': 'API is working!'}), 200
    
    elif request.method == 'POST':
        try:
            if 'image' not in request.files:
                return jsonify({'error': 'No image file found,select the key as image!'}), 400
            
            uploaded_files = request.files.getlist('image')
            
            if len(uploaded_files) > 1:
                return jsonify({'message': 'Multiple files have been selected,please choose one!'}), 200
            
            predictions = []
            for uploaded_file in uploaded_files:
                image_data = uploaded_file.read()
                
                if not image_data:
                    return jsonify({'error': 'Empty image data'}), 400

                nparr = np.frombuffer(image_data, np.uint8)
                img = cv2.imdecode(nparr, cv2.IMREAD_GRAYSCALE)
                
                if img is None:
                    return jsonify({'error': 'Failed to decode image'}), 400
                
                img = cv2.resize(img, (28, 28))
                img = img.reshape(1, 28, 28, 1)
                img = img.astype('float32') / 255.0
                
                prediction = model.predict(img)
                predicted_digit = np.argmax(prediction[0])
                
                predictions.append(int(predicted_digit))
            
            return jsonify({'predicted_digits': predictions})
        
        except Exception as e:
            return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
