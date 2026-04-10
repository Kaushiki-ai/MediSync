# appointments.py - LOCAL VERSION

class Appointment:
    def __init__(self, patient_name, doctor_name, date, time, city, state):
        self.patient_name = patient_name
        self.doctor_name = doctor_name
        self.date = date
        self.time = time
        self.city = city
        self.state = state

    def schedule(self):
        return (f"[LOCAL] Appointment for {self.patient_name} with Dr. {self.doctor_name} "
                f"in {self.city}, {self.state}")

