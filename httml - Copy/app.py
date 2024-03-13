from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/profile', methods=['POST'])
def profile():
    user_id = request.form.get('id')
    data = load_data('data.csv')
    user = find_user_by_id(data, user_id)

    return render_template('profile1.html', user=user)

def load_data(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        header = lines[0].strip().split(',')
        data = [dict(zip(header, line.strip().split(','))) for line in lines[1:]]
    return data

def find_user_by_id(data, user_id):
    for user in data:
        if user['id'] == user_id:
            return user
    return None

if __name__ == '__main__':
    app.run(debug=True)
