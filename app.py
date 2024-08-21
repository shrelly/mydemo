from flask import Flask

app=Flask(__name__)

@app.route('/')
def hello():
    return 'Haaaaaaafdasdaa'

@app.route('/page/<page>')
@app.route('/page')
@app.route('/page/')
def page_show(page=1):
    return '这展示第{}页'.format(page)
# if __name__ == '__main__':
#     app.run()S