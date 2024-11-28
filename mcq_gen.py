import gradio as gr

# Function to generate multiple-choice questions
def generate_mcqs(topic):
    
    mcqs = [
        {
            "question": "1. What type of plot is required for the data in the table listing the number of strikeouts posted by the top 30 strikeout pitchers in the 2008 Major League Baseball season?",
            "choices": ["Bar chart", "Histogram", "Stem-and-leaf plot", "Scatter plot"],
            "answer": "Stem-and-leaf plot"
        },
        {
            "question": "2. Which approach of probability is used in a situation where a political polling survey is conducted with a large sample size, and voters are asked which candidate they support?",
            "choices": ["Classical approach", "Relative frequency approach", "Subjective approach", "Empirical approach"],
            "answer": "Relative frequency approach"
        },
        {
            "question": "3. What is the probability distribution that will be used to find the probabilities in a clinical trial where researchers are testing the effectiveness of a new medication?",
            "choices": ["Binomial distribution", "Poisson distribution", "Normal distribution", "Exponential distribution"],
            "answer": "Binomial distribution"
        },
        {
            "question": "4. If a random variable Y = 3X - 2 and X follows a normal distribution with mean 2 and variance 4, what is the mean of the random variable Y?",
            "choices": ["2", "4", "6", "8"],
            "answer": "6"
        },
        {
            "question": "5. What is the transformation used to find the probability density function for the random variable Y, where Y = βX and X follows a Gamma(α) distribution?",
            "choices": ["Linear transformation", "Non-linear transformation", "Affine transformation", "Gamma transformation"],
            "answer": "Linear transformation"
        }
    ]
    
    # Formatting the output as a string to display in Gradio
    output = ""
    for i, mcq in enumerate(mcqs, 1):
        output += f"{i}. {mcq['question']}\n"
        for j, choice in enumerate(mcq['choices'], 1):
            output += f"   {j}) {choice}\n"
        output += f"Answer: {mcq['answer']}\n\n"
    
    return output

# Create the Gradio interface
iface = gr.Interface(
    fn=generate_mcqs,  # Function to call when interacting with the Gradio interface
    inputs="text",  # Input type (text box)
    outputs="text",  # Output type (text area for displaying questions)
    title="Quiz-N-learn",  # Title for the web interface
    description="Enter a topic to generate multiple-choice questions."  # Description for users
)

# Launch the Gradio app
iface.launch()
