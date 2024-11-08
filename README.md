# Quiz-n-Learn

**Quiz-n-Learn** is an AI-driven web application that generates multiple-choice questions (MCQs) from uploaded PDF files, designed to provide an interactive and engaging learning experience. Leveraging Groq LLM, it creates quizzes in real-time with features like scoring, feedback, and exporting MCQs to Word documents for offline practice.

## Features

- **PDF Upload**: Upload any PDF file to extract text content for quiz generation.
- **Automatic MCQ Generation**: Uses Groq LLM to create relevant multiple-choice questions based on the PDF content.
- **Real-Time Feedback**: Interactive quiz interface provides instant scoring and feedback.
- **Export to Word**: Save generated MCQs as a Word document for easy distribution or offline study.

## Tech Stack

- **Frontend**: Streamlit
- **Backend**: Python, LangChain, Groq LLM
- **Libraries**:
  - `python-docx`: for exporting MCQs to Word documents
  - `PyPDF2`: for PDF parsing
  - `dotenv`: for managing environment variables

