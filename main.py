from flask import Flask , render_template
from wtforms import StringField , SubmitField , RadioField , IntegerField
from flask_wtf import FlaskForm
from flask import request
from wtforms.validators import DataRequired
from flask_bootstrap import Bootstrap5

import random

upper_case_characters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
lower_case_characters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
all_symbols = ['@' , '#' , '$' , '%' , '^' , '&' , '*' , '(' , ')' , '-' , '_' , '+' , '=' , '[' , ']' , '{' , '}' , '/' , '?']
all_numbers = ['0','1','2','3','4','5','6','7','8','9']

def create_pass(upper , lower , number , symbol):
    characters = []
    if upper == 'Yes':
        characters += upper_case_characters
    if lower == 'Yes':
        characters += lower_case_characters
    if symbol == 'Yes':
        characters += all_symbols
    if number == 'Yes':
        characters += all_numbers
    
    return characters 

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
bootstrap = Bootstrap5(app)

class PassForm(FlaskForm):
    pass_length = IntegerField('Enter Password Length ' , validators=[DataRequired()])
    include_upper_case  = RadioField('Include Uppercase letters' , choices=['Yes' , 'No'])
    include_lower_case = RadioField('Include Lowercase letters' , choices=['Yes' , 'No'])
    include_numbers = RadioField('Include Numbers' , choices=['Yes' , 'No'])
    include_symbols  = RadioField('Include Symbols' , choices=['Yes' , 'No'])
    submit = SubmitField('Generate')



@app.route('/' , methods = ['GET' , 'POST'])
def home():
    random_pass = ''
    form = PassForm()
    if request.method == 'POST':
        pass_length = request.form['pass_length']
        include_upper_case = request.form['include_upper_case']
        include_lower_case = request.form['include_lower_case']
        include_numbers = request.form['include_numbers']
        include_symbols = request.form['include_symbols']

        characters_to_be_used = create_pass(include_upper_case , include_lower_case , include_numbers , include_symbols)
        if len(characters_to_be_used) == 0:
            return "<h1>Password can not be created as none of the character type is selected"
    
        upper_bound = len(characters_to_be_used)
        print(upper_bound)
        for i in range(int(pass_length)):
            random_idx = random.randint(0 , upper_bound-1)
            random_pass += characters_to_be_used[random_idx]
            

        print(random_pass)

    return render_template('index.html' , form = form , random_pass = random_pass)

if __name__ == '__main__':
    app.run(debug=True)