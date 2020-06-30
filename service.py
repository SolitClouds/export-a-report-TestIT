# coding: utf8

import sections
from api import *

from flask import Flask, render_template, make_response


app = Flask(__name__)


@app.context_processor
def inject_enumerate():
    return dict(enumerate=enumerate)


@app.route('/')
def api():
    return render_template(
        "index.html",
        project_list=get_list_projects(),
        templates=['Default']
    )


@app.route('/html/<project_id>')
def html(project_id):

    struct = sections.get_struct(project_id)
    flat = sections.tree_to_flat(struct)
    project_name = [v for k, v in get_list_projects().items() if k == project_id][0]

    return render_template(
        "templates_default.html",
        title=project_id,
        flat=flat,
        name_project=project_name
    )


@app.route('/pdf/<project_id>')
def pdf(project_id):

    cases = []
    for work_item_id in get_project_work_items(project_id):
        cases.append(get_work_item(work_item_id))

    for case in cases:
        for attach in case['attachments']:
            load_image("/api/Attachments/" + attach['id'])
        for step in case['steps']:
            step['expected'] = step['expected'].replace("/api/Attachments", "/static")

    response = ""
    # html_template = render_template('templates_default.html', title=project_id, cases=cases)
    # pdf_file = HTML(string=html_template).write_pdf()
    # response = make_response(pdf_file)
    # response.headers['Content-Type'] = 'application/pdf'
    # response.headers['Content-Disposition'] = \
    #     'inline; filename=%s.pdf' % 'yourfilename'
    return response


if __name__ == '__main__':
    app.run()

