#!flask/bin/python
from config import engine, usersTable, tasksTable
from flask import abort
from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from flask import Response
from sqlalchemy import create_engine

app = Flask(__name__)
auth = HTTPBasicAuth()
tasks = [
	{
		"id": "1",
		"title": u"Buy groceries",
		"description": u"Milk, Cheese, Pizza, Fruit, Tylenol",
		"done": False
	},
	{
		"id": "2",
		"title": u"Learn Python",
		"description": u"Need to find a good python tutorial on the web",
		"done": False
	}
]
users = {
    "admin": "password"
}

@auth.get_password
def get_password(username):
    try:
        return users[username]
    except:
        return None

@auth.error_handler
def unauthorized():
    return Response("{'error':'Unauthorized Access'}", status=403, mimetype='application/json')

@auth.verify_password
def sign_in(username, password):
	try:
		data = request.args
		if(data["username"] in accounts):
			if(users[data["username"]] == data["password"]):
				return True
		return False
	except:
		return False

@app.route('/register/', methods=['POST'])
def add_user():
	username = dict(request.form)["username"][0];
	password = dict(request.form)["password"][0];
	try:
		users[username];
		return jsonify({
			'success': False
		})
	except:
		users[username] = password;
		return jsonify({
			'success': True
		})		

@app.route('/todo/api/v1.0/tasks/', methods=['GET'])
@auth.login_required
def get_task():
	task_id = None;
	try:
		task_id = dict(request.args)["task_id"][0];
	except:
		return jsonify({'Error 503':'task_id missing'}), 503
	int_checker = True
	try:
		int(task_id)
	except:
		int_checker = False
	response = [];
	for task in tasks:
		if int_checker:
			if task["id"] == str(task_id):
				response.append(task)
				break
		else:
			try:
				if task["title"].lower().index(task_id.lower()) >= 0:
					response.append(task);
			except ValueError as e:
				continue;
	if len(response) == 0:
		return jsonify({})
	return jsonify({'task': response})



@app.route('/todo/api/v1.0/tasks/addtask', methods=['POST'])
@auth.login_required
def add_task():
	addtask = dict(request.form)
	try:
		addtask["title"] = addtask["title"][0]
		addtask["description"] = addtask["description"][0]
		addtask["done"] = False
		seq = [task['id'] for task in tasks]
		addtask["id"] = str(int(max(seq)) + 1)
		tasks.append(addtask)
		return "Task added: "+ addtask["id"]
	except:
		return "Error while including task"
		
@app.route('/todo/api/v1.0/tasks/modtask', methods=['PUT'])
@auth.login_required
def modify_task():
	update_task = dict(request.form)
	try:
		update_task["id"] = update_task["id"][0]
		for task_index in range(len(tasks)):
			if tasks[task_index]["id"] == update_task["id"]:
				tasks[task_index]["title"] = update_task["title"][0]
				tasks[task_index]["description"] = update_task["description"][0]		
				return "Task: "+update_task["id"]+" updated successfully\n"
		return "no changes made"
	except:
		return "Error while adding task"	
		
@app.route('/todo/api/v1.0/tasks/toggledone', methods=['PUT'])
@auth.login_required
def toggle_done():
	update_task = dict(request.form)
	try:
		update_task["id"] = update_task["id"][0]
		for task_index in range(len(tasks)):
			if tasks[task_index]["id"] == update_task["id"]:
				if bool(tasks[task_index]["done"]):
					tasks[task_index]["done"] = False
					return "Task with id#: "+update_task["id"]+" changed to False"
				else:
					tasks[task_index]["done"] = True
					return "Task with id#: "+update_task["id"]+" changed to True"
		return "no changes made"
	except:
		return "Error while updating task"

@app.route('/todo/api/v1.0/tasks/deletetask', methods=['DELETE'])
@auth.login_required
def delete_task():
	task_id = dict(request.form)
	try:
		task_id["id"] = task_id["id"][0]
		for task_index in range(len(tasks)):
			if tasks[task_index]["id"] == task_id["id"]:
				tasks.pop(int(task_id["id"]))
				return "Task with id#: "+update_task["id"]+" deleted"
		return "no changes made"
	except:
		return "Error while adding task"

@auth.error_handler
def unauthorized():
    response = jsonify({'Error 403':'Forbidden'})
    return response, 403

if __name__ == '__main__':
	app.run(debug=False, ssl_context=('cert.pem', 'key.pem'), host='0.0.0.0')


	
	

