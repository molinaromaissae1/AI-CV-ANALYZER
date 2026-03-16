# AI-CV-ANALYZER
This project is a prototype of an intelligent system designed to analyze CVs automatically and extract relevant information.

The system reads CV files in PDF format and extracts important features such as:
	•	professional experience
	•	education level
	•	technical skills
	•	languages
	•	sector of activity

These features are then used to calculate an ATS score that helps evaluate the candidate profile.
Technologies Used
	•	Python
	•	Streamlit
	•	Regular Expressions (Regex)
	•	PDF text extraction
  Project Structure

app.py
Main application and Streamlit interface.

reader.py
Extracts text from PDF CV files.

preprocess.py
Cleans and prepares text for analysis.

features.py
Extracts features such as skills, languages, sector and companies.

education_experience.py
Extracts education level and experience duration.

ats_scoring.py
Calculates the ATS score of the candidate.

requirements.txt
Contains the libraries needed to run the project.

⸻

How to Run the Project
	1.	Install the required libraries

pip install -r requirements.txt
	2.	Run the application

streamlit run app.py
	3.	Upload a CV in PDF format and the system will analyze it automatically.

⸻

Conclusion

This project demonstrates how an intelligent system can assist in the recruitment process by automatically analyzing CVs and ranking candidates based on extracted information.
