from flask import Flask, render_template, request # type: ignore

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        radius_input = request.form.get('radius', '').strip()
        if not radius_input:
            return render_template('index.html', result=None)
        radius = float(radius_input)
        if radius < 0:
            return render_template('index.html', result=None)
        area = round(3.14159 * radius ** 2, 2)
        return render_template('index.html', radius=radius, result=area)
    except (ValueError, TypeError):
        return render_template('index.html', result=None)

if __name__ == '__main__':
    import os
    app.run(host='0.0.0.0', port=5000, debug=os.getenv('FLASK_DEBUG', 'False').lower() == 'true')
