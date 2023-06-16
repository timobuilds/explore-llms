# LLM Playground

## Introduction
------------
 This is a collection of silly AI apps built with Streamlit. It provides some examples of what LLMs can do!
    - **LinkBlink**: Upload a URL and summarize the content on the website.
    - **PDF Search**: Upload a single PDF and ask it questions one at a time.  
    - **ChatPDFs**: Upload multiple PDFs and have a conversation with them.  
    - **SciFi StoryTime**: Upload an image, get a story. 
    - **AutoRnD**: An agent that automates the collection and generation of research ideas from Twitter.  
    - **Script Generator**: An agent that uses sequential chains of prompts generate Youtube script summary. 



# Dependencies 
----------------------------
Install:

1. Clone the repository to your local machine.

2. Create VM


Using `conda`:
``` bash
cd multi-pdf-chat
conda create -n mpc-env python=3.9
conda activate mpc-env
```

2. Install the required dependencies by running the following command:
   ```
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the root directory of the project. Inside the file, add your OpenAI API key:

```makefile
OPENAI_API_KEY=your_api_key_here
```

## Usage
-----
Steps:

1. Ensure that you have installed the required dependencies and added the OpenAI API key to the `.env` file.

2. Run the `main.py` file using the Streamlit CLI. Execute the following command:
   ```
   streamlit run app.py
   ```

3. The application will launch in your default web browser, displaying the user interface.

4. Loa.....

