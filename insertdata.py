import mysql.connector


mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="pythonsql"
)


cursor = mydb.cursor()

patient_data = {
    "Name": "Emily Smith",
    "DOB": "1992-03-08",
    "Gender": "Female",
    "Blood_Type": "B",
    "Height": "168",
    "Weight": "64",
    "Allergies": "None",
    "Medical_History": "Emily Smith has a relatively clean medical history with no significant chronic conditions.",
    "Past_Diseases": "1. Common Cold - 2005\n2. Tonsillitis - 2010",
    "Hospital_Visits": "1. County General Hospital - July 12, 2015",
    "Timeline_of_Visits": "1. County General Hospital - July 12, 2015\n - Reason: Fractured left wrist in a bicycle accident\n - Outcome: X-rays, casting, and discharged with instructions for follow-up care.",
    "Consulting_Doctors": "1. Dr. Mark Anderson - Orthopedic Surgeon",
    "Medications": "Over-the-counter pain relievers as needed for minor aches and pains.",
    "Previous_Surgeries": "None",
    "Emergency_Contact": "7891234010"

}
insert_statement = "INSERT INTO patient_data (name, dob, gender, blood_type, height, weight, allergies, medical_history, past_diseases, hospital_visits, timelinevisit, consulting_doctors, medications, previous_surgeries, emergency_contact) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
data_values = tuple(patient_data.values())

cursor.execute(insert_statement, data_values)


mydb.commit()

cursor.close()
mydb.close()
