CREATE TABLE sms_attendance (
    attendance_id SERIAL PRIMARY KEY,
    student_id INT NOT NULL,
    class_id INT NOT NULL,
    section_id INT NOT NULL,
    attendance_status INT NOT NULL,
    attendance_date VARCHAR(255) NOT NULL
);


CREATE TABLE sms_classes (
    id SERIAL PRIMARY KEY,
    name VARCHAR(40) NOT NULL,
    section VARCHAR(255) NOT NULL,
    teacher_id INT NOT NULL
);

CREATE TABLE sms_section (
    section_id SERIAL PRIMARY KEY,
    section VARCHAR(255) NOT NULL
);


CREATE TABLE sms_students (
    id SERIAL PRIMARY KEY,
    name VARCHAR(40) NOT NULL,
    gender VARCHAR(40) NOT NULL,
    dob VARCHAR(255) NOT NULL,
    photo VARCHAR(40),
    mobile BIGINT NOT NULL,
    email VARCHAR(40),
    current_address VARCHAR(40),
    permanent_address VARCHAR(40),
    father_name VARCHAR(255) NOT NULL,
    father_mobile BIGINT NOT NULL,
    father_occupation VARCHAR(255) NOT NULL,
    mother_name VARCHAR(255) NOT NULL,
    mother_mobile BIGINT NOT NULL,
    admission_no INT NOT NULL,
    roll_no INT NOT NULL,
    class INT NOT NULL,
    section INT NOT NULL,
    stream INT,
    hostel INT,
    admission_date VARCHAR(255) NOT NULL,
    category INT,
    academic_year INT NOT NULL
);

CREATE TABLE sms_subjects (
    subject_id SERIAL PRIMARY KEY,
    subject VARCHAR(255) NOT NULL,
    type VARCHAR(255) NOT NULL,
    code INT NOT NULL
);


CREATE TABLE sms_teacher (
    teacher_id SERIAL PRIMARY KEY,
    teacher VARCHAR(255) NOT NULL,
    subject_id INT NOT NULL
);

CREATE TABLE sms_user (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(50) NOT NULL,
    gender VARCHAR(10) CHECK (gender IN ('male', 'female')),
    mobile VARCHAR(50) NOT NULL,
    designation VARCHAR(50) NOT NULL,
    image VARCHAR(250) NOT NULL,
    type VARCHAR(250) NOT NULL DEFAULT 'general',
    status VARCHAR(20) CHECK (status IN ('active', 'pending', 'deleted', '')) DEFAULT 'pending',
    authtoken VARCHAR(250) NOT NULL
);


INSERT INTO sms_attendance (student_id, class_id, section_id, attendance_status, attendance_date) VALUES
(6, 2, 1, 1, '2019/06/22'),
(5, 2, 1, 4, '2019/06/22'),
(3, 2, 1, 3, '2019/06/22'),
(7, 4, 4, 3, '2019/06/22'),
(6, 2, 1, 1, '2023/01/01'),
(6, 2, 1, 1, '2023/01/02'),
(5, 2, 1, 1, '2023/01/02'),
(3, 2, 1, 3, '2023/01/02');

INSERT INTO sms_classes (name, section, teacher_id) VALUES
('class1', '1', 1),
('class2', '4', 3),
('class3', '2', 2),
('vbvcncvn', '2', 1),
('sffsafas', '2', 2);

INSERT INTO sms_section (section) VALUES
('A'),
('B'),
('C'),
('dgdsgsdgsd bbb');

INSERT INTO sms_students (name, gender, dob, photo, mobile, email, current_address, permanent_address, father_name, father_mobile, father_occupation, mother_name, mother_mobile, admission_no, roll_no, class, section, stream, hostel, admission_date, category, academic_year) VALUES
('Smith', 'male', '0000-00-00', '1559480265cat-2083492_960_720.jpg', 123456789, 'smith@test.com', 'xyxz', NULL, 'jhone smith', 0, '', 'Diana smith', 0, 1234567, 654378, 2, 1, NULL, NULL, '0000-00-00', NULL, 2019),
('jaeeme khan', 'male', '22/06/1992', '1559480508phpzag.gif', 123456789, 'jaeeme@test.com', 'New delhi india', NULL, '', 0, '', '', 0, 12345678, 67891, 3, 2, NULL, NULL, '02/06/2019', NULL, 2019),
('Root', 'male', '22/06/1992', '1560685652password reset with php.png', 0, 'root@gmail.com', '', NULL, '', 0, '', '', 0, 123456789, 3532552, 2, 1, NULL, NULL, '02/06/2019', NULL, 2019);

INSERT INTO sms_subjects (subject, type, code) VALUES
('English', 'Theory', 210),
('Mathmatics', 'Theory', 220),
('Drawing', 'Practical', 230),
('szfsfasfasf mmm', 'Theory', 53534);

INSERT INTO sms_teacher (teacher, subject_id) VALUES
('Daniel', 1),
('George', 2),
('Mohan', 3),
('David', 0),
('sfsafas bbbb nn', 1);

INSERT INTO sms_user (first_name, last_name, email, password, gender, mobile, designation, image, type, status, authtoken) VALUES
('nazar', 'mohammed', 'nazarchess14@gmail.com', 'nazar123', 'male', '7483282896', 'Web developer', '', 'administrator', 'active', '');

SELECT * FROM sms_students;
SELECT * FROM sms_attendance;
SELECT * FROM sms_classes;
SELECT * FROM sms_teacher;