from flask import Flask, request, render_template

app = Flask(__name__)

# Route to display the form
@app.route('/')
def index():
    return render_template('form.html')  # Load the HTML form

# Route to handle form submission
@app.route('/submit', methods=['POST'])
def submit():
    # Get data from the form
    fname = request.form.get('fname')
    lname = request.form.get('lname')

    # Create a success message or update the form
    success_message = f"Hello, {fname} {lname}! Your data has been submitted."

    # Re-render the form with the success message
    return render_template('form.html', message=success_message)

if __name__ == '__main__':
    app.run(debug=True)
