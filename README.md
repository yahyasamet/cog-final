<h1 align="center" id="title">GreenPath</h1>
<h2>Welcome to Greenpath - Your Ultimate Destination for Sustainable Living!</h2>


<p>Greenpath is more than just a website; it's a comprehensive platform dedicated to fostering sustainable living practices. Our mission is to empower individuals to make environmentally conscious choices while embracing creativity and innovation.
</p>

<img src="[https://github.com/Me710/CogniPath-A2SV-GenAI/assets/80206931/f61b7e7d-4359-4b73-a9fc-9d9e70f80ca8](https://i.ibb.co/ZBfp2bg/Screenshot-2024-03-03-083808.png)" alt="project-screenshot" width=auto height="auto">

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




## Detailed description of our Recycle feature

Recycle is a revolutionary feature that empowers users to make informed decisions about recycling. Here's how it works:

- **Upload and Analyze:** Users can upload a photo of an item to Recycle. Recycle utilizes generative AI to analyze the item and provide tailored recycling instructions. For example, it might suggest the most environmentally friendly way to dispose of a water bottle, whether it's plastic, glass, or metal.

- **Educational Content:** Recycle also offers educational content to help users understand the importance of recycling and its impact on the environment. Users can learn about recycling best practices and discover creative ways to reduce waste.

- **Interactive Experience:** Recycle provides an interactive experience, allowing users to engage with the recycling process and track their environmental impact over time. With Recycle, users can make a meaningful difference in protecting our planet for future generations.

Join us in embracing sustainable living with Recycle and take the first step towards a greener future with Greenpath.

## Detailed description of our Foody feature

Foody is a revolutionary feature that empowers users to discover delicious recipes tailored to their ingredients. Here's how it works:

- **Ingredient Analysis:** Users can input their ingredients into Foody, and it will generate a variety of recipe options based on what they have on hand. Foody also offers nutritional information for each recipe, helping users make informed decisions about their meals.

- **Lowest Price Recipes:** Foody highlights the lowest price recipes for users, helping them minimize food waste and save money on groceries. With Foody, users can make the most of their ingredients while reducing their environmental footprint.

- **Interactive Cooking Experience:** Foody provides an interactive cooking experience, complete with step-by-step instructions and visual aids to guide users through the recipe. Whether you're a novice cook or a seasoned chef, Foody makes cooking fun and accessible for everyone.

Join us in exploring the culinary delights of Foody and make every meal a sustainable and delicious experience with Greenpath.

## Detailed description of our Donation feature

The Donation feature is a heartwarming addition to Greenpath, connecting those with items to spare to those in need. Here's how it works:

- **Donate and Receive:** Users can donate items they no longer need through the Donation feature. These items are then made available to those in need, creating a mutually beneficial exchange that promotes generosity and kindness.

- **Browse and Request:** Users in need can browse the Donation gallery to find items they require. They can then request these items through the platform, and donors can choose to fulfill these requests based on availability.

- **Community Support:** The Donation feature fosters a sense of community and solidarity, bringing people together to support one another in times of need. With Donation, users can make a positive impact on the lives of others while decluttering their own spaces.

Join us in spreading kindness and making a difference with the Donation feature on Greenpath.



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
*   OpenAI API (GPT-4)
*   OpenAI API (DALLE 3) 
*   OpenAI API (GPT4-V) 
  
