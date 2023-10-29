import speech_recognition as sr
import pyttsx3
import mysql.connector
from fpdf import FPDF
import subprocess

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="pythonsql"
)

recognizer = sr.Recognizer()
engine = pyttsx3.init()


def create_pdf(text_content, pdf_file):
    pdf = FPDF(format='letter')
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(190, 10, txt=text_content, align='L')
    pdf.output(pdf_file)


def speak(text):
    engine.say(text)
    engine.runAndWait()


def fetch_patient_data_and_create_pdf(patient_ID):
    cursor = mydb.cursor()
    select_query = "SELECT * FROM patient_data WHERE id = %s"
    cursor.execute(select_query, (patient_ID,))
    patient_data = cursor.fetchone()

    if patient_data:

        formatted_data = f"Name: {patient_data[1]}\nDOB: {patient_data[2]}\nGender: {patient_data[3]}\nBlood Type: {patient_data[4]}\nHeight: {patient_data[5]}\nWeight: {patient_data[6]}\nAllergies: {patient_data[7]}\nMedical History: {patient_data[8]}\nPast Diseases: {patient_data[9]}\nHospital Visits: {patient_data[10]}\nConsulting Doctors: {patient_data[11]}\nMedications: {patient_data[12]}\nPrevious Surgeries: {patient_data[13]}\nEmergency Contact: {patient_data[14]}\nTimeline of Visits: {patient_data[15]}"

        pdf_filename = f"patient_{patient_ID}.pdf"

        with open(f"patient_{patient_ID}.txt", "w") as text_file:
            text_file.write(formatted_data)

        create_pdf(formatted_data, pdf_filename)

        speak(f"Patient data has been written to patient_{patient_ID}.txt and {pdf_filename}.")
        subprocess.Popen(["start", "", pdf_filename], shell=True)
    else:
        speak("Patient not found in the database.")


with sr.Microphone() as source:
    speak("Hello! Welcome to the patient data service.")
    speak("Please provide the Patient ID.")
    audio = recognizer.listen(source)

    try:
        patient_ID = recognizer.recognize_google(audio)
        speak(f"You provided the Patient ID: {patient_ID}")
        fetch_patient_data_and_create_pdf(patient_ID)
    except sr.UnknownValueError:
        speak("Unable to recognize speech.")
    except sr.RequestError as e:
        speak(f"Error: {str(e)}")


