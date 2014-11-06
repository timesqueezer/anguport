from flask import jsonify
from flask.ext import restful
from flask.ext.restful import reqparse

from ngptf import app, db, api_rest
from ngptf.models import Project, ProjectSchema

def project_or_abort(project_id):
    p = Project.query.get(project_id)
    if p == None:
        restful.abort(404, message="Project {} doesn't exist").format(project_id)
    else:
        return p

parser = reqparse.RequestParser()
parser.add_argument('title', type=str)
parser.add_argument('desc', type=str)

project_list_schema = ProjectSchema()

def as_json(project):
    return project_list_schema.dump(project).data

class ProjectList(restful.Resource):
    def get(self):
        l = []
        for p in Project.query.all():
            l.append(as_json(p))
        return l
            
    def post(self):
        args = parser.parse_args()
        p = Project(title=args['title'], desc=args['desc'])
        db.session.add(p)
        db.session.commit()
        return as_json(p), 201

class Projects(restful.Resource):
    def get(self, project_id):
        p = project_or_abort(project_id)
        return as_json(p)
    def delete(self, project_id):
        p = project_or_abort(project_id)
        db.session.delete(p)
        db.session.commit()
        return '', 204
    def put(self, project_id):
        args = parser.parse_args()
        p = project_or_abort(project_id)
        p.title = args['title']
        p.desc = args['desc']
        db.session.commit()
        return as_json(p), 201

api_rest.add_resource(Projects, '/api/<string:project_id>')
api_rest.add_resource(ProjectList, '/api')