from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    result = 0
    error = None

    if request.method == 'POST':
        try:    
            kms = float(request.form['kms'])
            fuel = float(request.form['fuel'])

            if fuel <= 0:
                error = "Fuel consumption must be greater than zero."
            elif kms < 0:
                error = "Kilometers driven cannot be negative."
            else:
                result = round(kms / fuel, 2)

        except ValueError:
            error = "Please enter valid numbers for kilometers and fuel."

    return render_template('index.html', result=result, error=error)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    

    
            