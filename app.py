from flask import Flask, request, jsonify
from flask_cors import CORS
import os
from resume_matcher import extract_text_from_pdf, get_resume_score

app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/upload', methods=['POST'])
def upload_resume():
    file = request.files['resumes']
    if not file.filename.endswith('.pdf'):
        return jsonify({'error': 'Only PDF files are allowed'}), 400

    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(file_path)

    job_description = """
    We are seeking a highly skilled and motivated Python Developer to join our growing technology team. The ideal candidate will have a strong background in Python programming, experience in building web applications using Flask, and a solid understanding of machine learning and natural language processing (NLP) concepts. You will be responsible for designing, developing, and deploying intelligent systems that process and analyze natural language data, as well as integrating these capabilities into scalable web applications. This role requires collaboration with data scientists, frontend developers, and product teams to build solutions that solve real-world problems.
 Responsibilities:
Develop RESTful APIs and backend logic using Flask
1. Implement machine learning models and integrate them into web applications
2.Preprocess, clean, and analyze large sets of text data
3. Build NLP pipelines for tasks such as classification, entity extraction, summarization, and semantic matching
4.Work with tools such as scikit-learn, spaCy, NLTK, TensorFlow, or PyTorch
5.Write clean, maintainable, and well-documented Python code
6.Collaborate with frontend developers to ensure seamless user experiences
7.Optimize applications for maximum speed and scalability
8.Perform code reviews and write unit tests


    """

    resume_text = extract_text_from_pdf(file_path)
    score = get_resume_score(resume_text, job_description)

    return jsonify({
        'filename': file.filename,
        'match_score': score
    })

if __name__ == '__main__':
    app.run(debug=True)
