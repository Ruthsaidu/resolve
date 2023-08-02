def save_data(data):
    fieldnames = ['name', 'email', 'age']  # Add more fields here

    try:
        with open('data.csv', 'a', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerow(data)
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False

@app.route('/', methods=['GET', 'POST'])
def data_collection():
    if request.method == 'POST':
        data = {
            'name': request.form['name'],
            'email': request.form['email'],
            'age': request.form['age'],
            # Add more fields as needed
        }

        if save_data(data):
            return redirect('/thankyou')  # Redirect to the 'thankyou' page after successful submission
        else:
            return "An error occurred while saving data. Please try again later."

    return render_template('form.html')

@app.route('/thankyou')
def thankyou():
    return render_template('thankyou.html')

if __name__ == "__main__":
    app.run(debug=True)
