from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')  # A simple HTML form for Python

@app.route('/submit', methods=['POST'])
def submit_form():
    name = request.form.get('name')
    age = request.form.get('age')
    file = request.files.get('file')

    if name and age and file:
        return jsonify({
            'message': 'Form submitted successfully!',
            'name': name,
            'age': age,
            'file_name': file.filename
        })
    return jsonify({'error': 'Missing data!'}), 400

if __name__ == '__main__':
    app.run(debug=True)
