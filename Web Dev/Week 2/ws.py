#!flask/bin/python
from flask import abort
from flask import Flask, jsonify, request

app = Flask(__name__)

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

@app.route('/todo/api/v1.0/tasks/', methods=['GET'])
def get_tasks():
	return jsonify({
		'tasks': tasks
	})

@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
	response = [];
	for task in tasks:
		if task["id"] == str(task_id):
			response.append(task)
			break
	if len(response) == 0:
		abort(404)
	return jsonify({
		'task': response[0]
	})

@app.route('/todo/api/v1.0/tasks/addtask', methods=['POST'])
def new_task():
	addtask = dict(request.form)
	try:
		addtask["title"] = addtask["title"][0]
		addtask["description"] = addtask["description"][0]
		addtask["done"] = False
		seq = [task['id'] for task in tasks]
		addtask["id"] = str(int(max(seq)) + 1)
		tasks.append(addtask)
		return "Task added successfully with id#: "+ addtask["id"]+"\n"
	except:
		return "Error while adding task"
		
@app.route('/todo/api/v1.0/tasks/updatetask', methods=['PUT'])
def update_task():
	updatetask = dict(request.form)
	try:
		updatetask["id"] = updatetask["id"][0]
		for task_index in range(len(tasks)):
			if tasks[task_index]["id"] == updatetask["id"]:
				tasks[task_index]["title"] = updatetask["title"][0]
				tasks[task_index]["description"] = updatetask["description"][0]		
				return "updated successfully"
		return "no changes made"
	except:
		return "Error Occurred"	
		
@app.route('/todo/api/v1.0/tasks/toggledone', methods=['PUT'])
def toggle_done():
	update_task = dict(request.form)
	try:
		update_task["id"] = update_task["id"][0]
		for task_index in range(len(tasks)):
			if tasks[task_index]["id"] == update_task["id"]:
				if bool(tasks[task_index]["done"]):
					tasks[task_index]["done"] = False
					return "Marked as undone successfully"
				else:
					tasks[task_index]["done"] = True
					return "Marked as done successfully"
		return "no changes made"
	except:
		return "Error Occurred"

@app.route('/todo/api/v1.0/tasks/removetask', methods=['DELETE'])
def remove_task():
	task_id = dict(request.form)
	try:
		task_id["id"] = task_id["id"][0]
		for task_index in range(len(tasks)):
			if tasks[task_index]["id"] == task_id["id"]:
				tasks.pop(int(task_id["id"]))
				return "Task removed successfully"
		return "no changes made"
	except:
		return "Error Occurred"

if __name__ == '__main__':
	app.run(debug=True)


	
	

