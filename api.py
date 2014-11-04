from flask import Flask
from flask.ext import restful
from flask.ext.restful import reqparse

from crossdomainhelper import *

app = Flask(__name__)
api = restful.Api(app)

projects = {
    'test1': {'id': 'test1', 'title': 'Test1 Project', 'desc': 'Description of the first test project. This is only here to let me see if my script works.'},
    'test2': {'id': 'test2', 'title': 'Second Test Project', 'desc': 'Second description. Nothing really here, it\'s just a little lorem ipsum'},
}

def abort_if_not_project(project_id):
    if project_id not in projects:
        restful.abort(404, message="Project {} doesn't exist").format(project_id)

parser = reqparse.RequestParser()
parser.add_argument('title', type=str)
parser.add_argument('desc', type=str)

class ProjectList(restful.Resource):
    def get(self):
        return projects
    def post(self):
        args = parser.parse_args()
        project_id = 'test%d' % (len(projects) + 1)
        projects[project_id] = {'id': project_id, 'title': args['title'], 'desc': args['desc']}
        return projects[project_id], 201

class Projects(restful.Resource):
    def get(self, project_id):
        abort_if_not_project(project_id)
        return projects[project_id]
    def delete(self, project_id):
        abort_if_not_project(project_id)
        del projects[project_id]
        return '', 204
    def put(self, project_id):
        args = parser.parse_args()
        project = {'title': args['title'], 'desc': args['desc']}
        projects[project_id] = project
        return project, 201

api.add_resource(Projects, '/api/<string:project_id>')
api.add_resource(ProjectList, '/api')

@app.route('/')
def main():
    return app.send_static_file('index.html')

if __name__ == '__main__':
    app.run(debug=True)