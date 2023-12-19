CREATE DATABASE hospital_portal;
USE hospital_portal;

CREATE TABLE patients (
	patient_id int not null unique auto_increment primary key,
    patient_name varchar(45) NOT NULL,
    age int not null,
    admission_date date,
    discharge_date date
    );
    

CREATE TABLE Appointments (
	appointment_id int not null unique auto_increment primary key,
    patient_id int not null,
    doctor_id int not null,
    appointment_date date not null,
    appointment_time decimal not null,
    foreign key (patient_id) references patients(patient_id)
    );
    
INSERT INTO patients (patient_name, age, admission_date, discharge_date)
VALUES ("Maria Jozef", 67, "2023/10/01", "2023/10/07"),
	   ("Breanna Olsen", 35, "2023/06/25", "2023/06/29"),
       ("Henry Smith", 55, "2023/09/17", "2023/09/25");
       
SELECT * FROM patients;

CREATE TABLE doctors (
	doctor_id int not null unique auto_increment primary key,
    doctor_name varchar(45) NOT NULL,
    doctor_field varchar(45) NOT NULL
    );

ALTER TABLE appointments
ADD FOREIGN KEY (doctor_id) REFERENCES doctors(doctor_id);    

DELIMITER //

CREATE PROCEDURE ScheduleAppointment (
	IN app_patient_id INT,
    IN p_doctor_id INT,
    IN p_appointment_date DATE,
    IN p_appointment_time DECIMAL(5, 2)
    )
    
BEGIN
	INSERT INTO Appointments (patient_id, doctor_id, appointment_date, appointment_time)
    VALUES (app_patient_id, app_doctor_id, app_appointment_date, app_appointment_time);
    
END //

DELIMITER ;


DELIMITER //

CREATE PROCEDURE DischargePatient (
	IN app_patient_id INT
    )
BEGIN
	UPDATE patients
    SET discharge_date = CURRENT_DATE()
    WHERE patient_id = app_patient_id;

END //

DELIMITER ;

INSERT INTO doctors (doctor_name, doctor_field)
VALUES ("Steven Strange", "Neural Surgeon"),
	   ("Wanda Maximoff", "Pediatrics"),
       ("Vladimir Tepes", "Cardiology");
       
CREATE VIEW AppointmentView AS
SELECT
    A.appointment_id,
    A.appointment_date,
    A.appointment_time,
    P.patient_id,
    P.patient_name,
    P.age,
    P.admission_date,
    P.discharge_date,
    D.doctor_id,
    D.doctor_name,
    D.doctor_field
FROM
    Appointments A
JOIN
    Patients P ON A.patient_id = P.patient_id
JOIN
    Doctors D ON A.doctor_id = D.doctor_id;
    
    CALL ScheduleAppointment(2, 3, '2023-12-20', 16.30);
    
    DROP PROCEDURE ScheduleAppointment;

DELIMITER //

CREATE PROCEDURE ScheduleAppointment (
	IN app_patient_id INT,
    IN app_doctor_id INT,
    IN app_appointment_date DATE,
    IN app_appointment_time DECIMAL(5, 2)
    )
    
BEGIN
	INSERT INTO Appointments (patient_id, doctor_id, appointment_date, appointment_time)
    VALUES (app_patient_id, app_doctor_id, app_appointment_date, app_appointment_time);
    
END //

DELIMITER ;

CALL ScheduleAppointment(2, 3, '2023-12-20', 16.30);

SELECT * FROM AppointmentView;

CALL DischargePatient(2);

SELECT * FROM AppointmentView;

SELECT * FROM patients;

CALL ScheduleAppointment(2, 3, '2023-12-20', 0830);

SELECT * FROM AppointmentView;

SELECT * FROM patients;

SELECT * FROM AppointmentView;

SELECT * FROM AppointmentView;

ALTER TABLE appointments MODIFY appointment_time DECIMAL;

ALTER TABLE appointments MODIFY appointment_time DECIMAL;

SELECT * FROM AppointmentView;

ALTER TABLE appointments DROP COLUMN appointment_time; 

ALTER TABLE appointments ADD appointment_time DECIMAL(5,2);

SELECT * FROM AppointmentView;

DELETE FROM appointments;

DELETE FROM appointments WHERE patient_id > 0;

SELECT * FROM AppointmentView;

SELECT * FROM appointments;

CALL DischargePatient(4);

SELECT * FROM recordsview;

DELIMITER //

CREATE PROCEDURE UpdatePatient(
    IN p_patient_id INT,
    IN p_patient_name VARCHAR(45),
    IN p_age INT,
    IN p_admission_date DATE,
    IN p_discharge_date DATE
)
BEGIN
    UPDATE patients
    SET
        patient_name = p_patient_name,
        age = p_age,
        admission_date = p_admission_date,
        discharge_date = p_discharge_date
    WHERE patient_id = p_patient_id;
END //

DELIMITER ;


