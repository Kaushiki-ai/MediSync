# appointments.py - REMOTE VERSION

class Appointment:
    def __init__(self, patient_name, doctor_name, date, time, location):
        self.patient_name = patient_name
        self.doctor_name = doctor_name
        self.date = date
        self.time = time
        self.location = location

    def schedule(self):
        return f"[REMOTE] Appointment for {self.patient_name} with Dr. {self.doctor_name} at {self.location}"

