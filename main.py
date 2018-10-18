from flask import Flask, request
from caesar import rotate_character
app = Flask(__name__)
app.config['DEBUG'] = True

form="""
<!doctype html>
 <html>
    <head>
        <style>
            form {
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }
            textarea {
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }
        </style>
    </head>
    <body>
     <form method="post">
     <div>
     <label for="rot">Rotate by:</label>
     <input type="text" name="rot" value="0">
     <p class="error"></p>
     </div>
     <textarea type="text" name="text">{0}</textarea>
     <br>
     <input type="submit">
    </form>
    </body>
</html>
"""   
@app.route("/")
def index():
    return form

@app.route("/", methods=['POST']) 
def alphabet_position (letter):
    alphabet ="abcdefghijklmnopqrstuvwxyz" #Lists alphabet for a key
    lower_letter = letter.lower()   #Makes any input lowercase.
    return alphabet.index(lower_letter) #Returns the position of input as a number. 

""" @app.route("/", methods=['POST'])  
def rotate_character(char, rot):      #says already defined on line 2
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    if char.isalpha():
        a = alphabet_position(char)
        a = (a + rot) % 26            #needs modulo
        a = (alphabet[a])
        if char.isupper():
            a = a.title()
        return a
    else:
       return char  """
    
@app.route("/", methods=['POST']) 
def encrypt(text, rot):
    new_text = ""
    for char in text:
        new_char = rotate_character(char, rot)
        new_text += str(new_char)
    return '<h1>new_text</h1>'


""" @app.route("/hello", methods=['POST'])
def hello():
    first_name = request.form['first_name']
    return '<h1>Hello, ' + first_name +'</h1>'   """


   
app.run()  

