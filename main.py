from flask import Flask, request
from caesar import rotate_string
app = Flask(__name__)
app.config['DEBUG'] = True

form="""
<!doctype html>
<html>
   <head>
       <style>
           form {{
               background-color: #eee;
               padding: 20px;
               margin: 0 auto;
               width: 540px;
               font: 16px sans-serif;
               border-radius: 10px;
           }}
           textarea {{
               margin: 10px 0;
               width: 540px;
               height: 120px;
           }}
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

# def alphabet_position (letter):
#    alphabet ="abcdefghijklmnopqrstuvwxyz" #Lists alphabet for a key
#    lower_letter = letter.lower() #Makes any input lowercase.  
#    return alphabet.index(lower_letter) 

""" def alphabet_position(letter):
   alphabet ="abcdefghijklmnopqrstuvwxyz" #Lists alphabet for a key
   lower_letter = letter.lower() #Makes any input lowercase.
   for letter in alphabet:  
       return alphabet.index(lower_letter) #Returns the position of input as a number. """


""" def encrypt(text, rot):
   for char in text:
       print(char)
       new_char = rotate_character(char, rot)
       text += str(new_char)
   return "" """

""" @app.route("/", methods=['POST'])
def get_text(text):
   text=input("Type your text here.")
   return text """

@app.route("/", methods=['POST'])
def submission():
  rot = request.form['rot']
  text = request.form['text']
  return form.format(rotate_string(text, rot))

@app.route("/")
def index():
   return form.format("")

""" @app.route("/hello", methods=['POST'])Con
def hello():
   first_name = request.form['first_name']
   return '<h1>Hello, ' + first_name +'</h1>'   """



app.run()

