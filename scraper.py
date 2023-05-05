import PyPDF2
import pandas as pd
import re

# Open the PDF file
with open('pega_process_fabric_hub_2-17-2023', 'rb') as pdf_file:
    # Create a PDF reader object
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    
    # Create an empty list to hold the extracted sentences
    sentences = []
    
    # Loop over each page in the PDF
    for page_num in range(len(pdf_reader.pages)):
        # Extract the text from the page
        page_text = pdf_reader.pages[page_num].extract_text()
        
        # Split the text into sentences using regular expression
        page_sentences = re.split(r'[.!?]+', page_text)
        
        # Combine four sentences into one record
        combined_sentences = []
        for i in range(0, len(page_sentences), 2):
            sentence = page_sentences[i].strip().replace('\n', '')
            if i+1 < len(page_sentences):
                sentence += ' ' + page_sentences[i+1].strip().replace('\n', ' ')
           
           
            combined_sentences.append(sentence)
        
        # Only include sentences that contain at least one alphabetic character
        for sentence in combined_sentences:
            if re.search('[a-zA-Z]', sentence):
                sentences.append(sentence)
    
    # Convert the list of sentences to a pandas DataFrame
    df = pd.DataFrame({'Sentence': sentences})
    
    # Save the DataFrame to a CSV file
    df.to_csv('sentences_robot.csv', index=False)
