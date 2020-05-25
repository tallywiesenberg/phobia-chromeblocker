from flask import Flask, render_template, request

from .edits import PageEditor

def create_app():
    '''Create and configure instance of the Flask framework'''
    app = Flask(__name__)
    app.config['DEBUG'] = True

    @app.route('/demo')
    def demo():
        pe = PageEditor(keyword='spider', orientation='block')
        output = pe.edit()
        return render_template('demo.html', output=output)

    @app.route('/<keyword>/<orientation>/<site>', methods=['POST', 'GET'])
    def edit(keyword, orientation, site):
        pe = PageEditor(keyword, orientation, site)
        output = pe.edit()
        return render_template('demo.html', output=output)

    return app