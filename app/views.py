# Imports
import os
from flask import render_template, request, url_for, redirect, send_from_directory, jsonify, session
from flask_login import login_user, logout_user, current_user, login_required
from werkzeug.exceptions import HTTPException, NotFound, abort
from jinja2 import TemplateNotFound
from openai import AzureOpenAI
from app import app, lm, db, bc
from app.models import *
import requests
import numpy as np
from dotenv import load_dotenv
import base64
import azure.cognitiveservices.speech as speechsdk
import time

from array import array
from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import OperationStatusCodes
from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes
from msrest.authentication import CognitiveServicesCredentials
from io import BytesIO
from flask import send_file
from azure.cognitiveservices.speech import SpeechSynthesizer
from azure.cognitiveservices.speech.audio import AudioConfig
import json
import random
load_dotenv()
# Azure OpenAI Client Initialization
client = AzureOpenAI(
  api_key="1314c89d0d7647c495a818998dfedf96",
  api_version="2024-02-01",
  azure_endpoint="https://cognipath.openai.azure.com/"
)
API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-xl-base-1.0"
API_URL_trocr="https://api-inference.huggingface.co/models/microsoft/trocr-large-handwritten"
headers = {"Authorization": "Bearer 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"}
import time
from array import array
from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import OperationStatusCodes
from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes
from msrest.authentication import CognitiveServicesCredentials
from io import BytesIO
from flask import send_file
from azure.cognitiveservices.speech import SpeechSynthesizer
from azure.cognitiveservices.speech.audio import AudioConfig
CV_API_KEY = os.getenv("CV_API_KEY")
SP_API_KEY = "1314c89d0d7647c495a818998dfedf96"
ENDPOINT = "https://cog.cognitiveservices.azure.com/"
computervision_client = ComputerVisionClient(ENDPOINT, CognitiveServicesCredentials("c6875d143a96465cad2ba687d274c223"))
import json
import random
# Configure Azure Cognitive Services Speech SDK
speech_config = speechsdk.SpeechConfig("fd1c98be42a2404d91f56ab21507bd1c", "francecentral")
audio_config = speechsdk.audio.AudioOutputConfig(use_default_speaker=True)
speech_config.speech_synthesis_voice_name = 'en-US-AnaNeural'
speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)



# provide login manager with load_user callback
@lm.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))

@login_required
@app.route('/back_index')
def back_index():
    # Access user attributes from the current_user object
    session['flag'] = 0
    # json_file = 'app/static/emotions.json'
    # random_id, random_sentence = get_random_emotion(json_file)
    # filename = f"app/static/gen_images/{random_id}.jfif"
    # generate_image(API_URL, headers, filename,random_sentence)
    count_activities = update_user_scores(current_user.email)
    activities_count_per_days = get_activities_count_by_day(current_user.email)
    activities_count_per_week = get_activities_count_by_week(current_user.email)
    activities_count_per_month = get_activities_count_by_month(current_user.email)
    recent_activities = get_recent_activities(current_user.email)
    # Render the dashboard template and pass the user data
    return render_template('dashboard.html', user=current_user, count_activities=count_activities, 
                           activities_count_per_days=activities_count_per_days,
                           activities_count_per_week=activities_count_per_week,
                            activities_count_per_month=activities_count_per_month,
                            recent_activities = recent_activities )
# Logout user
@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


# Register a new user
@app.route('/auth', methods=['GET', 'POST'])
def register():
    msg = None
    success = False

    if request.method == 'POST':
        if 'signup' in request.form:  # Check if the signup form is submitted
            username = request.form['FullName']
            email = request.form['Email']
            password = request.form['mdp']
            pathology = "ASD"

            # Check if the required fields are not empty
            if username and email and password:
                # Check if a user with the same username or email already exists
                user = Users.query.filter_by(user=username).first()
                user_by_email = Users.query.filter_by(email=email).first()

                if user or user_by_email:
                    msg = 'User already exists!'
                else:
                    pw_hash = bc.generate_password_hash(password)
                    user = Users(username, email, pw_hash,progression=0,Language=0,Intellect=0, Social_Skills=0,pathology='ASD',isPremium=False)
                    user.save()
                    msg = 'Welcome '+username+' to CogniPath'
                    success = True
            else:
                msg = 'Input error'

        elif 'signin' in request.form:  # Check if the signin form is submitted
            email_login = request.form['Email_login']
            password_login = request.form['mdp_login']

            # Check if the required fields are not empty
            if email_login and password_login:
                user = Users.query.filter_by(email=email_login).first()

                if user:
                    if bc.check_password_hash(user.password, password_login):
                        login_user(user)
                        return redirect(url_for('index'))
                    else:
                        msg = "Wrong password. Please try again."
                else:
                    msg = "Unknown user"
            else:
                msg = 'Sign-in failed. Please try again.'

    return render_template('login.html', msg=msg, success=success)


# Authenticate user
@app.route('/login', methods=['GET', 'POST'])
def login():

    # Flask message injected into the page, in case of any errors
    msg = None
    
    # check if both http method is POST and form is valid on submit
    if form.validate_on_submit():

        # assign form data to variables
        username = request.form.get('username', '', type=str)
        password = request.form.get('password', '', type=str) 

        # filter User out of database through username
        user = Users.query.filter_by(user=username).first()

        if user:
            
            if bc.check_password_hash(user.password, password):
                login_user(user)
                return redirect(url_for('index'))
            else:
                msg = "Wrong password. Please try again."
        else:
            msg = "Unknown user"

    return render_template( 'login.html', form=form, msg=msg )

# App main route + generic routing
@app.route('/', defaults={'path': 'index'})
@app.route('/<path>')
def index(path):

    #if not current_user.is_authenticated:
    #    return redirect(url_for('login'))

    try:

        return render_template( 'index.html')
    
    except TemplateNotFound:
        return render_template('page-404.html'), 404
    
    except:
        return render_template('page-500.html'), 500

# Return sitemap
@app.route('/sitemap.xml')
def sitemap():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'sitemap.xml')



@app.route('/homepage', methods=['GET', 'POST'])
def homepage():
    json_file = 'app/static/emotions.json'
    random_id, random_sentence = get_random_emotion(json_file)
    filename = f"app/static/gen_images/{random_id}.jfif"
    generate_image(API_URL, headers, filename,random_sentence)
    ##session['output'], session['correct_emotion'] = process_emotion_image(API_URL, headers, filename)
    return render_template('index.html')   

 
@app.route("/display_image/<filename>")
def display_image(filename):
    return send_file(filename, mimetype='image/jfif')




@app.route('/Essay_correction')
@login_required
def Essay_correction():
    return render_template('EssayCorrection.html')


@app.route('/Text_simplification')
@login_required
def Text_simplification():
    return render_template('Text_simplification.html')

@app.route('/cognipro')
@login_required
def cognipro():
    return render_template('cognipro.html')
@app.route("/generate_text", methods=["POST"])
@login_required
def generate_text():
    try:
        image = request.files["image"]
        if image:
            img_stream = BytesIO(image.read()) # Read the uploaded file as bytes
            img_data = base64.b64encode(img_stream.getvalue()).decode('utf-8')
            read_response = computervision_client.read_in_stream(img_stream, language='en', raw=True)
            read_operation_location = read_response.headers["Operation-Location"]
            operation_id = read_operation_location.split("/")[-1]

            while True:
                read_result = computervision_client.get_read_result(operation_id)
                if read_result.status not in ['notStarted', 'running']:
                    break
                time.sleep(1)

            if read_result.status == OperationStatusCodes.succeeded:
                extracted_text = ''  # Create a variable to store the extracted text
                for text_result in read_result.analyze_result.read_results:
                    for line in text_result.lines:
                        extracted_text += line.text + ' '
            # You can return the extracted text and any other data you want to the template
            return render_template("EssayCorrection.html", generated_text=extracted_text,imgg=img_data)

    except Exception as e:
        return f"An error occurred: {str(e)}"


@app.route("/correct_text", methods=["POST"])
def correct_text():
    activity = "Writing Wizard"
    user_input = request.form["user_input"]

    # Use the user_input as input for ChatGPT
    messages = [
    {
        "role": "user",
        "content": user_input
    },
    {
        "role": "assistant",
        "content": """Great job sharing your work with us! We're here to help you grow as a writer. Please use this format for feedback:

Grade: [Your grade, like A, B, or C]

Strengths:
- [Strength 1]
- [Strength 2]
- [Add more strengths if desired]

Areas for Improvement:
- [Area for Improvement 1]
- [Area for Improvement 2]
- [Add more areas for improvement if desired]

Remember, every great writer started somewhere, and we believe in your potential!"""
    }
]
    try:
        # Make the OpenAI chat completion request
        response = client.chat.completions.create(
            model='cog',  # use the correct model name or deployment name
            messages=messages,
            temperature=0,
            max_tokens=256,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        assistant_reply = response.choices[0].message.content
        print(assistant_reply)

        # Split the response into lines
        lines = assistant_reply.split('\n')

        # Initialize variables to store the grade, strengths, and areas for improvement
        grade = ""
        strengths = ""
        areas_for_improvement = ""

        current_section = None

                # Iterate through the lines to categorize them into grade, strengths, and areas for improvement
        for line in lines:
                if line.startswith("Grade:"):
                    current_section = "Grade"
                    grade += line + '\n'
                elif line.startswith("Strengths:"):
                    current_section = "Strengths"
                    strength_points = line.split("\n")
                    strengths += '\n'.join(point.strip() for point in strength_points if point.strip()) + '\n'
                elif line.startswith("Areas for Improvement:"):
                    current_section = "Areas for Improvement"
                    improvement_points = line.split("\n")
                    areas_for_improvement += '\n'.join(point.strip() for point in improvement_points if point.strip()) + '\n'
                else:
                    if current_section == "Grade":
                        grade += line + '\n'
                    elif current_section == "Strengths":
                        strengths += line + '\n'
                    elif current_section == "Areas for Improvement":
                        areas_for_improvement += line + '\n'
        pros = strengths
        cons=areas_for_improvement  # Replace with the actual areas for improvement
        calculate_score(grade, activity)

    except Exception as e:
        return f"Error generating assistant reply: {str(e)}"
    # Render the HTML template with the variables
    return render_template("EssayCorrection.html", grade=grade, pros=pros, cons=cons, user_input=user_input)

@app.route("/simplify", methods=["GET", "POST"])
def simplify():
    if request.method == "GET":
        return render_template("simplify.html")

    user_input = request.form["user_input"]
    generated_text = user_input  # Use the user-provided text as input

    # Use the generated_text as input for ChatGPT
    messages = [
        {
            "role": "system",
            "content": "Simplify the paragraph given please so a 5-year-old can understand it make it like a short story of maximum 70 words  : "
        },
        {
            "role": "user",
            "content": generated_text  # Use the user-provided text as the user's input
        }
    ]

    # Make the OpenAI chat completion request
    response = client.chat.completions.create(
        model='cog',  # Use the correct model name
        messages=messages,
        temperature=0,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    assistant_reply = response.choices[0].message.content
    print(assistant_reply)

    return render_template("simplify.html", generated_text=generated_text, corrected_text=assistant_reply)

@app.route("/play_voice", methods=["GET"])
def play_voice():
    generated_text = request.args.get("generated_text")

    # Define the path relative to the app's root directory
    output_path = os.path.join(app.root_path, "output.mp3")

    audio_config = AudioConfig(filename=output_path)
    synthesizer = SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)
    synthesizer.speak_text(generated_text)

    return send_file(output_path, as_attachment=True)

def separate_sentences(input_list):
    if len(input_list) == 1:
        # Split the single string in the list into sentences based on the newline character ('\n')
        sentences = input_list[0].split('\n')

        # Remove any leading or trailing whitespace from each sentence
        sentences = [sentence.strip() for sentence in sentences]

        return sentences
    else:
        return []
def generate_image(API_URL, headers, filename,correct_emotion):
    payload = {
        "inputs": correct_emotion
    }

    try:
        response = requests.post(API_URL, headers=headers, json=payload)
        response.raise_for_status()
        image_bytes = response.content

        # Save the image to a file
        with open(filename, "wb") as f:
            f.write(image_bytes)
    except requests.exceptions.RequestException as e:
        print({"error": str(e)})
    
def process_emotion_options(API_URL, headers, filename,correct_emotion):
    prompts = [
        "I want you to generate a 4 random simple emotion recognition sentences for example : 'A sad lady in red' or 'A happy young girl holding a toy'"
    ]
    output = separate_sentences(generate_emotion_recognition_text(prompts))
    if output: 
        output[random.randint(0, 3)] = correct_emotion

    print(output)
    return output
    
def get_random_emotion(json_file):
    try:
        with open(json_file, 'r') as file:
            data = json.load(file)
            random_id = random.choice(list(data.keys()))
            random_sentence = data[random_id]
            return random_id, random_sentence
    except (FileNotFoundError, json.JSONDecodeError):
        return None, None
    

@app.route('/Emotions', methods=['GET', 'POST'])
def Emotions():
     output = ['A happy girl in a pink dress', 'A teary-eyed child at the dentist office.', 'An old woman feeling nostalgic', 'A boy looking sad and lost']
     json_file = 'app/static/emotions.json'
     random_id, random_sentence = get_random_emotion(json_file)
     filename = f"gen_images/{random_id}.jfif"
     session['correct_emotion'] = random_sentence
     output_intermediate  = process_emotion_options(API_URL, headers, filename,correct_emotion=random_sentence)
     print("**********************session flag ",session['flag'])
     if output_intermediate:
         session['output'] = output_intermediate
     else: 
         session['output'] = output
         session['correct_emotion'] = "A teary-eyed child at the dentist office."
         filename = "gen_images/5.jfif"
     if request.method == "get":
         submitted_choice = request.form.get('selected-choice', '', type=str)
         #submitted_choice = request.form["selected-choice"]
         print("submitted choice *************************",submitted_choice)
        #  if session['correct_emotion'] == submitted_choice:
        #      print("Correct********************************************************")
        #  else:
        #      print("Wrong********************************************************")
     return render_template('Emotions_Recognition.html', image_filename=filename)


@app.route('/profile')
def profile():
    return render_template('profile.html')

def generate_emotion_recognition_text(prompts):
    # Initialize an array to store the results
    results = []
    retry_interval = 30

    # Initialize the OpenAI API client
    try:
        # Generate text for each prompt and append it to the results array
        for prompt in prompts:
            response = client.chat.completions.create(
                model='cog',  # use the correct model name or deployment name
                prompt=prompt,
                max_tokens=50  # Adjust the max tokens as needed
            )
            result_text = response.choices[0].text.strip()
            results.append(result_text)
    except Exception as e:  # Catch all exceptions
        print(f"An error occurred: {str(e)}")
        time.sleep(retry_interval)

    

    

    return results


def calculate_score(grade, activity):
    if grade:
        if activity == "Writing Wizard":
            language_score = [ 5 if grade.strip()=="Grade: A" else 4 if grade.strip()=="Grade: B" else 3 if grade.strip()=="Grade: C" else 2]
            language_score = language_score[0]
            social_score = 0
            
        elif activity == "Emotion Recognition":
            language_score = 0
            social_score = [ 5 if grade.strip()=="Grade: A" else 0 ]
            social_score = social_score[0]
        intellect_score = round(0.7*language_score + 0.3*social_score,0)
        new_activity = Activity(
            title=activity,
            input=activity,
            output="Output",
            user_email=current_user.email,
            activity=activity,
            social_score=social_score,
            intellect_score=intellect_score,
            language_score=language_score,
            avg_score=round((social_score+intellect_score+language_score)/3,0)
        )
        
        
        new_activity.save()
        update_user_scores(current_user.email)

@app.route('/update_session_variable', methods=['POST'])
def update_emotion_score():
    data = request.get_json()
    if 'flag' in data:
        #session['flag'] 
        score = data['flag']
        data['flag'] = 0
        activity = "Emotion Recognition"
        if score == 10:
            grade = "Grade: A"
            score = 0   
        else:
            grade = "Grade: E"
        calculate_score(grade, activity)
        return jsonify({'message': 'Session variable updated'})
    else:
        return jsonify({'error': 'Invalid data received'})