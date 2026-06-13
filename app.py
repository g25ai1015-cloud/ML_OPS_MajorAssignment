import joblib
import numpy as np
from flask import Flask, request, render_template_string
from PIL import Image

app = Flask(__name__)
model = joblib.load('savedmodel.pth')

HTML_FORM = '''
<!doctype html>
<html>
<head><title>MLOps Face Predictor</title></head>
<body>
  <h2>Upload an Olivetti Face Image</h2>
  <form method="post" enctype="multipart/form-data">
    <input type="file" name="file">
    <input type="submit" value="Upload & Predict">
  </form>
</body>
</html>
'''

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files.get('file')
        if file:
            img = Image.open(file).convert('L').resize((64, 64))
            img_array = np.array(img).flatten() / 255.0
            prediction = model.predict([img_array])
            return f"<h3>Predicted Class (Subject ID): {prediction[0]}</h3><a href='/'>Upload another</a>"
    return render_template_string(HTML_FORM)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)