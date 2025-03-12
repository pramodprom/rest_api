from flask import Flask, jsonify, render_template


todo = Flask(__name__)

students = [
    {
        'id': 1,
        'name': 'tiger',
        'age': 10
    },
    {
        'id': 2,
        'name': 'tiger',
        'age': 10
    }
]
@todo.route('/students-list')
def get_students_list():
    # return render_template('index.html', con=students)
    return jsonify(students)

@todo.route('/student/get/<int:id>')
def get_student_by_id(id):
    print(id)
    for std in students:
        if std['id'] == id:
            return jsonify(std)
        print(std)
    return jsonify('not found')

if __name__ == '__main__':
    todo.run(
        host='127.0.0.1',
        port=5010,
        debug=True
    )