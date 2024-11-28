import streamlit as st
from generate import generate_mcqs
from export import export_to_doc
from utils import extract_text_from_pdf

def display_mcq(mcqs):
    st.title("Multiple Choice Questions")

    if 'user_answers' not in st.session_state:
        st.session_state.user_answers = [None] * len(mcqs)

    if 'submitted' not in st.session_state:
        st.session_state.submitted = False

    if st.button("Reset Choices"):
        for idx in range(len(mcqs)):
            st.session_state[f"q_{idx}"] = None
        st.session_state.user_answers = [None] * len(mcqs)
        st.session_state.submitted = False
        st.rerun()

    # Form for questions
    with st.form("mcq_form"):
        for idx, mcq in enumerate(mcqs):
            st.subheader(mcq['question'])
            options = mcq['choices']
            choice = st.radio(
                f"Select your answer for Question {idx+1}:",
                options,
                key=f"q_{idx}"
            )
            st.session_state.user_answers[idx] = choice  # Update user's answers

        submitted = st.form_submit_button("Submit All Answers")
        if submitted:
            st.session_state.submitted = True

    if st.session_state.submitted:
        for idx, mcq in enumerate(mcqs):
            correct_answer = mcq['answer']
            if st.session_state.user_answers[idx] == correct_answer:
                st.success(f"Question {idx+1}: Correct! The answer is {correct_answer}")
            else:
                st.error(f"Question {idx+1}: Incorrect. The correct answer is {correct_answer}")


    if st.button("Export to DOC"):
        doc_buffer = export_to_doc(mcqs)
        st.download_button(
            label="Download DOC",
            data=doc_buffer,
            file_name="mcqs.docx",
            mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
        )

def main():
    st.sidebar.title("Quiz-N-learn")
    
    st.sidebar.write("This Web app displays 5 multiple-choice questions generated from PDF.")
    

    uploaded_file = st.sidebar.file_uploader("Choose a PDF file", type="pdf")
    
    if uploaded_file is not None:

        pdf_text = extract_text_from_pdf(uploaded_file)
        
      
        if st.sidebar.button("Generate New Questions"):
            st.session_state.pop('mcqs', None)
            st.session_state.user_answers = [None] * 5
            st.session_state.submitted = False
            for idx in range(5):  
                st.session_state.pop(f"q_{idx}", None)
            st.rerun()
        
        # Generate MCQs
        if 'mcqs' not in st.session_state:
            with st.spinner('Generating MCQs...'):
                st.session_state.mcqs = generate_mcqs(pdf_text)
        
        if st.session_state.mcqs:
            st.sidebar.success("MCQs generated successfully!")
            display_mcq(st.session_state.mcqs)
        else:
            st.sidebar.error("Failed to generate MCQs.")
    else:
        st.sidebar.info("Upload a PDF to generate MCQs.")

if __name__ == "__main__":
    main()
