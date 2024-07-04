<h1 align="center" id="title">CogniPath</h1>
<h2>Welcome to Cognipath – Your Learning Companion for Students with Learning Difficulties!</h2>


<p>Cognipath is more than just a website, it's a dedicated learning platform designed to empower all the students inluding those with mental illness like ADHD and ASD. Our mission is to make education accessible, engaging, and tailored to the unique needs of every learner.</p>

<img src="https://github.com/Me710/CogniPath-A2SV-GenAI/assets/80206931/f61b7e7d-4359-4b73-a9fc-9d9e70f80ca8" alt="project-screenshot" width=auto height="auto">

<h2>🧐 Structure</h2>

```
|-- .venv/                                 # Virtual environment folder
|-- requirements.txt                      # App Dependencies
|-- run.py                                # Start the app - WSGI gateway
|
|-- app/
|    |
|    |-- authentication/
|    |    |
|    |    |-- static/
|    |    |    |
|    |    |    |-- auth/
|    |    |    |    |-- css/
|    |    |    |    |-- img/
|    |    |    |    |-- js/
|    |    |    |
|    |    |    |-- front/
|    |    |    |    |-- css/
|    |    |    |    |-- img/
|    |    |    |    |-- js/
|    |    |    |-- back/
|    |    |    |    |-- css/
|    |    |    |    |-- img/
|    |    |    |    |--js/
|    |-- templates/                      # Templates used to render pages
|    |    |
|    |    |-- *.html                   # All HTML files
|    |
|    |-- views.py                       # App views and routes

```



## Detailed description of our Generative AI models

* **Writing Wizard:** Our Writing Wizard feature offers comprehensive support for enhancing writing skills. Users can select a handwritten paragraph and initiate the analysis process by clicking on the "recognize" button. The tool utilizes the Azure Cognitive Services, specifically the Computer Vision API from Microsoft, renowned for its robust functionality in Optical Character Recognition (OCR).Following the recognition phase, the captured paragraph is readily available for further examination. Furthermore, users have the option to access an audio feature, enabling the playback of the text using Facebook's FastSpeech2-en-ljspeech technology. This interactive feature aids students in improving their English speech and enhancing pronunciation. In addition to the automated features, users retain control over their content and can manually edit the paragraph to correct any errors. They may also reference an accompanying image displayed on the right for context. Upon completing these steps, users can finalize their document by clicking the "correct" button, triggering a comprehensive feedback process. This feedback is generated through OpenAI's GPT-4o and provides insights into the strengths of the written work, including sentence structure, linkers, vocabulary usage, and areas for improvement. Users will find this feedback both informative and encouraging as they continue to refine their writing skills with the Writing Wizard feature.
* **Emotion recognition:** Emotional recognition is essentially a process involving two key components: Firstly, we employ the OpenAI API to generate four sentences related to emotions. Secondly, we utilize a stable-diffusion-xl -base-1.0 approach to produce an image that conveys one of the four generated phrases. The student's task is to correctly identify the correspondence between the image and the phrase. A pop-up message will appear to indicate success or failure in the student's ability to recognize the emotion. This feature is of paramount importance as it enhances emotional skills.
* **Storyfy:** We developed a new feature called "Storyfy" that allows users to input a word or a complex paragraph, and the system generates a kid-friendly story based on the input by OpenAI: GPT-4o. This feature includes text to speech (SpeechSynthesisUtterance with a male voice) integration and image generation for an interactive storytelling experience.
* **Chatbot:** The chatbot is a powerful tool in which we used botpress that can help students with ASD in a number of ways. It can provide students with support and guidance, answer their questions, and help them to develop coping mechanisms.

## How Generative AI Models are Solving the Problem

Generative AI models are solving the problem of helping students with mental illness like ASD in a number of ways.

* **Essay correction:** Generative AI models can help students with mental illness by providing them with feedback on their essays. This can help students to identify areas where they need to improve their writing skills, and to make their writing more clear, concise, and engaging.
* **Emotion recognition:** Generative AI models can help students with mental illness to better understand their own emotions, and the emotions of others. This can be helpful for social skills development, and for managing stress and anxiety.
* **Storyfy:** Generative AI models can help students with mental illness to develop their creativity and imagination. This can be helpful for self-expression, and for developing coping mechanisms for dealing with mental illness.
* **Chatbot:** The chatbot can provide students with support and guidance, answer their questions, and help them to develop coping mechanisms.


Generative AI models are a powerful tool that can be used to help students with mental illness in a number of ways. By providing students with feedback on their writing, helping them to better understand emotions, and developing their creativity, generative AI models can help students to thrive in school and in life.


<h2>🛠️ Installation Steps:</h2>

<p>1. Create a Virtual Environment</p>

```
python -m venv .venv
```

<p>2. Activate the Virtual Environment</p>

```
.venv\Scripts\activate
```

<p>3. Install Dependencies</p>

```
pip install -r requirements.txt
```

<p>4. Run the Application</p>

```
flask run --host=0.0.0.0 --port=5015
```


  
<h2>💻 Built with</h2>

Technologies used in the project:

*   Flask
*   Jinja2
*   OpenAI API (GPT-4o)
*   Microsoft Trocr (Optical Character Recognition)
*   OpenCV-Python
