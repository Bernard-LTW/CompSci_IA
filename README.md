Bernard's IA: Recipe Sharing Website

<img src="Assets/DALLE_Flask.jpeg" style="zoom:50%;" />[^1]

[^1]: "APixar-style animation scene of a vibrant kitchen with a more intense and dramatic atmosphere. A woman is engrossed in her tablet, browsing through the RecipeShare app. Behind her, the oven erupts with a huge flame, the blender explodes sending its contents flying, and sparks fly from electrical outlets. The scene feels more chaotic, like a comedic action sequence. The title 'RecipeShare' is prominently displayed above, with the letters giving off a fiery glow. by DALL E 3, Open AI, Accessed 25th October 2023

## Criteria A: Planning

## Problem definition(Client identification)

My client is a housewife that really like cooking. She and her neighbours like sharing recipes with each other. However, they noticed that there is a lack of a platform to share their receipes. They tried using text messages but found it very hard to keep track of and hard to view. Not to mention, each family's receipes are for different amounts of people so it's very hard to accurate gauge how much ingredients is needed for multiple servings. Credibility is also a question my client noticed. (See evidence of consultation in Appendix 1)

## Proposed Solution

Considering the client's requirements, an adequate solution would be social-media styled website that can store data
inside a database. The most common tools for web development are Javascript, HTML, CSS[^8]but Javascript is a
client-side language, which means that code is executed on the user's browser. This can burden the client's computer with heavy tasks. To remedy this, Python would be an adequate programming language for more heavy tasks in the web application as it is not a client-side language, open sourced, mature and excels at memory management[^2]. As for the choice of web server framework, Flask would be an adequate choice as it is the scale of the website isn't so large that it requires more sophisticated frameworks like Django, making it fit to the client's need for a school use website without overcomplicating resources[^3][^9].For the database, SQLite would be a good fit as the data we are fitting is not very large and SQLite, with its embedded,serverless nature[^4], can reduce the use of computing resources while running the website, not to mention higher speeds. To interface with database, the SQLAlchemy is the prefered interface layer as it has performance advantages and is protected against security attacks such as SQL injections[^5]. As for the user interface for the website, Bootstrap 5 is recommended for its dynamic scaling abilities to scale automatically for different devices[^6].To keep the website and their users secure, JSON web tokens are used because they are resistant to security attacks[^7] and can prevent malicious users from modifying the key to access unauthorized content.

[^2]: Python Geeks. “Advantages of Python: Disadvantages of Python.” Python Geeks, 26 June 2021, https://pythongeeks.org/advantages-disadvantages-of-python
[^3]: “6 Reasons Why Flask Is Better Framework for Web Application Development.”*Able*, https://able.bio/hardikshah/6-reasons-why-flask-is-better-framework-for-web-application-development--cd398f73.
[^4]: S, Ravikiran A. “What Is Sqlite? And When to Use It?” *Simplilearn.com*, Simplilearn, 16 Feb.2023, https://www.simplilearn.com/tutorials/sql-tutorial/what-is-sqlite.
[^5]:  Uwase, Ange. “Here Is the Reason Why SQLAlchemy Is so Popular.” Medium, 8 Feb.2021,https://towardsdatascience.com/here-is-the-reason-why-sqlalchemy-is-so-popular-43b489d3fb00#:~:text=SQLAlchemy%20is%20the%20ORM%20of.
[^6]: Pratikasha Shinde. “6 Reasons to Use Bootstrap 5 for Better UI Development – Blog.” *Jade Global*, 6 Oct. 2021, https://www.jadeglobal.com/blog/6-reasons-use-bootstrap-5-better-ui-development.
[^7]: “What Is JWT?: Akana by Perforce.”*Akana*, https://www.akana.com/blog/what-is-jwt#:~:text=Why%20Use%20JWT%3F,was%20signed%20by%20the%20issuer.

[^8]: “11 Most in-Demand Programming Languages in 2023.” *Berkeley Boot Camps*, 5 Jan 2023, https://bootcamp.berkeley.edu/blog/most-in-demand-programming-languages/.
[^9]: “Flask vs Django: Let’s Choose Your next Python Framework.” Kinsta®, 13 Sept. 2023, kinsta.com/blog/flask-vs-django/#:~:text=Flask%20tends%20to%20be%20simpler,%2C%20demands%2C%20and%20existing%20requirements. Accessed 07 Dec. 2023. 

### Design statement

I will design a social media platform on a website built with Flask, Bootstrap, HTML, and CSS which stores data in an
SQLite database for me and my classmates. This website will allow my client and her neighbours to post receipes and ingredients of
them accordingly, with a comment system to provide feedback. It will take approximately 1 month to complete and
will be evaluated according to the criteria below:

## Success Criteria

1. The website must allow user registration for personal accounts secured*(Issue tackled: "Credibility is also a question my client noticed" and "found it very hard to keep track of")*
2. The website must allow for posting of recipes and their respective details *(Issue tackled: "there is a lack of a platform to share their receipes.")*
3. The webiste must allow for commenting on each recipe posted  *(Issue tackled: "very hard to keep track of")*
4. The website must allow for calculating the amount of ingredients needed based on the number of serving inputted by the user *(Issue tackled: "it's very hard to accurate gauge how much ingredients is needed for multiple servings.")*
5. The website would allow putting picture on each posted receipe*(Issue tackled:"They tried using text messages but found it very hard to keep track of and hard to view.")*
6. The website would allow searching for recipes with the ingredients *(Issue tackled:"They tried using text messages but found it very hard to keep track of and hard to view.")*
7. The website would allow for exporting the recipe to a PDF  *(Issue tackled: "very hard to keep track of")*

<div style="page-break-after: always"></div>

# Criteria B: Design

## System Diagram

![](Assets/SysD3.jpeg)

**Fig.1** *System diagram of the Website* This diagram shows the system design of the RecipeShare social media. This system design consists of two main parts. The first part is the flask server on top. In my case, I'm using a server running macOS. This server houses the flask application inside a Python virtual environment. This server also holds the SQLite database which is responsible for storing user data. The client, on the bottom, connects to the server on a browser through the internet with HTTP `GET` and `POST` requests. The user inputs data using the keyboard and trackpad or mouse and the output is displayed on the screen.

## Data Storage

<img src="Assets/RecipeShare_ER2.jpeg" style="zoom: 50%;" />

**Fig.2** *ER diagram of the Website* This diagram shows the relational database strcuture design for this social media. As users are the core of the service, every other database column has some form of connection back to the `User` table. In my design, the user writes `Recipes` and `Comments`. In which `Recipes` have `Ingredients` in them as the number of ingredients is unpredictable to the system and that would be the most logical way to normalize the database.

### Example of Data Entries

All data shown here are examples and does not reflect any real information for privacy purposes

<img src="Assets/RecipeShare_RecipeTablev2.jpg" alt="CodeShareDB_User" style="zoom: 67%;" />

**Fig.3** *Example of data entry in the Recipe table*

<img src="Assets/RecipeShare_UserTable.jpg" alt="CodeShareDB_User" style="zoom: 67%;" />

**Fig.4** *Example of data entry in the User table*

<img src="Assets/RecipeShare_CommentsTable.jpg" alt="CodeShareDB_User" style="zoom: 67%;" />

**Fig.5** *Example of data entry in the Comments table*

<img src="Assets/RecipeShare_IngredientsTable.jpg" alt="CodeShareDB_User" style="zoom: 67%;" />

**Fig.6** *Example of data entry in the Ingredients table*

## UML Diagram

![](Assets/RecipeShare_UMLv2.jpeg)

**Fig.7** *UML Diagram of the website* This diagram showcases the different classes I used to group together functions I use through the program. My classes are separated into two sections. One for interacting with the database(the part in green). And two for doing authentication management(the part in blue). This is utilizing the Object-Oriented Programming structure to reduce boilerplate code and provide a level of abstraction on the main server program.

## Wireframe

<img src="Assets/RecipeShare_Wireframe.jpg" style="zoom: 67%;" />

**Fig.7** *Wireframe of the website* This diagram showcases the preliminary design I had in mind after listening to the client's requests.

## Flow Diagrams

### Ingridients Storage into database

<img src="Assets/RecipeShare_IngridientStorage2.jpg" style="zoom: 25%;" />

**Fig.7** *Flow Diagram of process of storing ingredients into database* This diagram shows how the website handles a different number of ingredients each time a new recipe is added. 

### Serving Calculations

<img src="Assets/RecipeShare_FlowServingCalculations2.jpg" style="zoom:25%;" />

**Fig.8** *Flow Diagram of serving calculation* This flow diagram demonstrates the ability to calculate the ingredients according to the number of servings inputted by the user.

### File Uploads

<img src="Assets/RecipeShare_FileUpload.jpg" style="zoom:25%;" /> 

**Fig.9** *Flow diagram for handling file uploads* This flow diagram demonstrates how the system handles pictures uploaded by the user when they create a recipe

## Test Plan

| Type                | Description                | Process                                                      | Anticipated Outcome                                          |
| ------------------- | -------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| Unit Testing        | User Registration          | 1.Open Website<br/>2.Click on the register button<br/>3.Put "johndoe" as the username and "johndoelovescake" for both password fields<br/>4. Click the register button on the modal. | The modal should disappear and a flash message if stating that the user has been registered successfully. |
| Unit Testing        | User Login                 | 1.Open Website<br />2. Put "johndoe" as the username and "johndoelovescake" as the password<br />3. Click the login button on the login card | The user should be redirected to the dashboard page of the page if the user exists and the password matches the hash in the database. |
| Unit Testing        | Logout                     | 1.Open Website<br />2.Login using the same credentials as above<br />3.Click the log out button on the top bar | The user should be redirected back to the login screen and the session token should be removed from the session storage if checked using "Inspect" |
| Integration Testing | Login and Registration     | 1.Open Website<br />2.Follow the instructions for registering a user above<br />3. Follow the instructions for logging in above using the same credentials that was registered with<br /> | If the user followed the instructions properly and registered for a user, then the user should be able to login with the same credentials that were just registered with. |
| Unit Testing        | Adding new post            | 1.Open Website<br />2.Login<br />3.Click New Post on the header<br />4.Put in "Fried Eggs" as the title, "just put oil and crack the egg on the pan." as the Content and one egg as the ingredient.<br />5.Upload a random picture<br />6.Click the submit button | The user should be redirected to their own profile page, where they can see their own posts, including the one they just posted. |
| Unit Testing        | Commenting on a post       | 1.Open Website<br />2.Login<br />3.Click on a recipe button of a recipe<br />4. Write a comment saying "Cool!" and press "Post" | The user should be able to see the comment they just posted in the comment section of the recipe. |
| Unit Testing        | Serving Calculations       | 1.Open Website<br />2.Login<br />3.Click on a read more button of a recipe<br />4. Press the plus button on the servings calculator | The user should be able to see the amount of ingredients needed flucuate according to the number of servings chosen by te user. |
| Integration Testing | Adding Post / Viewing Post | 1.Open Website<br />2.Login<br />3.Create a new post following the instructions above<br />4.Click the home button | The user should be able to see the post they just created on the top of the dashboard. |
| Unit Testing        | Search System              | 1.Open Website<br />2.Login<br />3.Click the search button on the top bar<br />4.Put in "French" as the search keyword and press search | The user should be able to see a post with the keyword French in the title. |
| Unit Testing        | PDF Export                 | 1.Open Website<br />2.Login<br />3.Click on a post<br />4.Click the "Print Recipe" button<br />5.Save as PDF using the popped up dialog | The user should be able to download a pdf of the opened recipe |
| Code Review         | Reviewing Code             | Going through the code and making sure unused parts are removed, variables are named properly and comments are placed appropriated | Easy to understand and easy to debug code for future development. |

<div style="page-break-after: always"></div>

## Record of Tasks

| Task No | Planned Action                                               | Planned Outcome                                              | Time estimate | Target completion date | Criterion |
| ------- | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------- | ---------------------- | --------- |
| 1       | Planning: First Meeting with client                          | Start collecting the context of the problem and research on current solutions | 3 min         | 2023-08-28             | A         |
| 2       | Planning: Defining problem                                   | Start on refining client's requirements and tools needed     | 1 hr          | 2023-08-29             | A         |
| 3       | Planning: Writing proposed solution and design statement     | Write about product being developed and why particular choices were made. | 30 min        | 2023-08-30             | A         |
| 4       | Planning : Second Meeting with client                        | Decided success criteria(See Appendix 2)                     | 20 min        | 2023-08-31             | A         |
| 5       | Planning: Drawing the system diagram                         | To have a clear idea of the hardware equipment needed for development | 45 min        | 2023-09-01             | A         |
| 6       | Planning: Researching about JS in HTML                       | To have a clear idea of how JS can be used to make HTML dyanmic | 1 hr          | 2023-09-01             | A         |
| 7       | Planning: Researching about SQLAlchemy                       | To have a clear idea of how SQLAlcehmy can be used in my project to interact with databases in a more organized way | 20 min        | 2023-09-02             | A         |
| 8       | Planning: Researching about flask file uploads               | To have an idea of how flask can be used to handle file uploads | 40 min        | 2023-09-03             | A         |
| 9       | Planning: Creating Wireframe                                 | To have Wireframe diagram finished                           | 1 hr          | 2023-09-04             | B         |
| 10      | Planning: Create ER diagram                                  | To have the structure of the database drawn out              | 30 min        | 2023-09-05             | B         |
| 11      | Planning: Third Meeting with client                          | To obtain approval from client to start development          | 5 min         | 2023-09-06             | A         |
| 12      | Initializing codebase                                        | To have the base environment of program ready for coding     | 1 hr          | 2023-09-07             | B         |
| 13      | Development: Setting up Flask application                    | To have set up a basic flask application                     | 20 min        | 2023-09-10             | C         |
| 14      | Development: Coding the structure of the database            | Finalize on the structure of the database                    | 10min         | 2023-09-10             | C         |
| 15      | Development: Initializing db_manager                         | To have a base for the database handler coded and ready for new functions to be coded on top | 10min         | 2023-09-11             | C         |
| 16      | Development: Coding basic endpoints                          | To have basic endpoints coded                                | 15min         | 2023-09-12             | C         |
| 17      | Development: Coding the token manager                        | To have the JWT system implement as a base for my flask application | 45min         | 2023-09-13             | C         |
| 18      | Development: Fixing error for JWT Timeout                    | Fixed error where JWT tokens will still work even after timeout | 2 hr          | 2023-09-14             | C         |
| 19      | Development: Coding the Login/Registration backend           | To have the backend database logics implemented for the user management | 20min         | 2023-09-15             | C         |
| 20      | Development: Retooling database structure details            | Retooled database structure to include details like unique attributes and more. | 30 min        | 2023-09-16             | C         |
| 21      | Development: Coding the login page                           | To design the login page for the website, complete with the registration function as well | 1hr           | 2023-09-17             | C         |
| 22      | Development: Coding Header/Footer                            | To have the header/footer of the website designed and coded  | 20 min        | 2023-09-18             | C         |
| 23      | Development: Coding Dashboard                                | To have the layout of the dashboard page coded               | 30 min        | 2023-09-19             | C         |
| 24      | Development: Finalizing theme of website                     | To have a consistent theme for the website                   | 30 min        | 2023-09-20             | C         |
| 25      | Development: Cosolidating header/footer into template        | To have a base template for all other pages to use in a way that avoids boilerplate code | 20 min        | 2023-09-21             | C         |
| 26      | Development: Coding New Recipe Page                          | To have the layout of the new recipe page coded              | 30 min        | 2023-09-22             | C         |
| 27      | Development: Coding New Recipe Page                          | To have the layout of the new recipe page finalised          | 1 hr          | 2023-09-23             | C         |
| 28      | Developing: Coding ingredients mechanism for new recipe page | Created system that allows dyanmic adding/subtracting from the HTML used to store the ingredients | 2 hr          | 2023-09-24             | C         |
| 29      | Development: Coding My Profile                               | To have the layout of the my profile page coded              | 30min         | 2023-09-25             | C         |
| 30      | Development: Coding logic for Dashboard                      | To have the dashboard page connected to the database logic   | 45min         | 2023-09-27             | C         |
| 31      | Development: Coding logic for New Post                       | To have the new post page connected to the database logic    | 45min         | 2023-09-28             | C         |
| 32      | Planning: Research about secure file uploads                 | To have a clear idea of how to make file uploads safer in Flask | 1 hr          | 2023-09-29             | B         |
| 33      | Development: Coding the secure logic for validating file uploads | Implemented the logic to detect malicious file extension     | 30 min        | 2023-09-30             | C         |
| 34      | Development: Coding file storage                             | Wrote the python code to handle file saving onto the server  | 50 min        | 2023-09-31             | C         |
| 35      | Development: Fixing issue of not being able to retreive files | Fixed the issue of not being able to retreive uploaded files. | 20 min        | 2023-10-01             | C         |
| 36      | Development: Coding logic for My Profile                     | To have the my profile page connected to the database logic  | 45min         | 2023-10-02             | C         |
| 37      | Development: Coding recipe details page layout               | To have the layout for the recipe details page coded         | 30 min        | 2023-10-03             | C         |
| 38      | Development: Coding logic for recipe details page            | To have the logic for the recipe details page coded          | 1 hr          | 2023-10-04             | C         |
| 39      | Development: Coding logic for serving counter                | To have the logic for the servings counter started           | 30 min        | 2023-10-05             | C         |
| 40      | Planning: Researching JS syntax                              | To obtain a clearer idea of how to code in JS                | 30 min        | 2023-10-06             | C         |
| 41      | Development: Coding logic for serving counter                | To have the logic for the servings counter finalised         | 30 min        | 2023-10-07             | C         |
| 42      | Development: Coding comments layout                          | To have the layout of the comments sections designed and coded | 30 min        | 2023-10-08             | C         |
| 43      | Development: Coding endpoints for comments                   | To have the necessary endpoints for handling comments coded  | 30 min        | 2023-10--09            | C         |
| 44      | Development: Retooling database relationships for comments   | Fixed One-to-many relationship in database in order to handle data storage more effectively | 30 min        | 2023-10-10             | C         |
| 45      | Development: Fixing bug for flash messages                   | Fixed issue where flash messages weren't showing on the dashboard | 30 min        | 2023-10-11             | C         |
| 46      | Development: Consolidating repeating code                    | Put together repeating code into functions                   | 30 min        | 2023-10-12             | C         |
| 47      | Development: Renaming variables                              | Improved readability for future extension                    | 30 min        | 2023-10-13             | C         |
| 48      | Development: Search Function                                 | To code the html page for the search page                    | 30 min        | 2023-10-14             | C         |
| 49      | Development: Search Function                                 | To have the endpoint for the search page coded               | 20min         | 2023-10-15             | C         |
| 50      | Planning: Researching SQLAlcehmy                             | To have an idea of what function to use for searching        | 20min         | 2023-10-16             | A         |
| 51      | Development: Search Function                                 | To have the search function coded and working                | 20min         | 2023-10-17             | C         |
| 52      | Planning: Research about PDF rendering libraries             | To have an idea of how to render pdfs from HTML              | 60min         | 2023-10-18             | A         |
| 53      | Development: PDF Export function                             | To have the endpoints for the pdf exports coded              | 30min         | 2023-10-19             | C         |
| 54      | Planning: Research about client-side JS functions            | To have an idea of alternate options for exporting to pdf    | 20min         | 2023-10-20             | C         |
| 55      | Development:  PDF Export function                            | To have the function coded and working                       | 20min         | 2023-10-21             | C         |
| 56      | Planning: Creating UML Diagram                               | To have understanding of the different parts of the code     | 30min         | 2023-10-23             | B         |
| 57      | Planning: Creating Flow Diagrams                             | To have a clear understanding of difficult parts of code     | 1hr           | 2023-10-24             | B         |
| 58      | Development: Cleaning up Code                                | To have the code finalized and organized for easy-understanding | 10min         | 2023-10-25             | C         |
| 59      | Development: Cleaning up Code                                | To have the code finalized and organized for easy-understanding | 30 min        | 2023-10-26             | C         |
| 60      | Planning: Creating Test Plan                                 | To have a test plan created for confirming if the application works to standard | 30min         | 2023-10-27             | B         |
| 61      | Planning: Finalizing Test Plan                               | To have the test plan finalized                              | 30 min        | 2023-10-28             | B         |
| 62      | Implementation: Evaluation by client                         | To have the website evaluated by the client and the subsequent evidence documented | 1hr           |                        | E         |
| 63      | Beta Testing: Evaluation by peer                             | To have the website evaluated by a peer and the subsequent evidence documented | 1hr           |                        | E         |
| 64      | Implementation: Collect Recommendations from users/client    | To have taken in recommendations from both evaluations on how the website can be improved and document them properly | 15min         |                        | E         |

<div style="page-break-after: always"></div>

# Criteria C: Development

## Existing Tools

| Libraries    |
| ------------ |
| flask        |
| json         |
| os           |
| Datetime     |
| sqlalchemy   |
| passlib.hash |
| dotenv       |
| Python-jose  |

## References

### [Bootstrap 5 Documentation](https://getbootstrap.com/docs/5.3/getting-started/introduction/)

Bootstrap 5's official documentation is what I referenced regarding UI elements of my website.
Snippets of code for modals, cards, headers and footer have been taken from the documentation and have been since modified to fit the needs of the current application

### [ChatGPT](https://chat.openai.com)

ChatGPT is a large language model developed by OpenAI, based on the GPT (Generative Pre-trained Transformer)
architecture. It helps me with logics in code and pseudocode for parts like HTML, JavaScript and JWT tokens.

***Disclaimer*** *No part of this program includes code blocks directly copied from ChatGPT*

#### Example use of ChatGPT

![](Assets/ChatGPTUse.jpg)

**Fig.10**  *Conversation with ChatGPT screenshotted on 2023-10-26*

## List of Techniques

1. Object-Oriented Programming(OOP)
2. Object Relation Mapping(ORM): SQLAlchemy
3. Flask Library/Routes
4. Javascript/Python inside HTML
5. CSS Styling
6. For loops for showing posts
7. if statements
8. Password Hashing
9. Token-based authentication
10. Interacting with Databases
11. Arrays and Lists
12. Text Formatting
14. DRY Programming Technique

## Development

### JSON Web Tokens (Success Criteria #1)

One of the success criteria was to have a hashed login system. One issue I had after the user logged in which was that I could not recognize the user after the initial login process. One Idea I had was to use cookies to store the user id. It can be easily retreived by the backend when needed and takes up little system resources. However, I realized after wards that cookies can be easily modified on the client's side and render the hashed passwords useless. Soon I discovered session tokens. Session token are basically a hash created when the user successfully logs in and is the pass the user holds to perform previleged actions on the website. They expire after a time designated by the developer and can be used to protect the user as it is hashed using a special secret key that only the developer has control over. Currently, once the user successfully logs in with the right username and password. The main function on the flask endpoint executes a `create_token` function from the `token_management.py`. The token is created as follows:

```py
# This functions takes in the username and the how long the token should last in minutes
def create_token(username, token_duration):
    # This adjusts the starting time of counting the token expiry to keep consistency across different platforms
    unix_timestamp = (datetime.now() - datetime(1970, 1, 1)).total_seconds()
    # This line sets the expiry time of the token
    ttl = token_duration * 60 + unix_timestamp
    # token format = encoded(username, datetime) token_duration in minutes
    token = jwt.encode({'username': username, 'datetime': ttl}, token_encryption_key, algorithm='HS256')
    # Token is returned to the main flask function
    return token
```

After the main function receives the token from the `create_token` function, its gives the token back to the client by
putting it into the session variable of the browser as follows:

```py
session['token'] = create_token(username, 120)
```

Now, the user holds the token in their browser. When they want to execute an action, the backend tries to get the token
from the browser as follows:

```py
@app.route("/recipe/<int:recipe_id>")
def recipe(recipe_id):
    # Check if the token exists in the session
    token = session.get('token')
    if token and check_token(token):
        #Continues Function
    else:
      #If either the token doesnt exist or it is expired when checked against the key, the user is returned to the login screen.
    	return redirect(url_for('login'))
```

On the code above, I used the `try` statement to handle `KeyError` in the instance that the JWT is not present in the
user's browser and redirects them to the login page. If the token is present, the validity of it is checked using
a `check_token` function. It decodes the token and checks if the expiry time has exceeded current time as follows:

```py
def check_token(token): # check if token is valid and not expired
    try:
        # Decodes token using predefined key and algorithm
        decoded_token = jwt.decode(token, token_encryption_key, algorithms=['HS256'])
        current_time = datetime.utcnow().timestamp()
        # Compares expiry time and current time
        if decoded_token['datetime'] < current_time:
            return False
        else:
            return True
    except Exception:
        return False
```

The main function then receives a boolean value of whether the user is valid in an active session and lets them proceed with the desired action accordingly. This system closes the loophole of modifying cookies and completes the hashed authentication system criteria.

### Base Template(Pattern Recognition/Generalization/Abstraction)

As the header and footer needs to be present in every single page, it creates a lot of repetition and boilerplate code in my program. Boilerplate code is referring to parts of code that has to be repeatedly be used with no or a little modification. This is especially present in HTML as it is declarative language. If the code for the header and footer is repeated every time a new page is needed, it would make my code very repetitive and make it hard when I have to change one thing in the header or the footer as I have to change it in every file seperately. Thus, I decided to used a template file, where the header and footer is housed inside one file only, and other files extends from this base file to add their own respective content. The base file starts out like a normal html file with the necessary scripts and CSS files imported, but in the main body, only one line is added:

```html
{% block content%}{% endblock %}
```

This line opens up a variable called `content` in the base template. On the other files, it is indicated on the first
line that the file is extending the base file:

```html
{% extends "base_template.html" %}
```

After that the child file can add content into the variable with the same line:

```html
{% block content%}
{# Normal HTML for the main body of the page. Omitted here because of length#}
{% endblock %}
```

When this html file is loaded on the browser, the base file is taken and the variables from the child file is being stitched together automatically into one single HTML file. That way, if I need to change anything on the header/footer or change out dependencies, I only need to change it once and it will spread across all pages, improving efficiency and future development upgradibility.

### Ingredients Storage(Success Criteria #2)

My client needed to be able to post recipes and their respective details in an organized way. While designing the system for that, I noticed a problem. That is that there would only be one column for ingredients inside the table but there would be a different number of ingredients inputted by the user. To resolve this, I could take two approaches, one is JSON string. A JSON string is a string representation of a JSON data structure. It's very universal and is language dependent which means that it will be able to work easily with any programming language. However, storing a JSON string inside a relational database like SQLite is not very efficient as we would be building a database with in a column of the database. Thus, the more resonable approach to this would be to use another table of the database with relation back to the `Recipes` table.

![](Assets/JS_Showcase.jpg)

**Fig.11**  *Screenshot showing the section for inputting ingredients*

In my implementation, on the client side, they are able to easily add text fields to the form they are typing in. This is achieved through JS on the client side.

```javascript
document.getElementById('addInputBtn').addEventListener('click', function () {
    //Code omitted for defining the UI elements
    // Add the input, dropdown, and remove button to the new div
    newDiv.appendChild(newInput);
    newDiv.appendChild(newInput2);
    newDiv.appendChild(newDropdown);
    newDiv.appendChild(removeBtn);
    // Add the new div to the form
    document.getElementById('newInputs').appendChild(newDiv);
});
```

When the user clicks the `Add Item` button, it triggers the javascript to create a new set of elements for a new ingridient. When the user clicks the `delete` button, it removes the set of elements from the HTML. Allowing the user to dynamically adjust the form to the needs of their recipe.

When a user submits a form, it is done through a `POST` request. The flask application then collects the information for the ingredients' name, amount and unit separately and zips them into a list along with collecting other information for the form as shown below:

```py
if request.method == 'POST':
    title = request.form.get('title')
    content = request.form.get('content')
    #Ingredients' names, amounts, and units are collected separately
    ingredient_names = request.form.getlist('ingredient_name[]')
    ingredient_amounts = request.form.getlist('ingredient_amount[]')
    ingredient_units = request.form.getlist('ingredient_unit[]')
		#All three elements are zipped into a list.
    ingredients = zip(ingredient_names, ingredient_amounts, ingredient_units)
```

After collecting the raw information from the user, the zipped list is put into dictionary as shown below

```python
ingredients_dict_list = [
                {
                    "name": ingredient_name,
                    "amount": ingredient_amount,
                    "unit": need_description
                }
                for ingredient_name, ingredient_amount, need_description in ingredients
            ]
```

The dictionary is then passed through to the `create_post` function in the database handler class. This function firsts creates the recipe by doing:

```python
#Creates new Recipe object
new_post = Recipe(name=title, content=content, image=unique_filename, user_id=user_id)
#Add the newly created object to the already-opened session
self.session.add(new_post)
#Commit the changes
self.session.commit()
```

Notice that we haven't passed through the ingredients but we have commited the changes already. That is because the ingredients require the recipe `id` as a foreign key so we cannot commit the changes at the same time as we would not know what `id` would be assigned to that recipe before commiting the changes. Thus after this, a for loop is used to loop through each item in the dictionary to add them to the database:

```python
for ingredient in ingredients_dictionary:
  new_ingredient = Ingredients(name=ingredient["name"], amount=ingredient["amount"], unit=ingredient["unit"], recipe_id=new_post.id)
  self.session.add(new_ingredient)
```

After this we do another commit to the database using 

```python
self.session.commit()
```

When it comes time to retrieve the data, or that is to say, when the user clicks on the `Read More` button on the dashboard, the server requests the `recipe` by id. Which then the database handler queries the database for the recipe and the ingredients separately:

```python
#Database handler receives id as input
def get_one_post(self, id):
  	#Recipe table is queried by id
    recipe =  self.session.query(Recipe).filter_by(id=id).first()
    #Ingredients table is queried by id
    ingredients = self.session.query(Ingredients).filter_by(recipe_id=id).all()
    #List is returned with username of poster as well as the other information being queried
    return [recipe,self.session.query(Users).filter_by(id=temp.user_id).first().username,ingredients]
```

The flask application then passes the list to the html file and the `jinja2` logic creates the ingridients by column automatically as shown below.

![](Assets/ingredients_eg.jpg)

**Fig.12**  *Screenshot showing the ingredients part when a user loads up a recipe*

### Commenting System(Success Criteria #3)

My client specifically requested for the ability to comment on recipes. To achieve that, I used a separate table on the database with a foreign key that links back to the recipe. As a recipe is represented in the way of a card, I added the comments section to the footer of the card with the `card-footer`class as shown below:

```html
<div class="card-footer">
  <div class="comments-section">
      <h4>Comments</h4>
      {% if comments %}
          <ul class="list-group">
          {% for comment in comments %}
					<!--Code Omitted for demonstrative purpose-->
          {% endfor %}
      {% else %}
          <p>No comments yet.</p>
      {% endif %}
      </ul>
  </div>
  <div class="add-comment-form">
<!--Code Omitted for demonstrative purpose-->
  </div>
</div>
```

As you can see, when the recipe is loaded,the database is queried for comments with the same id as the recipe for the foreign key. After the results of that query is passed through to the HTML, I used jinja2's loop function to create a section for each comment made, showing the author and the content of the comment.

![](Assets/Comments.jpg)

**Fig.13**  *Screenshot showing the section for comments*

To post a comment, the user would put the comment in the textbox above and press `Post Comment`. That will trigger a form submission into the flask application and it would be processed with a function. 

```python
def add_comment(recipe_id):
    #Collects session token from browser
    token = session.get('token')
    #Checks token validity
    if token and check_token(token):
      #Unpacks token
        username = get_username_from_token(token)
        #Collects form input
        comment_content = request.form.get('comment_content')
        #Passes through information to database handler
        db.add_comment_to_recipe(recipe_id, username, comment_content)
        return redirect(url_for('recipe', recipe_id=recipe_id))
    return redirect(url_for('login'))
```



Inside the first omitted section in the HTML I also included an if statement to check if the logged in user is the user who wrote the comment, and if so, include a delete button for the user to be able to delete their comment. The delete button is an endpoint on the flask application called `/recipe/<int:recipe_id>/delete_comment/<int:comment_id>/` ,It handles the removal of comments on the Python side by the code same as above but with one different line:

```python
db.remove_comment(recipe_id, comment_id, username)
```

This line calls back to the database handler to remove the selected comment from the database and completes the success criteria.

### Serving Calculations(Success Criteria #4)

My client also requested for the ability to calculate the amounts of ingredients needed to make the number of servings inputted by the user. As when the recipe is created, the user is asked to input the ingredients in a systematic manner as seen in **Fig.11**, calculating the amount of ingredients needed for `x` serving should be as simple as multiplying the dataset we have stored in the database by `x`. This could be achieved in two ways. One way is to use a hyperlink to a flask endpoint which receives the recipe id and does the calculations in Python. This mean that each time a user increments the servings counter by 1, the whole html file would need to be reloaded and rendered from the server. This is very ineffiecient as we are only trying to change a few values on the HTML file and reloading the whole HTML would cost much more bandwidth and decrease responsiveness of the website. Becasue of this reason, I chose to use Javascript on the HTML. This would make the calculations local on the client's browser, eliminating the need of calling back to the main server to get a multiplication done. To achieve this, I first created a counter object in HTML as shown below:

![](Assets/ServingCounter.jpg)

**Fig.14**  *Screenshot showing the counter for adjusting the number of servings*

This counter above is created by using the `input_group` class in Bootstrap to group the buttons and the text display together as shown:

```html
<div class="input-group mb-3" style="width: 200px">
    <button class="btn btn-secondary" type="button" id="minusButton">-</button>
    <input type="text" id="servingInput" value="1" readonly
           class="form-control text-center">
    <button class="btn btn-secondary" type="button" id="plusButton">+</button>
</div>
```

As seen, the first line defines the holder for group of elements, followed by the buttons and text fields being defined. These buttons are handled by a javascript function. This function first defines three internal variables to collect information from the form.

```javascript
const servingInput = document.getElementById('servingInput');
const minusButton = document.getElementById('minusButton');
const plusButton = document.getElementById('plusButton');
```

These three lines define variables to allow the javascript to interact with the data in HTML. After defining the variables that allow the JavaScript to interact with the data in the HTML, the script continues by creating the `updateIngredients()` function. This function is the core of our interactive serving size feature.

```javascript
// This function updates the displayed ingredient amounts
function updateIngredients() {
    // Parses the serving size entered by the user as an integer
    const servings = parseInt(servingInput.value, 10);
    // Selects all ingredient list items and loops over them
    document.querySelectorAll('#ingredientList li').forEach(function (ingredientItem) {
        // Retrieves the base amount of the ingredient from the 'data-amount' attribute and converts it to a float
        const baseAmount = parseFloat(ingredientItem.getAttribute('data-amount'));
        // Retrieves the unit of measurement for the ingredient from the 'data-unit' attribute
        const unit = ingredientItem.getAttribute('data-unit');
        // Calculates the new amount needed for the specified number of servings
        const newAmount = baseAmount * servings;
        // Updates the text content of the ingredient amount on the page, rounding to two decimal places
        ingredientItem.querySelector('.ingredientAmount').textContent = newAmount.toFixed(2) + ' ' + unit;
    });
}
```

This function is called whenever there is a need to update the ingredient amounts. It is wired to respond to user interactions with the serving size counter. Continuing with the event listeners:

```javascript
// Event listener for the minus button
minusButton.addEventListener('click', function () {
    // Get the current value from the serving input as an integer
    const currentValue = parseInt(servingInput.value, 10);
    // Check if the current value is greater than the minimum allowed servings (1 in this case)
    if (currentValue > 1) {
        // Decrement the serving count
        servingInput.value = currentValue - 1;
        // Update the ingredient amounts to reflect the new number of servings
        updateIngredients();
    }
});
//Code for the plus button event listener is omitted because of similarity
```

These event listeners monitor clicks on the minus and plus buttons. When the minus button is clicked, it checks if the serving size is above the minimum and, if so, decreases the serving count and updates the ingredient amounts. Conversely, when the plus button is clicked, it simply increments the serving count and then updates the ingredient amounts.

By using these JavaScript functions and event listeners, users can dynamically adjust the servings they wish to prepare, and the ingredient amounts will automatically update to match. This enhances the interactivity of the webpage by providing immediate feedback right in the browser without any need for server-side processing or full page refreshes. This not only improves the responsiveness of the application but also conserves bandwidth and server resources, creating a smoother and more efficient user experience.

### Pictures on Recipes/File Uploads(Success Criteria #5)

One of the key functions my client mentioned was the capability for users to upload images of their culinary creations. Images are a vital aspect of sharing recipes, providing a preview of what the finished dish should look like. To achieve this feature, a few essential components were integrated into the server's flask application.

The initial setup involves specifying the directory where all the uploaded images will be stored, which is a folder named 'uploads'. To ensure that the server only accepts image files, a set of allowed extensions is declared—'png', 'jpg', 'jpeg', and 'gif'. The Flask app is then configured to reference this upload folder:

```python
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
```

Furthermore, to reliably handle the file path regardless of the operating system, we use `os.path` functions to construct an absolute path to the uploads directory:

```python
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
UPLOADS_PATH = os.path.join(BASE_DIR, 'uploads')
```

The next step in the process is the implementation of a small but crucial function, `allowed_file`. This function serves as a gatekeeper, determining if the uploaded file's extension is within our defined set of permitted file types in order to prevent users from uploading malicious files:

```python
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
```

This function first checks if a file extension in present. If a file extension is present, it will be extracted in the second part of the return function and checked against the list of `ALLOWED_EXTENSIONS`. If both conditions are met, then the fucntion would return TRUE. With the preparatory work in place, the logic for handling an uploaded image is straightforward. When a file is received through the user's submission:

```python
uploaded_file = request.files.get('uploaded_image')
```

It undergoes a series of checks—firstly, to ascertain that there is indeed a file and that it has a filename, then to validate the file type using our `allowed_file` function. If these checks are passed, the file is saved with a unique timestamped filename to avoid overwriting any existing files:

```python
if uploaded_file and uploaded_file.filename != '':
    if allowed_file(uploaded_file.filename):
        # Generate unique filename using timestamp
        unique_filename = f"{int(time.time())}_{uploaded_file.filename}"
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], unique_filename)
        uploaded_file.save(filepath)
        print(f"Image saved as: {filepath}")
    else:
        print("Invalid file type.")
        return "Invalid file type.", 400
else:
    unique_filename = "No file"
```

The last part is incorporating this filename into the database entry for the new recipe post, ensuring that the image can be referenced and displayed alongside the recipe content. When a user loads the dashboard or a specific recipe, the browser will request the image from the `/uploads/` endpoint. To handle this, a flask endpoint is in place to serve the images from their absolute paths to the browser:

```python
@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(UPLOADS_PATH, filename)
```

This allows easy loading of the pictures uploaded and completes the success criteria.

### Search Function(Success Criteria #6)

My client wanted search functionality for their recipe-sharing platform. This feature is designed to be straightforward for the end-user to be able to easily find the recipe they're looking for. To initiate a search, the user would click the `Search` button on the header of the webpage. There, a search box would appear on a new page. The user would enter their keyword for query and click `Search` again to submit their query. The backend handles this input using the following Flask route:

```python
if request.method == 'POST':
    search_query = request.form.get('search_query')
    posts = db.search(search_query)
    return render_template('search.html', username=username, search_results=posts)
```

This code snippet shows how the server processes a search request. When the search form is submitted, the website makes a POST request, signifying that the user is initiating a new search. Within this request, the user's search input, referred to as `search_query`, is retrieved from the form data. After that, the search query is passed on to a method called `search` within the database management class `db_manager`. This function interacts with the underlying SQL Database using SQLAlchemy. The code is as follows:

```python
def search(self, search_query):
    # This line queries the Recipe table, using a LIKE SQL clause to find matches
    temp = self.session.query(Recipe).filter(Recipe.name.like("%"+search_query+"%")).all()
    posts = []
    # Looping through each matched recipe
    for post in temp:
        # Appending a combination of recipe information and the username of the poster
        posts.append([post, self.session.query(Users).filter_by(id=post.user_id).first().username])
    return posts
```

In this function, a SQL query is formulated to look for any recipe names that contain the user's search term.  The user's search term is encapsulated with percentage symbols(%), which means wildcards in SQL. The result is a collection of recipe that matches the search criterias.

For each recipe found, there's an additional step of fetching the username of the person who posted the recipe. This is achieved by querying the `Users` table for the `user_id` associated with each recipe. The result is a list of posts, each including the recipe and the corresponding username. 

Finally, the list of search results is passed back to the Flask route, which then calls render_template to generate the HTML output. The search results are neatly packaged into a context dictionary that the search.html template uses to display the information on the web page.

### PDF Downloads(Success Criteria #7)

My client wanted the ability to download recipe as PDFs. This function allows the end-user to be able to download and print out the pdf for the specific recipe and serving size without having to log into the website everytime and checking. This is done by a rendering engine in the server. First and foremost, there is definitely a download button on the recipe page. 

```html
<a href="/recipe/download/{{ recipe.id }}/"><button class="btn btn-primary" type="button" id="downloadRecipe">Download Recipe</button></a>
```

I started out developing this button to link back to a donwload endpoint, where the function receives the recipe id from request. It would then render the according to recipe data from database. This is the code:

```python
#Function definition and token authentication is omitted for demonstrative purposes
#Renders template file with Flask and jinja2 engine
rendered = render_template('recipe.html')
#Uses WeasyPrint Libray to put rendered html into pdf
pdf = HTML(string=rendered).write_pdf()
#Constructing pdf into a response
response = make_response(pdf)
#Setting parameters for response
response.headers['Content-Type'] = 'application/pdf'
response.headers['Content-Disposition'] = 'attachment; filename=output.pdf'
#Send the response
return response
```

However this has one issue. It is not able to render the amount of servings accordingly. To address this issues, I tried multiple methods of form submission and `POST` requests but all to no avail, some failed to render correctly, while others threw errors such as not being able to find certain resources. In light of this, I resorted to use client-side javascript to tell the client's browser to print the screen with the following code:

```html
<button class="btn btn-primary" type="button" onclick="window.print()">Print Recipe</button>
```

When this button is clicked, the javascript calls back to the window object of the webpage and uses the `print()` function inside that object to trigger the browser to print the page with the printing dialog. This allows the client to turn their current viewing recipe into a pdf without reaching out to the server once more while also preserving the servings counter for the desired number of servings.

<div style="page-break-after: always"></div>

# Criteria D: Functionality

## Demonstration Video

[Click here for the Video](https://drive.google.com/drive/folders/1JOyAGobjKdZ32JniPXS8psKatWZlygEW?usp=drive_link)

<div style="page-break-after: always"></div>

# Criteria E: Evaluation

## Evaluation by Client

| Success Criteria                                             | Met? | Description                                                  |
| ------------------------------------------------------------ | ---- | ------------------------------------------------------------ |
| The website must allow user registration for personal accounts secured with a token system | Yes  | Users are secured behind a hashed login system and token system |
| The website must allow for posting of recipes and their respective details | Yes  | The website allows for posting new content via the `new_post/` endpoint |
| The website must allow for commenting on each recipe posted  | Yes  | This website allows for commenting on each recipe with the comments section under each post and the `add_comment` endpoint |
| The website must allow for calculating the amount of ingredients needed based on the number of serving inputted by the user | Yes  | The website allows for calculating the amount based on the inputted number with client-side Javascript |
| The website must allow putting picture on each posted recipe | Yes  | The website allows for posting pictrues alongside posts with the `add_post` endpoint |
| The website must allow searching for recipes                 | Yes  | The website allows for search through the social media a dedicated `/search` page |
| The website must allow for exporting the recipe in PDF form  | Yes  | The website allows for exporting to PDF using client-side Javascript |

The client is very satisfied by the product(See Appendix 3), with the website meeting all the success criteria. During
beta testing, the client suggested to add a confirmation dialog for deleting posts to eliminate accidental deletion (See
Appendix 5)and that has been implemented as well. One possible improvement highlighted by the client is that one person
is limited to one like or dislike in order to prevent people from spamming the like button, removing authenticity from
the rating.

## Evaluation by Peer

My peer is very satisfied by the product(See Appendix 4), with the website meeting all the success criteria.
One possible improvement highlighted by my peer was the ability
to filter through code by the code language on the home page
as that would make it easier to sort through what they are looking for.

## Extensibility

The client was very satisfied with the final result, as it met all of his requirements. After some additional discussion,
we concluded that the following future extensions could be added:



<div style="page-break-after: always"></div>


# Appendix

![](Assets/Appendix1.jpg)

**Appendix.1** *Rough notes from first meeting with client, includes basic ideas behind problem with current solution*

![](Assets/SuccessCriteriaConfirm2.jpg)

**Appendix.2** *Contact between developer and client approving success criteria*

![](/Users/bernardlee/PycharmProjects/IA_Kivy/Assets/ClientEvaluation.jpg)

**Appendix.3** *Contact between developer and client for evaluation of website*

![](/Users/bernardlee/PycharmProjects/IA_Kivy/Assets/PeerEvaluation2.jpg)

**Appendix.4** *Contact between developer and a peer for evaluation of website*

![](/Users/bernardlee/PycharmProjects/IA_Kivy/Assets/ClientBeta.jpg)

**Appendix.5** *Contact between developer and client regarding beta testing and feedback* 