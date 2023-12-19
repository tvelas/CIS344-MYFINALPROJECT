from http.server import HTTPServer, BaseHTTPRequestHandler
from os import curdir, sep
from portalDatabase import Database
import cgi

class HospitalPortalHandler(BaseHTTPRequestHandler):
    
    def __init__(self, *args):
        self.database = Database()
        BaseHTTPRequestHandler.__init__(self, *args)
    
    def do_POST(self):
        try:
            if self.path == '/addPatient':
                self.send_response(200)
                self.send_header('Content-type','text/html')
                self.end_headers()
                form = cgi.FieldStorage(
                    fp=self.rfile,
                    headers=self.headers,
                    environ={'REQUEST_METHOD': 'POST'}
                )

                patient_name = form.getvalue("patient_name")
                age = int(form.getvalue("patient_age"))
                admission_date = form.getvalue("admission_date")
                discharge_date = form.getvalue("discharge_date")
                
                self.database.addPatient(patient_name, age, admission_date,discharge_date)

                print("Patient added:", patient_name, age, admission_date)
                
                self.wfile.write(b"<html><head><title> Hospital Portal </title></head>")
                self.wfile.write(b"<body>")
                self.wfile.write(b"<center><h1>Hospital Portal</h1>")
                self.wfile.write(b"<hr>")
                self.wfile.write(b"<div> <a href='/'>Home</a>| \
                                 <a href='/addPatient'>Add Patient</a>|\
                                  <a href='/scheduleAppointment'>Schedule Appointment</a>|\
                                  <a href='/viewAppointments'>View Appointments</a>|\
                                  <a href='/viewAllDoctors'>Doctors</a>|\
                                  <a href='/viewRecords'>Records</a>|\
                                  <a href='/updatePatient'>Update Patients</a>|\
                                  <a href='/dischargePatient'>Discharge Patient</a></div>")
                self.wfile.write(b"<hr>")
                self.wfile.write(b"<h3>Patient has been added</h3>")
                self.wfile.write(b"<div><a href='/addPatient'>Add Another Patient</a></div>")
                self.wfile.write(b"</center></body></html>")
        
        except IOError:
            self.send_error(404,'File Not Found: %s' % self.path)
        
        
        try:
            if self.path == '/scheduleAppointment':
                self.send_response(200)
                self.send_header('Content-type','text/html')
                self.end_headers()
                form = cgi.FieldStorage(
                    fp=self.rfile,
                    headers=self.headers,
                    environ={'REQUEST_METHOD': 'POST'}
                )

                patient_id = int(form.getvalue("patient_id"))
                doctor_id = int(form.getvalue("doctor_id"))
                appointment_date = form.getvalue("appointment_date")
                appointment_time = form.getvalue("appointment_time")
        
                self.database.scheduleAppointment(patient_id, doctor_id, appointment_date, appointment_time)

                print("Appointment made:", patient_id, doctor_id, appointment_date, appointment_time)
                
                self.wfile.write(b"<html><head><title> Hospital Portal </title></head>")
                self.wfile.write(b"<body>")
                self.wfile.write(b"<center><h1>Hospital Portal</h1>")
                self.wfile.write(b"<hr>")
                self.wfile.write(b"<div> <a href='/'>Home</a>| \
                                 <a href='/addPatient'>Add Patient</a>|\
                                  <a href='/scheduleAppointment'>Schedule Appointment</a>|\
                                  <a href='/viewAppointments'>View Appointments</a>|\
                                  <a href='/viewAllDoctors'>Doctors</a>|\
                                  <a href='/viewRecords'>Records</a>|\
                                  <a href='/updatePatient'>Update Patients</a>|\
                                  <a href='/dischargePatient'>Discharge Patient</a></div>")
                self.wfile.write(b"<hr>")
                self.wfile.write(b"<h3>Appointment has been made</h3>")
                self.wfile.write(b"<div><a href='/scheduleAppointment'>Make Another Appointment</a></div>")
                self.wfile.write(b"</center></body></html>")
                
        except IOError:
            self.send_error(404,'File Not Found: %s' % self.path)



        try:
            if self.path == '/dischargePatient':
                self.send_response(200)
                self.send_header('Content-type','text/html')
                self.end_headers()
                form = cgi.FieldStorage(
                    fp=self.rfile,
                    headers=self.headers,
                    environ={'REQUEST_METHOD': 'POST'}
                )

                patient_id = int(form.getvalue("patient_id"))
                
                
                self.database.dischargePatient((patient_id,))

                print("Patient Discharged:", patient_id)
                
                self.wfile.write(b"<html><head><title> Hospital Portal </title></head>")
                self.wfile.write(b"<body>")
                self.wfile.write(b"<center><h1>Hospital Portal</h1>")
                self.wfile.write(b"<hr>")
                self.wfile.write(b"<div> <a href='/'>Home</a>| \
                                 <a href='/addPatient'>Add Patient</a>|\
                                  <a href='/scheduleAppointment'>Schedule Appointment</a>|\
                                  <a href='/viewAppointments'>View Appointments</a>|\
                                  <a href='/viewAllDoctors'>Doctors</a>|\
                                  <a href='/viewRecords'>Records</a>|\
                                  <a href='/updatePatient'>Update Patients</a>|\
                                  <a href='/dischargePatient'>Discharge Patient</a></div>")
                self.wfile.write(b"<hr>")
                self.wfile.write(b"<h3>Patient has been discharged</h3>")
                self.wfile.write(b"<div><a href='/dischargePatient'>Discharge Another Patient</a></div>")
                self.wfile.write(b"</center></body></html>")
                
        except IOError:
            self.send_error(404,'File Not Found: %s' % self.path)




        #Update Patient code start
        
        try:
            if self.path == '/updatePatient':         
                self.send_response(200)
                self.send_header('Content-type','text/html')
                self.end_headers()
                form = cgi.FieldStorage(
                    fp=self.rfile,
                    headers=self.headers,
                    environ={'REQUEST_METHOD': 'POST'}
                )

                patient_id = int(form.getvalue("patient_id"))
                patient_name = form.getvalue("patient_name")
                age = int(form.getvalue("patient_age"))
                admission_date = form.getvalue("admission_date")
                discharge_date = form.getvalue("discharge_date")

                self.database.updatePatient(patient_id, patient_name, age, admission_date, discharge_date)

                self.wfile.write(b"<html><head><title> Hospital's Portal </title></head>")
                self.wfile.write(b"<body>")
                self.wfile.write(b"<center><h1>Hospital's Portal</h1>")
                self.wfile.write(b"<hr>")
                self.wfile.write(b"<div> <a href='/'>Home</a>| \
                                 <a href='/addPatient'>Add Patient</a>|\
                                  <a href='/scheduleAppointment'>Schedule Appointment</a>|\
                                  <a href='/viewAppointments'>View Appointments</a>|\
                                  <a href='/viewAllDoctors'>Doctors</a>|\
                                  <a href='/viewRecords'>Records</a>|\
                                  <a href='/updatePatient'>Update Patients</a>|\
                                  <a href='/dischargePatient'>Discharge Patient</a></div>")
                self.wfile.write(b"<hr>")
                self.wfile.write(b"<h3>Patient information updated</h3>")
                self.wfile.write(b"<div><a href='/updatePatient'>Update Another Patient</a></div>")
                self.wfile.write(b"</center></body></html>")

        except IOError:
            self.send_error(404, 'File Not Found: %s' % self.path)
        
        
        #Update Patient code ends

        return


###testing beings

    

###Testing Ends


    
    
    def do_GET(self):
        
        try:
            if self.path == '/':
                data=[]
                records = self.database.getAllPatients()
                print(records)
                data=records
                self.send_response(200)
                self.send_header('Content-type','text/html')
                self.end_headers()
                self.wfile.write(b"<html><head><title> Hospital's Portal </title></head>")
                self.wfile.write(b"<body>")
                self.wfile.write(b"<center><h1>Hospital's Portal</h1>")
                self.wfile.write(b"<hr>")
                self.wfile.write(b"<div> <a href='/'>Home</a>| \
                                 <a href='/addPatient'>Add Patient</a>|\
                                  <a href='/scheduleAppointment'>Schedule Appointment</a>|\
                                  <a href='/viewAppointments'>View Appointments</a>|\
                                  <a href='/viewAllDoctors'>Doctors</a>|\
                                  <a href='/viewRecords'>Records</a>|\
                                  <a href='/updatePatient'>Update Patients</a>|\
                                  <a href='/dischargePatient'>Discharge Patient</a></div>")
                self.wfile.write(b"<hr><h2>All Patients</h2>")
                self.wfile.write(b"<table border=2> \
                                    <tr><th> Patient ID </th>\
                                        <th> Patient Name</th>\
                                        <th> Age </th>\
                                        <th> Admission Date </th>\
                                        <th> Discharge Date </th></tr>")
                for row in data:
                    self.wfile.write(b' <tr> <td>')
                    self.wfile.write(str(row[0]).encode())
                    self.wfile.write(b'</td><td>')
                    self.wfile.write(str(row[1]).encode())
                    self.wfile.write(b'</td><td>')
                    self.wfile.write(str(row[2]).encode())
                    self.wfile.write(b'</td><td>')
                    self.wfile.write(str(row[3]).encode())
                    self.wfile.write(b'</td><td>')
                    self.wfile.write(str(row[4]).encode())
                    self.wfile.write(b'</td></tr>')
                
                self.wfile.write(b"</table></center>")
                self.wfile.write(b"</body></html>")
                return
            
            if self.path == '/addPatient':
                self.send_response(200)
                self.send_header('Content-type','text/html')
                self.end_headers()
                self.wfile.write(b"<html><head><title> Hospital's Portal </title></head>")
                self.wfile.write(b"<body>")
                self.wfile.write(b"<center><h1>Hospital's Portal</h1>")
                self.wfile.write(b"<hr>")
                self.wfile.write(b"<div> <a href='/'>Home</a>| \
                                 <a href='/addPatient'>Add Patient</a>|\
                                  <a href='/scheduleAppointment'>Schedule Appointment</a>|\
                                  <a href='/viewAppointments'>View Appointments</a>|\
                                  <a href='/viewAllDoctors'>Doctors</a>|\
                                  <a href='/viewRecords'>Records</a>|\
                                  <a href='/updatePatient'>Update Patients</a>|\
                                  <a href='/dischargePatient'>Discharge Patient</a></div>")
                self.wfile.write(b"<hr><h2>Add New Patient</h2>")

                self.wfile.write(b"<form action='/addPatient' method='post'>")
                self.wfile.write(b'<label for="patient_name">Patient Name:</label>\
                      <input type="text" id="patient_name" name="patient_name"/><br><br>\
                      <label for="patient_age">Age:</label>\
                      <input type="number" id="patient_age" name="patient_age"><br><br>\
                      <label for="admission_date">Admission Date:</label>\
                      <input type="date"id="admission_date" name="admission_date"><br><br>\
                      <label for="discharge_date">Discharge Date:</label>\
                      <input type="date"id="discharge_date" name="discharge_date"><br><br>\
                      <input type="submit" value="Submit">\
                      </form>')
                
                self.wfile.write(b"</center></body></html>")
                return
            
            if self.path == '/scheduleAppointment':
                self.send_response(200)
                self.send_header('Content-type','text/html')
                self.end_headers()
                self.wfile.write(b"<html><head><title> Hospital's Portal </title></head>")
                self.wfile.write(b"<body>")
                self.wfile.write(b"<center><h1>Hospital's Portal</h1>")
                self.wfile.write(b"<hr>")
                self.wfile.write(b"<div> <a href='/'>Home</a>| \
                                 <a href='/addPatient'>Add Patient</a>|\
                                  <a href='/scheduleAppointment'>Schedule Appointment</a>|\
                                  <a href='/viewAppointments'>View Appointments</a>|\
                                  <a href='/viewAllDoctors'>Doctors</a>|\
                                  <a href='/viewRecords'>Records</a>|\
                                  <a href='/updatePatient'>Update Patients</a>|\
                                  <a href='/dischargePatient'>Discharge Patient</a></div>")
                self.wfile.write(b"<hr><h2>Schedule Appointiment</h2>")

                #Start of implemented code
                
                self.wfile.write(b"<form action='/scheduleAppointment' method='post'>")
                self.wfile.write(b'<label for="patient_id">Patient ID:</label>\
                      <input type="number" id="patient_id" name="patient_id"/><br><br>\
                      <label for="doctor_id">Doctor ID:</label>\
                      <input type="number" id="doctor_id" name="doctor_id"><br><br>\
                      <label for="appointment_date">Appointment Date:</label>\
                      <input type="date"id="appointment_date" name="appointment_date"><br><br>\
                      <label for="appointment_time">Appointment Time:</label>\
                      <input type="decimal"id="appointment_time" name="appointment_time"><br><br>\
                      <input type="submit" value="Submit">\
                      </form>')
                      
                #End of implemented code
                
                self.wfile.write(b"</center></body></html>")
                return

            
            if self.path == '/viewAppointments':
                data=[]
                records = self.database.viewAppointments()
                print(records)
                data=records
                self.send_response(200)
                self.send_header('Content-type','text/html')
                self.end_headers()
                self.wfile.write(b"<html><head><title> Hospital's Portal </title></head>")
                self.wfile.write(b"<body>")
                self.wfile.write(b"<center><h1>Hospital's Portal</h1>")
                self.wfile.write(b"<hr>")
                self.wfile.write(b"<div> <a href='/'>Home</a>| \
                                 <a href='/addPatient'>Add Patient</a>|\
                                  <a href='/scheduleAppointment'>Schedule Appointment</a>|\
                                  <a href='/viewAppointments'>View Appointments</a>|\
                                  <a href='/viewAllDoctors'>Doctors</a>|\
                                  <a href='/viewRecords'>Records</a>|\
                                  <a href='/updatePatient'>Update Patients</a>|\
                                  <a href='/dischargePatient'>Discharge Patient</a></div>")
                self.wfile.write(b"<hr><h2>View Appointments</h2>")

                #Add Code Code Here
                
                self.wfile.write(b"<table border=2> \
                                    <tr><th> Appointment ID </th>\
                                        <th> Patient ID </th>\
                                        <th> Doctor ID </th>\
                                        <th> Appointment Date</th>\
                                        <th> Appointmnet Time </th</tr>")
                                        
                for row in data:
                    self.wfile.write(b' <tr> <td>')
                    self.wfile.write(str(row[0]).encode())
                    self.wfile.write(b'</td><td>')
                    self.wfile.write(str(row[1]).encode())
                    self.wfile.write(b'</td><td>')
                    self.wfile.write(str(row[2]).encode())
                    self.wfile.write(b'</td><td>')
                    self.wfile.write(str(row[3]).encode())
                    self.wfile.write(b'</td><td>')
                    self.wfile.write(str(row[4]).encode())
                    self.wfile.write(b'</td></tr>')
                
                #End code here
                self.wfile.write(b"</center></body></html>")
                return


            #View Doctors code
            if self.path == '/viewAllDoctors':
                data=[]
                records = self.database.viewAllDoctors()
                print(records)
                data=records
                self.send_response(200)
                self.send_header('Content-type','text/html')
                self.end_headers()
                self.wfile.write(b"<html><head><title> Hospital's Portal </title></head>")
                self.wfile.write(b"<body>")
                self.wfile.write(b"<center><h1>Hospital's Portal</h1>")
                self.wfile.write(b"<hr>")
                self.wfile.write(b"<div> <a href='/'>Home</a>| \
                                 <a href='/addPatient'>Add Patient</a>|\
                                  <a href='/scheduleAppointment'>Schedule Appointment</a>|\
                                  <a href='/viewAppointments'>View Appointments</a>|\
                                  <a href='/viewAllDoctors'>Doctors</a>|\
                                  <a href='/viewRecords'>Records</a>|\
                                  <a href='/updatePatient'>Update Patients</a>|\
                                  <a href='/dischargePatient'>Discharge Patient</a></div>")
                self.wfile.write(b"<hr><h2>All Doctors</h2>")

                
                self.wfile.write(b"<table border=2> \
                                    <tr><th> Doctor ID </th>\
                                        <th> Doctor Name </th>\
                                        <th> Medical Field </th</tr>")
                                        
                for row in data:
                    self.wfile.write(b' <tr> <td>')
                    self.wfile.write(str(row[0]).encode())
                    self.wfile.write(b'</td><td>')
                    self.wfile.write(str(row[1]).encode())
                    self.wfile.write(b'</td><td>')
                    self.wfile.write(str(row[2]).encode())
                    self.wfile.write(b'</td></tr>')
                
                self.wfile.write(b"</center></body></html>")
                return
            #End of view doctors


            #View Records
            if self.path == '/viewRecords':
                data=[]
                records = self.database.viewRecords()
                print(records)
                data=records
                self.send_response(200)
                self.send_header('Content-type','text/html')
                self.end_headers()
                self.wfile.write(b"<html><head><title> Hospital's Portal </title></head>")
                self.wfile.write(b"<body>")
                self.wfile.write(b"<center><h1>Hospital's Portal</h1>")
                self.wfile.write(b"<hr>")
                self.wfile.write(b"<div> <a href='/'>Home</a>| \
                                 <a href='/addPatient'>Add Patient</a>|\
                                  <a href='/scheduleAppointment'>Schedule Appointment</a>|\
                                  <a href='/viewAppointments'>View Appointments</a>|\
                                  <a href='/viewAllDoctors'>Doctors</a>|\
                                  <a href='/viewRecords'>Records</a>|\
                                  <a href='/updatePatient'>Update Patients</a>|\
                                  <a href='/dischargePatient'>Discharge Patient</a></div>")
                self.wfile.write(b"<hr><h2>Records</h2>")

                
                self.wfile.write(b"<table border=2> \
                                    <tr><th> Appointment ID </th>\
                                        <th> Appointment Date </th>\
                                        <th> Appointment Time </th>\
                                        <th> Patient ID </th>\
                                        <th> Patient Name </th>\
                                        <th> Age </th>\
                                        <th> Admission Date </th>\
                                        <th> Discharge Date </th>\
                                        <th> Doctor ID </th>\
                                        <th> Doctor Name </th>\
                                        <th> Medical Field </th</tr>")
                                        
                for row in data:
                    self.wfile.write(b' <tr> <td>')
                    self.wfile.write(str(row[0]).encode())
                    self.wfile.write(b'</td><td>')
                    self.wfile.write(str(row[1]).encode())
                    self.wfile.write(b'</td><td>')
                    self.wfile.write(str(row[2]).encode())
                    self.wfile.write(b'</td><td>')
                    self.wfile.write(str(row[3]).encode())
                    self.wfile.write(b'</td><td>')
                    self.wfile.write(str(row[4]).encode())
                    self.wfile.write(b'</td><td>')
                    self.wfile.write(str(row[5]).encode())
                    self.wfile.write(b'</td><td>')
                    self.wfile.write(str(row[6]).encode())
                    self.wfile.write(b'</td><td>')
                    self.wfile.write(str(row[7]).encode())
                    self.wfile.write(b'</td><td>')
                    self.wfile.write(str(row[8]).encode())
                    self.wfile.write(b'</td><td>')
                    self.wfile.write(str(row[9]).encode())
                    self.wfile.write(b'</td><td>')
                    self.wfile.write(str(row[10]).encode())
                    self.wfile.write(b'</td></tr>')
                
                
                self.wfile.write(b"</center></body></html>")
                return
            #End of view records




            #Start Update Patient

            if self.path == '/updatePatient':
                data=[]
                records = self.database.getAllPatients()
                print(records)
                data=records
                self.send_response(200)
                self.send_header('Content-type','text/html')
                self.end_headers()
                self.wfile.write(b"<html><head><title> Hospital's Portal </title></head>")
                self.wfile.write(b"<body>")
                self.wfile.write(b"<center><h1>Hospital's Portal</h1>")
                self.wfile.write(b"<hr>")
                self.wfile.write(b"<div> <a href='/'>Home</a>| \
                                 <a href='/addPatient'>Add Patient</a>|\
                                  <a href='/scheduleAppointment'>Schedule Appointment</a>|\
                                  <a href='/viewAppointments'>View Appointments</a>|\
                                  <a href='/viewAllDoctors'>Doctors</a>|\
                                  <a href='/viewRecords'>Records</a>|\
                                  <a href='/updatePatient'>Update Patients</a>|\
                                  <a href='/dischargePatient'>Discharge Patient</a></div>")

                self.wfile.write(b"<table border=2> \
                                    <tr><th> Patient ID </th>\
                                        <th> Patient Name</th>\
                                        <th> Age </th>\
                                        <th> Admission Date </th>\
                                        <th> Discharge Date </th></tr>")
                for row in data:
                    self.wfile.write(b' <tr> <td>')
                    self.wfile.write(str(row[0]).encode())
                    self.wfile.write(b'</td><td>')
                    self.wfile.write(str(row[1]).encode())
                    self.wfile.write(b'</td><td>')
                    self.wfile.write(str(row[2]).encode())
                    self.wfile.write(b'</td><td>')
                    self.wfile.write(str(row[3]).encode())
                    self.wfile.write(b'</td><td>')
                    self.wfile.write(str(row[4]).encode())
                    self.wfile.write(b'</td></tr>')

                
                self.wfile.write(b"<hr><h2>Update Patient</h2>")


                self.wfile.write(b"<form action='/updatePatient' method='post'>")
                self.wfile.write(b'<label for="patient_id">ID of patient to be updated:</label>\
                      <input type="number" id="patient_id" name="patient_id" required><br><br>\
                      <label for="patient_name">Patient Name:</label>\
                      <input type="text" id="patient_name" name="patient_name"><br><br>\
                      <label for="patient_age">Age:</label>\
                      <input type="number" id="patient_age" name="patient_age"><br><br>\
                      <label for="admission_date">Admission Date:</label>\
                      <input type="date" id="admission_date" name="admission_date"><br><br>\
                      <label for="discharge_date">Discharge Date:</label>\
                      <input type="date" id="discharge_date" name="discharge_date"><br><br>\
                      <input type="submit" value="Submit">\
                      </form>')
                                 
                self.wfile.write(b"<br><br>")
                self.wfile.write(b"</center></body></html>")
                return

            #End Update Patient

            
            if self.path == '/dischargePatient':
                data=[]
                records = self.database.getAllPatients()
                print(records)
                data=records
                self.send_response(200)
                self.send_header('Content-type','text/html')
                self.end_headers()
                self.wfile.write(b"<html><head><title> Hospital's Portal </title></head>")
                self.wfile.write(b"<body>")
                self.wfile.write(b"<center><h1>Hospital's Portal</h1>")
                self.wfile.write(b"<hr>")
                self.wfile.write(b"<div> <a href='/'>Home</a>| \
                                 <a href='/addPatient'>Add Patient</a>|\
                                  <a href='/scheduleAppointment'>Schedule Appointment</a>|\
                                  <a href='/viewAppointments'>View Appointments</a>|\
                                  <a href='/viewAllDoctors'>Doctors</a>|\
                                  <a href='/viewRecords'>Records</a>|\
                                  <a href='/updatePatient'>Update Patients</a>|\
                                  <a href='/dischargePatient'>Discharge Patient</a></div>")


                self.wfile.write(b"<table border=2> \
                                    <tr><th> Patient ID </th>\
                                        <th> Patient Name</th>\
                                        <th> Age </th>\
                                        <th> Admission Date </th>\
                                        <th> Discharge Date </th></tr>")
                for row in data:
                    self.wfile.write(b' <tr> <td>')
                    self.wfile.write(str(row[0]).encode())
                    self.wfile.write(b'</td><td>')
                    self.wfile.write(str(row[1]).encode())
                    self.wfile.write(b'</td><td>')
                    self.wfile.write(str(row[2]).encode())
                    self.wfile.write(b'</td><td>')
                    self.wfile.write(str(row[3]).encode())
                    self.wfile.write(b'</td><td>')
                    self.wfile.write(str(row[4]).encode())
                    self.wfile.write(b'</td></tr>')




                
                self.wfile.write(b"<hr><h2>Discharge Patient</h2>")

                #Add Code Code Here
                


                
                
                self.wfile.write(b"<form action='/dischargePatient' method='post'>")
                self.wfile.write(b'<label for="patient_id">ID of patient to be discharged:</label>\
                      <input type="number" id="patient_id" name="patient_id"/><br><br>\
                      <input type="submit" value="Submit">\
                      </form>')
                
                self.wfile.write(b"<br><br>")
                self.wfile.write(b"</center></body></html>")
                return
            ##Add More path for the rest


            
            
        except KeyboardInterrupt:
                pass

def run(server_class=HTTPServer, handler_class=HospitalPortalHandler, port=8000):
    
    server_address = ('localhost', port)
    httpd = server_class(server_address, handler_class)
    print('Starting httpd on port {}'.format(port))
    httpd.serve_forever()
    

    
run()
