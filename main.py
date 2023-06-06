
from fastapi import FastAPI

from db import open_db, close_db

app = FastAPI()


@app.post("/students")
def create_student(surname: str, id_group: int):
    """
    POST /students - создать нового студента.
    """
    cur = open_db()
    cur.execute(f"insert into students (surname, id_group) values ('{surname}',{id_group});")
    close_db(cur)
    return 'Пользователь добавлен.'


@app.get("/students/{student_id}")
def get_student(student_id: int):
    """
    GET /students/{student_id} - получить информацию о студенте по его id.
    """
    cur = open_db()
    cur.execute(f"select * from students where students.id = {student_id};")
    result = cur.fetchall()

    close_db(cur)
    return result


@app.put("/students/{student_id}")
def update_student(student_id: int, surname: str, id_group: int):
    """
    PUT /students/{student_id} - обновить информацию о студенте по его id.
    """
    cur = open_db()
    cur.execute(f"update students set surname = '{surname}', id_group = {id_group} where id = {student_id}")
    close_db(cur)
    return 'Пользователь обновлен.'


@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    """
    DELETE /students/{student_id} - удалить студента по его id.
    """
    cur = open_db()
    cur.execute(f"delete from students where id = {student_id}")
    close_db(cur)
    return 'Пользователь удален.'


@app.get("/teachers")
def get_teachers():
    """
    GET /teachers - получить список всех преподавателей.
    """
    cur = open_db()
    cur.execute(f"select * from teacher;")
    result = cur.fetchall()

    close_db(cur)
    return result


@app.post("/courses")
def create_student(name_course: str, id_teacher: int):
    """
    POST /courses - создать новый курс.
    """
    cur = open_db()
    cur.execute(f"insert into course (name_course, id_teacher) values ('{name_course}',{id_teacher});")
    close_db(cur)
    return 'Курс добавлен.'


@app.get("/courses/{course_id}")
def get_teachers(course_id: int):
    """
    GET /courses/{course_id} - получить информацию о курсе по его id.
    """
    cur = open_db()
    cur.execute(f"select * from course where id = {course_id};")
    result = cur.fetchall()

    close_db(cur)
    return result


@app.get("/courses/{course_id}/students")
def get_teachers(course_id: int):
    """
    GET /courses/{course_id}/students - получить список всех студентов на курсе.
    """
    cur = open_db()
    cur.execute(f"select students.surname from students"
                f" join group_s on students.id_group=group_s.id "
                f"join course on group_s.id_course=course.id "
                f"where course.id = '{course_id}';")
    result = cur.fetchall()

    close_db(cur)
    return result
