from flask import Flask, render_template

app=Flask(__name__)


@app.route('/')

@app.route('/Home')
def homepage():
    return render_template('homepage.html', title= "Home Page")

@app.route('/Resume')
def resume():
    return render_template('Resume.html', title= "Resume")

@app.route('/Projects')
def projects():
    return render_template('Projects.html', title= "Projects")
    
@app.route('/Certifications')
def certifications():
    return render_template('Certifications.html', title= "Certifications")



if __name__ == "__main__":
    app.run(debug=True)