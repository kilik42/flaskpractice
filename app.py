from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)

JOBS= [
    {'title': 'Software Engineer',
      'company': 'Google', 
      'location': 'Mountain View, CA',
      'salary': '$100,000'
        
    },
    {'title': 'Software Engineer',
     'company': 'Facebook',
     'location': 'Menlo Park, CA',
     'salary': '$120,000'
     },
    {'title': 'Software Engineer',
      'company': 'Apple',
    'location': 'Cupertino, CA',
    'salary': '$110,000'
    },
    {
        'title': 'Software Engineer',
        'company': 'Amazon',
        'location': 'Seattle, WA',
        'salary': '$115,000'
    }
]

@app.route('/')
def index():
    return render_template('index.html', jobs = JOBS, company_name = 'Google')

if __name__ == '__main__':
    app.run(debug=True)