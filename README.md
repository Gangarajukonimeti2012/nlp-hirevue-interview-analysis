# nlp-hirevue-interview-analysis
AI-driven NLP system that analyzes HireVue-style interview responses using speech-to-text, sentiment analysis, keyword extraction, topic modeling, and ML-based scoring to evaluate candidate communication, confidence, and job fit.

ResumeScoreX – NLP Based Resume Screening Tool

ResumeScoreX is an AI powered tool that automatically compares a candidate’s resume with a job description using Natural Language Processing. It extracts text from PDF resumes, analyzes the content, and generates a match score based on how closely the resume aligns with the job requirements. This project helps automate and speed up the hiring process by providing an efficient and consistent way to shortlist candidates.

Project Overview

Recruiters often receive many resumes for a single job role. Manually reviewing each one is time consuming, inconsistent and difficult to scale. ResumeScoreX solves this problem by using NLP techniques to automate resume screening.

The system extracts skills, keywords and text content from the resume and compares them with the job description using TF IDF vectorization and cosine similarity. The result is a final match score between 0 and 100.

How ResumeScoreX Works

Resume Upload
The user uploads a PDF resume through a simple web interface.

Text Extraction
The backend uses pdfplumber to extract text from the uploaded PDF file.

Text Vectorization
The resume text and job description text are converted into numerical vectors using TF IDF.

Similarity Calculation
Cosine similarity is used to compare the vectors.
1.0 represents a perfect match
0.0 represents no similarity

Match Score Output
The cosine similarity value is multiplied by 100 to produce a percentage match score.

Concepts Used

HTML
Used for the frontend interface where users upload the resume PDF.

Flask
Lightweight Python web framework used to build the backend. It handles file uploads, runs the NLP logic and returns the match score.

pdfplumber
Library used to extract text from PDF resumes.

Scikit Learn
Provides the TF IDF Vectorizer and cosine similarity function for text comparison.

NLTK
Used for text cleaning, tokenization and preprocessing.

Flask CORS
Allows the frontend to communicate with the backend API.

Core Functions

Text Extraction Function
Extracts text from each page of the PDF and returns a clean continuous text string.

Matching Logic

Converts resume and job description to TF IDF vectors

Computes cosine similarity

Converts similarity value to a percentage score

For example, a cosine similarity of 0.82 becomes a final match score of 82 percent.

Flask Endpoint Description

The endpoint named /upload handles the entire resume scoring process.

It accepts the uploaded PDF file, validates it, saves it, extracts text using pdfplumber, runs the TF IDF and cosine similarity logic, and returns the match score as JSON. This enables real time resume scoring from any frontend interface.

Project Features

PDF resume upload through a web interface
Automatic text extraction
TF IDF and cosine similarity based comparison
Flask backend API for processing
Match score between 0 and 100

Benefits and Impact

Saves time by automating resume screening
Improves accuracy through objective text analysis
Ensures consistent and fair evaluation
Scalable for multiple job roles and large datasets

Recommended Project Structure

ResumeScoreX
│ src
│ extraction
│ extract_text.py
│ matching
│ similarity.py
│ app.py
│ frontend
│ index.html
│ uploads
│ requirements.txt
│ README.md

Installation and Running Instructions

Install dependencies
pip install -r requirements.txt

Run the backend
python app.py

Open the frontend page
Upload the resume and view the match score.

Authors

Vishwajeet Kale
Ganga Raju K N
