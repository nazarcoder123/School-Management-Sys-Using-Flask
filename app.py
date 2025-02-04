# from flask import Flask, render_template, request, redirect, url_for, session, jsonify
# import psycopg2
# from psycopg2 import sql
# from datetime import date
# from psycopg2 import extras
# import psycopg2.extras
# import logging
# from flask import flash

# app = Flask(__name__)

# # Configure logging
# logging.basicConfig(level=logging.INFO)

# app.secret_key = 'abcd21234455'  
# app.config['PG_HOST'] = 'localhost'
# app.config['PG_USER'] = 'postgres'
# app.config['PG_PASSWORD'] = 'Nazar123'
# app.config['PG_DB'] = 'python_sms'

# # Set up PostgreSQL connection
# def get_db_connection():
#     conn = psycopg2.connect(
#         host=app.config['PG_HOST'],
#         database=app.config['PG_DB'],
#         user=app.config['PG_USER'],
#         password=app.config['PG_PASSWORD']
#     )
#     return conn

# @app.route('/')
# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     message = ''
#     if request.method == 'POST' and 'email' in request.form and 'password' in request.form:
#         email = request.form['email']
#         password = request.form['password']
#         conn = get_db_connection()
#         cursor = conn.cursor()
#         cursor.execute('SELECT * FROM sms_user WHERE status = %s AND email = %s AND password = %s', ('active', email, password))
#         user = cursor.fetchone()
#         if user:
#             session['loggedin'] = True
#             session['userid'] = user[0]  # Assuming ID is the first column in sms_user
#             session['name'] = user[1]    # Assuming first_name is the second column
#             session['email'] = user[2]   # Assuming email is the third column
#             session['role'] = user[3]    # Assuming type is the fourth column
#             message = 'Logged in successfully!'
#             return redirect(url_for('dashboard'))
#         else:
#             message = 'Please enter correct email / password!'
#     return render_template('login.html', message=message)

# @app.route('/logout')
# def logout():
#     session.pop('loggedin', None)
#     session.pop('userid', None)
#     session.pop('email', None)
#     session.pop('name', None)
#     session.pop('role', None)
#     return redirect(url_for('login'))

# @app.route("/dashboard", methods=['GET', 'POST'])
# def dashboard():
#     if 'loggedin' in session:
#         return render_template("dashboard.html")
#     return redirect(url_for('login'))

# ########################### Teacher Section ###########################

# def get_db_connection():
#     conn = psycopg2.connect("dbname=python_sms user=postgres password=Nazar123 host=localhost")
#     return conn

# @app.route("/teacher", methods=['GET', 'POST'])
# def teacher():
#     if 'loggedin' in session:
#         conn = get_db_connection()
#         cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

#         cursor.execute('''
#             SELECT t.teacher_id, t.teacher, s.subject 
#             FROM sms_teacher t
#             LEFT JOIN sms_subjects s ON s.subject_id = t.subject_id
#         ''')
#         teachers = cursor.fetchall()

#         cursor.execute('SELECT * FROM sms_subjects')
#         subjects = cursor.fetchall()

#         cursor.close()
#         conn.close()
#         return render_template("teacher.html", teachers=teachers, subjects=subjects)
#     return redirect(url_for('login'))

# @app.route("/edit_teacher", methods=['GET'])
# def edit_teacher():
#     if 'loggedin' in session:
#         teacher_id = request.args.get('teacher_id')
#         if not teacher_id or not teacher_id.isdigit():
#             return redirect(url_for('teacher'))

#         conn = get_db_connection()
#         cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

#         cursor.execute('''
#             SELECT teacher_id, teacher, subject_id 
#             FROM sms_teacher 
#             WHERE teacher_id = %s
#         ''', (int(teacher_id),))
#         teacher = cursor.fetchone()

#         cursor.execute('SELECT * FROM sms_subjects')
#         subjects = cursor.fetchall()

#         cursor.close()
#         conn.close()

#         if teacher:
#             return render_template("edit_teacher.html", teacher=teacher, subjects=subjects)
#         return redirect(url_for('teacher'))
#     return redirect(url_for('login'))

# @app.route("/save_teacher", methods=['POST'])
# def save_teacher():
#     if 'loggedin' in session:
#         conn = get_db_connection()
#         cursor = conn.cursor()
#         try:
#             # Safely get and validate teacher_name
#             teacher_name = request.form.get('teacher_name')
#             if not teacher_name:
#                 return "Teacher name is required.", 400  # Return error if empty

#             specialization = request.form.get('specialization')
#             action = request.form.get('action', '')

#             # Convert specialization to integer or None
#             specialization = int(specialization) if specialization else None

#             if action == 'updateTeacher':
#                 teacher_id = request.form.get('teacherid')
#                 cursor.execute('''
#                     UPDATE sms_teacher 
#                     SET teacher = %s, subject_id = %s 
#                     WHERE teacher_id = %s
#                 ''', (teacher_name, specialization, teacher_id))
#             else:
#                 # Insert new teacher
#                 cursor.execute('''
#                     INSERT INTO sms_teacher (teacher, subject_id)
#                     VALUES (%s, %s)
#                 ''', (teacher_name, specialization))

#             conn.commit()
#         except Exception as e:
#             conn.rollback()
#             logging.error(f"Database error: {str(e)}", exc_info=True)
#             return f"Error: {str(e)}", 500
#         finally:
#             cursor.close()
#             conn.close()
#         return redirect(url_for('teacher'))
#     return redirect(url_for('login'))


# @app.route("/delete_teacher", methods=['GET'])
# def delete_teacher():
#     if 'loggedin' in session:
#         teacher_id = request.args.get('teacher_id')
#         if teacher_id and teacher_id.isdigit():
#             conn = get_db_connection()
#             cursor = conn.cursor()
#             cursor.execute('DELETE FROM sms_teacher WHERE teacher_id = %s', (teacher_id,))
#             conn.commit()
#             cursor.close()
#             conn.close()
#         return redirect(url_for('teacher'))
#     return redirect(url_for('login'))

# ########################### SUBJECT ##################################
    
# from psycopg2 import extras  # Add this import

# @app.route("/subject", methods=['GET', 'POST'])
# def subject():
#     if 'loggedin' in session:
#         conn = get_db_connection()
#         cursor = conn.cursor(cursor_factory=extras.DictCursor)  # Use DictCursor
#         cursor.execute('SELECT * FROM sms_subjects')
#         subjects = cursor.fetchall()
#         cursor.close()
#         conn.close()
#         print("Fetched Data:", subjects)  # Verify data in the terminal
#         return render_template("subject.html", subjects=subjects)
#     return redirect(url_for('login'))
    
    
# @app.route("/save_subject", methods=['GET', 'POST'])
# def save_subject():
#     if 'loggedin' in session:    
#         conn = get_db_connection()
#         cursor = conn.cursor()
        
#         if request.method == 'POST' and 'subject' in request.form and 's_type' in request.form and 'code' in request.form:
#             subject = request.form['subject'] 
#             s_type = request.form['s_type'] 
#             code = request.form['code']               
#             action = request.form['action']             
            
#             if action == 'updateSubject':
#                 subjectid = request.form['subjectid'] 
#                 # Update subject
#                 cursor.execute('UPDATE sms_subjects SET subject = %s, type = %s, code = %s WHERE subject_id = %s', 
#                                (subject, s_type, code, subjectid))
#                 conn.commit()        
#             else: 
#                 # Insert new subject
#                 cursor.execute('INSERT INTO sms_subjects (subject, type, code) VALUES (%s, %s, %s)', 
#                                (subject, s_type, code))
#                 conn.commit()        
#             # Close the cursor and connection after committing the changes
#             cursor.close()
#             conn.close()

#             return redirect(url_for('subject'))        
#         elif request.method == 'POST':
#             msg = 'Please fill out the form field!'        
#         return redirect(url_for('subject'))        
#     return redirect(url_for('login'))

# from psycopg2.extras import DictCursor  # Add this import

# @app.route("/edit_subject", methods=['GET'])
# def edit_subject():
#     if 'loggedin' in session:
#         subject_id = request.args.get('subject_id')
#         if not subject_id:
#             return "Subject ID is missing.", 400  # Handle missing ID
        
#         try:
#             conn = get_db_connection()
#             cursor = conn.cursor(cursor_factory=DictCursor)  # Use DictCursor
#             cursor.execute('''
#                 SELECT subject_id, subject, type, code 
#                 FROM sms_subjects 
#                 WHERE subject_id = %s
#             ''', (subject_id,))
#             subject = cursor.fetchone()  # Fetch SINGLE row
#             cursor.close()
#             conn.close()

#             if not subject:
#                 return "Subject not found.", 404  # Handle missing data

#             return render_template("edit_subject.html", subject=subject)
            
#         except Exception as e:
#             print("Database Error:", e)  # Log errors
#             return "An error occurred.", 500
            
#     return redirect(url_for('login'))
    
# @app.route("/delete_subject", methods=['GET'])
# def delete_subject():
#     if 'loggedin' in session:
#         subject_id = request.args.get('subject_id')
#         conn = get_db_connection()
#         cursor = conn.cursor()

#         # Delete the subject based on subject_id
#         cursor.execute('DELETE FROM sms_subjects WHERE subject_id = %s', (subject_id,))
#         conn.commit()

#         # Close the cursor and connection after the operation
#         cursor.close()
#         conn.close()

#         return redirect(url_for('subject'))
#     return redirect(url_for('login'))

# ################################ Classes  #######################################

# @app.route("/classes", methods=['GET', 'POST'])
# def classes():
#     if 'loggedin' in session:
#         conn = get_db_connection()
#         cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
      
        
#         cursor.execute('''
#                 SELECT c.id, c.name, s.section, t.teacher 
#                 FROM sms_classes c 
#                 LEFT JOIN sms_section s ON s.section_id = c.section::integer 
#                 LEFT JOIN sms_teacher t ON t.teacher_id = c.teacher_id
#         ''')
        
#         classes = cursor.fetchall()

#         # Get all sections
#         cursor.execute('SELECT * FROM sms_section')
#         sections = cursor.fetchall()

#         # Get all teachers
#         cursor.execute('SELECT * FROM sms_teacher')
#         teachers = cursor.fetchall()

#         # Close the cursor and connection after the operation
#         cursor.close()
#         conn.close()

#         return render_template("class.html", classes=classes, sections=sections, teachers=teachers)

#     return redirect(url_for('login'))


# @app.route("/edit_class", methods=['GET'])
# def edit_class():
#     if 'loggedin' in session:
#         class_id = request.args.get('class_id')  # Get the class_id from the URL query string

#         conn = get_db_connection()
#         cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

#         # Fetch class details based on class_id
#         cursor.execute('''SELECT c.id, c.name, s.section, t.teacher 
#                            FROM sms_classes c 
#                            LEFT JOIN sms_section s ON s.section_id = c.section 
#                            LEFT JOIN sms_teacher t ON t.teacher_id = c.teacher_id 
#                            WHERE c.id = %s''', (class_id,))
#         classes = cursor.fetchall()

#         # Get all sections
#         cursor.execute('SELECT * FROM sms_section')
#         sections = cursor.fetchall()

#         # Get all teachers
#         cursor.execute('SELECT * FROM sms_teacher')
#         teachers = cursor.fetchall()

#         # Close the cursor and connection after the operation
#         cursor.close()
#         conn.close()

#         return render_template("edit_class.html", classes=classes, sections=sections, teachers=teachers)

#     return redirect(url_for('login'))

# @app.route("/save_class", methods=['GET', 'POST'])
# def save_class():
#     if 'loggedin' in session:
#         if request.method == 'POST' and 'cname' in request.form:
#             cname = request.form['cname']
#             sectionid = request.form['sectionid']
#             teacherid = request.form['teacherid']
#             action = request.form['action']

#             conn = get_db_connection()
#             cursor = conn.cursor()

#             if action == 'updateClass':
#                 class_id = request.form['classid']
#                 cursor.execute('''UPDATE sms_classes 
#                                   SET name = %s, section = %s, teacher_id = %s 
#                                   WHERE id = %s''', (cname, sectionid, teacherid, class_id))
#                 conn.commit()
#             else:
#                 cursor.execute('''INSERT INTO sms_classes (name, section, teacher_id) 
#                                   VALUES (%s, %s, %s)''', (cname, sectionid, teacherid))
#                 conn.commit()

#             cursor.close()
#             conn.close()
#             return redirect(url_for('classes'))

#         elif request.method == 'POST':
#             msg = 'Please fill out the form field !'

#         return redirect(url_for('classes'))
    
#     return redirect(url_for('login'))
    

# @app.route("/delete_class", methods=['GET'])
# def delete_class():
#     if 'loggedin' in session:
#         class_id = request.args.get('class_id')
        
#         conn = get_db_connection()
#         cursor = conn.cursor()

#         cursor.execute('DELETE FROM sms_classes WHERE id = %s', (class_id,))
#         conn.commit()

#         cursor.close()
#         conn.close()
        
#         return redirect(url_for('classes'))
    
#     return redirect(url_for('login'))   

# ########################### SECTIONS ##################################

# @app.route("/sections", methods =['GET', 'POST'])
# def sections():
#     if 'loggedin' in session:
#         conn = get_db_connection()
#         # cursor = conn.cursor(dictionary=True)
#         cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        
#         cursor.execute('SELECT * FROM sms_section')
#         sections = cursor.fetchall()
        
#         cursor.close()
#         conn.close()
        
#         return render_template("sections.html", sections=sections)
    
#     return redirect(url_for('login'))

# @app.route("/edit_sections", methods =['GET'])
# def edit_sections():
#     if 'loggedin' in session:
#         section_id = request.args.get('section_id')
        
#         conn = get_db_connection()
#         cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
#         # cursor = conn.cursor(dictionary=True)
        
        
#         cursor.execute('SELECT * FROM sms_section WHERE section_id = %s', (section_id,))
#         sections = cursor.fetchall()
        
#         cursor.close()
#         conn.close()
        
#         return render_template("edit_section.html", sections=sections)
    
#     return redirect(url_for('login'))

# @app.route("/save_sections", methods =['GET', 'POST'])
# def save_sections():
#     if 'loggedin' in session:
#         conn = get_db_connection()
#         cursor = conn.cursor()
        
#         if request.method == 'POST' and 'section_name' in request.form:
#             section_name = request.form['section_name']
#             action = request.form['action']
            
#             if action == 'updateSection':
#                 section_id = request.form['sectionid']
#                 cursor.execute('UPDATE sms_section SET section = %s WHERE section_id = %s', (section_name, section_id))
#                 conn.commit()
#             else:
#                 cursor.execute('INSERT INTO sms_section (section) VALUES (%s)', (section_name,))
#                 conn.commit()
            
#             cursor.close()
#             conn.close()
            
#             return redirect(url_for('sections'))
        
#         elif request.method == 'POST':
#             msg = 'Please fill out the form field !'
        
#         return redirect(url_for('sections'))
    
#     return redirect(url_for('login'))

# @app.route("/delete_sections", methods =['GET'])
# def delete_sections():
#     if 'loggedin' in session:
#         section_id = request.args.get('section_id')
        
#         conn = get_db_connection()
#         cursor = conn.cursor()
        
#         cursor.execute('DELETE FROM sms_section WHERE section_id = %s', (section_id,))
#         conn.commit()
        
#         cursor.close()
#         conn.close()
        
#         return redirect(url_for('sections'))
    
#     return redirect(url_for('login')) 

# ########################### STUDENTS ##################################
    
# @app.route("/student", methods =['GET', 'POST'])
# def student():
#     if 'loggedin' in session:
#         conn = get_db_connection()
#         # cursor = conn.cursor(dictionary=True) 
#         cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)  
        
#         cursor.execute('SELECT s.id, s.admission_no, s.roll_no, s.name, s.photo, c.name AS class, sec.section '
#                        'FROM sms_students s '
#                        'LEFT JOIN sms_section sec ON sec.section_id = s.section '
#                        'LEFT JOIN sms_classes c ON c.id = s.class')
#         students = cursor.fetchall()
        
#         cursor.execute('SELECT * FROM sms_classes')
#         classes = cursor.fetchall()
        
#         cursor.execute('SELECT * FROM sms_section')
#         sections = cursor.fetchall()
        
#         cursor.close()
#         conn.close()
        
#         return render_template("student.html", students=students, classes=classes, sections=sections)
    
#     return redirect(url_for('login'))

# @app.route("/edit_student", methods =['GET'])
# def edit_student():
#     if 'loggedin' in session:
#         student_id = request.args.get('student_id')
        
#         conn = get_db_connection()
#         cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        
#         cursor.execute('SELECT s.id, s.admission_no, s.roll_no, s.name, s.photo, c.name AS class, sec.section '
#                        'FROM sms_students s '
#                        'LEFT JOIN sms_section sec ON sec.section_id = s.section '
#                        'LEFT JOIN sms_classes c ON c.id = s.class '
#                        'WHERE s.id = %s', (student_id,))    
        
#         students = cursor.fetchall()
        
#         cursor.execute('SELECT * FROM sms_classes')
#         classes = cursor.fetchall()
        
#         cursor.execute('SELECT * FROM sms_section')
#         sections = cursor.fetchall()
        
#         cursor.close()
#         conn.close()
        
#         return render_template("edit_student.html", students=students, classes=classes, sections=sections)
    
#     return redirect(url_for('login'))


# @app.route("/save_student", methods=['GET', 'POST'])
# def save_student():
#     if 'loggedin' in session:
#         if request.method == 'POST':
#             try:
#                 # Extract form data
#                 student_id = request.form.get('studentid')
#                 register_no = request.form.get('registerNo')[:40]  
#                 roll_no = request.form.get('rollNo')
#                 year = request.form.get('year')
#                 admission_date = request.form.get('admission_date')
#                 class_id = request.form.get('classid')
#                 section_id = request.form.get('sectionid')
#                 sname = request.form.get('sname')[:40]  
#                 gender = request.form.get('gender')
#                 dob = request.form.get('dob')
#                 email = request.form.get('email')[:255]  
#                 mobile = request.form.get('mobile')
#                 address = request.form.get('address')[:255]  
#                 fname = request.form.get('fname')[:40]
#                 mname = request.form.get('mname')[:40]

#                 # Handle photo upload
#                 photo = request.files.get('photo')
#                 photo_filename = photo.filename if photo else None
#                 if photo_filename and len(photo_filename) > 40:
#                     photo_filename = photo_filename[:40]  

#                 conn = get_db_connection()
#                 cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

#                 # Update query
#                 update_query = """
#                     UPDATE sms_students 
#                     SET admission_no = %s,
#                         roll_no = %s,
#                         name = %s,
#                         class = %s,
#                         section = %s,
#                         photo = %s,
#                         gender = %s,
#                         dob = %s,
#                         email = %s,
#                         mobile = %s,
#                         student_address = %s,
#                         admission_date = %s
#                     WHERE id = %s
#                 """
#                 cursor.execute(update_query, (
#                     register_no, roll_no, sname, class_id, section_id,
#                     photo_filename, gender, dob, email, mobile,
#                     address, admission_date, student_id
#                 ))
#                 conn.commit()
#                 flash('Student updated successfully!', 'success')

#             except Exception as e:
#                 conn.rollback()
#                 flash(f'Error updating student: {str(e)}', 'danger')
#                 return redirect(url_for('edit_student', student_id=student_id))

#             finally:
#                 cursor.close()
#                 conn.close()

#             # return redirect(url_for('students'))
#             return redirect(url_for('student'))

#         else:
#             flash('Invalid request method!', 'danger')
#             # return redirect(url_for('students'))
#             return redirect(url_for('student'))

#     return redirect(url_for('login'))




# @app.route("/delete_student", methods =['GET'])
# def delete_student():
#     if 'loggedin' in session:
#         student_id = request.args.get('student_id')
        
#         conn = get_db_connection()
#         cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        
#         cursor.execute('DELETE FROM sms_students WHERE id = %s', (student_id,))
#         conn.commit()
        
#         cursor.close()
#         conn.close()
        
#         return redirect(url_for('student'))
    
#     return redirect(url_for('login'))

# @app.route("/attendance", methods =['GET', 'POST'])
# def attendance():
#     if 'loggedin' in session:
#         conn = get_db_connection()
#         cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
#         # cursor = conn.cursor(dictionary=True)
        
#         cursor.execute('SELECT * FROM sms_classes')
#         classes = cursor.fetchall()
        
#         cursor.execute('SELECT * FROM sms_section')
#         sections = cursor.fetchall()
        
#         cursor.close()
#         conn.close()
        
#         return render_template("attendance.html", classes=classes, sections=sections)
    
#     return redirect(url_for('login'))

# @app.route("/getClassAttendance", methods =['GET', 'POST'])
# def getClassAttendance():
#     if 'loggedin' in session:
#         if request.method == 'POST' and 'classid' in request.form and 'sectionid' in request.form:
#             classid = request.form['classid']
#             sectionid = request.form['sectionid']
            
#             conn = get_db_connection()
#             cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
#             # cursor = conn.cursor(dictionary=True)
            
#             cursor.execute('SELECT * FROM sms_classes')
#             classes = cursor.fetchall()
            
#             cursor.execute('SELECT * FROM sms_section')
#             sections = cursor.fetchall()
            
#             currentDate = date.today().strftime('%Y/%m/%d')
            
#             cursor.execute('SELECT s.id, s.name, s.photo, s.gender, s.dob, s.mobile, s.email, s.current_address, '
#                            's.father_name, s.mother_name, s.admission_no, s.roll_no, s.admission_date, '
#                            's.academic_year, a.attendance_status, a.attendance_date '
#                            'FROM sms_students AS s '
#                            'LEFT JOIN sms_attendance AS a ON s.id = a.student_id '
#                            'WHERE s.class = %s AND s.section = %s', (classid, sectionid))
#             students = cursor.fetchall()
            
#             cursor.close()
#             conn.close()
            
#             return render_template("attendance.html", classes=classes, sections=sections, students=students, 
#                                    classId=classid, sectionId=sectionid)
        
#         elif request.method == 'POST':
#             msg = 'Please fill out the form field !'
        
#         return redirect(url_for('attendance'))
    
#     return redirect(url_for('login'))

# @app.route("/report", methods =['GET', 'POST'])
# def report():
#     if 'loggedin' in session:
#         conn = get_db_connection()
#         cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
#         # cursor = conn.cursor(dictionary=True)
        
#         cursor.execute('SELECT * FROM sms_classes')
#         classes = cursor.fetchall()
        
#         cursor.execute('SELECT * FROM sms_section')
#         sections = cursor.fetchall()
        
#         cursor.close()
#         conn.close()
        
#         return render_template("report.html", classes=classes, sections=sections)
    
#     return redirect(url_for('login'))

# if __name__ == "__main__":
#     app.run(debug=True)    