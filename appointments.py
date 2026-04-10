class Appointment:  
    def __init__(self, patient_name, doctor_name, date, time, city, state):  
        self.patient_name = patient_name  
        self.doctor_name = doctor_name  
        self.date = date  
        self.time = time  
        self.city = city  
        self.state = state  

    def schedule(self):  
        return (f"Appointment scheduled for {self.patient_name} with Dr. {self.doctor_name} "
                f"on {self.date} at {self.time} in {self.city}, {self.state}.")