


from flask import Flask
import random
import string

 
def generate_password(length, count):
    passwords = []
    for i in range(count):
        password = ''. join(random. choice(string. ascii_letters + string. digits + string. punctuation) for _ in range(length))
        passwords. append(password)
        return passwords

app = Flask(__name__)

@app.route('/')

def hello_name():
    password = generate_password(10, 1)
    return 'Your new password is: %s' %  password
     
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4567)


