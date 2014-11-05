from flask import jsonify
from flask.ext import restful
from flask.ext.restful import reqparse

from ngptf import app, api_rest
from ngptf.models import Project

def abort_if_not_project(project_id):
    if Project.query.filter_by(id = project_id) == None:
        restful.abort(404, message="Project {} doesn't exist").format(project_id)

parser = reqparse.RequestParser()
parser.add_argument('title', type=str)
parser.add_argument('desc', type=str)

class ProjectList(restful.Resource):
    def get(self):
        return jsonify(Project.query.all())
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

api_rest.add_resource(Projects, '/api/<string:project_id>')
api_rest.add_resource(ProjectList, '/api')

@app.route('/')
def main():
    return app.send_static_file('index.html')

if __name__ == '__main__':
    app.run(debug=True)