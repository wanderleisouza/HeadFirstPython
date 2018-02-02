from flask import Flask, render_template, request, redirect, escape

import vsearch
from pkg_resources import _ReqExtras

app = Flask(__name__)

FILE_NAME = 'vsearch.log'


def log_request(req: 'flask_request', res: str) -> None:
    with open(FILE_NAME, 'a') as log:
        print(req.form, req.remote_addr, req.user_agent, res, file=log, sep='|')


@app.route('/viewlog')
def view_log() -> 'html':
    contents = []
    with open(FILE_NAME) as log:
        for line in log:
            contents.append([])
            for item in line.split('|'):
                contents[-1].append(escape(item))
    titles = ('Form Data', 'Remote Addr', 'User Agent', 'Results')

    return render_template('viewlog.html',
                           the_title='View Log',
                           the_row_titles=titles,
                           the_data=contents,)


@app.route('/')
def hello() -> '302':
    return redirect('/entry')


@app.route('/search4', methods=['POST'])
def do_search() -> 'html':
    phrase = request.form['phrase']
    letters = request.form['letters']
    title = 'Here are your results:'
    results = str(vsearch.search_for_letters(phrase, letters))
    log_request(request, results)
    return render_template('results.html',
                           the_phrase=phrase,
                           the_title=title,
                           the_letters=letters,
                           the_results=results,
                           )


@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html', the_title='Welcome to search_for_letters on the web!')


if __name__ == '__main__':
    app.run(debug=True)
