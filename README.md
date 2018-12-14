# Veronique's Full Stack Project **Creature Comforts**
### Code Institute Full Stack Milestone Project

**Creature Comforts** is a small business venture that aims to bring happiness via well-thought, bespoke boxes.
By offering boxes filled with goods chosen with care, we wish to instill hygge (well-being) via SCENT, LIGHT, TEXTURE AND TASTE.
Our customers' daily routine can be uplifted by simple actions that are triggered or inspired by the content of the Creature Comforts boxes.
Those boxes can be purchase online and will be delivered at regular intervals following the frequency advertised (twice-yearly, every 3 months, etc.). 
Since the purpose of Creature Comforts is to help our customers maintain a cosy, happy mindset, we also offer a blog on our website to facilitate the connection of like-minded visitors 
and the exchange of ideas over various topics. 

## UX and UI
- [Original Wireframe](./planning/creaturecomforts.png)
- [Planning](./planning/userstories_creaturecomforts.xlsx)

 - Usage of specific colours in this project (psychology):
    - [Color in Design: Influence on Users' Actions](https://tubikstudio.com/color-in-design-influence-on-users-actions/)
    - [Color Theory Brief](https://uxplanet.org/color-theory-brief-guide-for-designers-76e11c57eaa)
    
- User stories
    - Personas: [Meet our Users!](./planning/USERS_STORIES.jpg?raw=true)
 
| As a [persona] | I want to [do something]                                                                             | so that I can [realize a reward]                                                               |
|----------------|------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------|
| **Persona**    | **Goal**                                                                                                 | **Result / Goal**                                                                          |
| :woman: Camille| wants to use her smartphone to go on the internet and visit Creature Comforts                        | since she always accesses websites on the go.                                                  |
|                | wants to try the trendiest boxes of Creature Comforts                                                | so she can interact with other people online with the same interests.                          |
|                | wants to see what previous customers think of their purchase                                         | so she can decide which item or option she likes best                                          |
|                | wants to send her comments and feedback easily                                                       | so she can get in touch with the webmaster if there is a problem with her browsing experience. |
|                | wants to see the list of all products in CC's shop, their prices and frequency                       | so she can decide which one she wants to buy.                                                  |
|                |                                                                                                      |                                                                                                |
|  :older_man: Harry          | wants to browse Creature Comforts' website without having to log in                                  | so he does not have to remember a password or username.                           |
|                | wants to visit the website's products by using categories or a search function                       | to find what he really wants to purchase.                                                      |
|                | wants to send messages to the webmaster without leaving Creature Comforts' website                   | so he does not forget to send the message and remembers what he wants to say.                  |
|                | wants to be able to access the Creature Comforts' website on his iMac                                | so he can shop online using his computer at home.                                              |
|                | wants to view the profiles of other members on Creature Comforts' blog                               | so that he can find others he might want to connect with.                                      |
|                |                                                                                                      |                                                                                                |
| :boy: Mike           | wants to browse the content of a website without having to pay a premium                             | so he can afford all features and recommend them to his friends.                         |
|                | wants to have a reset password option when he registers on Creature Comforts                         | so he can retrieve and update his login details during future visits.                          |
|                | wants to use a nickname on Creature Comforts' blog                                                   | so he can have a personalised browsing experience.                                             |
|                | wants to track information he likes on the blog                                                      | so he can return to it more easily.                                                            |
|                |                                                                                                      |                                                                                                |
| :man: Lou            | wants to include his family's need in his shopping                                                   | so he can spend quality time with them.                                                  |
|                | wants to access Creature Comforts' website using his iPad                                            | as it is the most convenient device in his house for browsing.                                 |
|                | wants to access information easily                                                                   | because Lou does not like to shop or spend too much time online.                               |
|                | wants to encourage small business and business ventures like creature Comforts                       | because he believes in buying local and trusting personable companies.                         |
|                | wants to see on the Creature Comforts' blog what other parents do with their kids in their down time | so he can come up with new activities on a budget.                                             |

## Features

- Creature Comforts' first impression (home page)
    - When arriving on the website's landing page, if they are using a big viewport, visitors are presented with a loading icon for less than a second while the home page promptly loads the relevant content (parallax image).
    On smaller viewport, the parallax is omitted and visitors are able to access the landing page immediately.
    
    - Visitors are then presented with a lovely website, and they can explore its many pages using the top-screen navigation bar (collapsible if on a small viewport). 
    Visitors have an overview of Creature Comforts' concept and what is provided in the boxes promoted. 
    Visitors can also view testimonials from previous Creature Comforts' customers.

- User Registration & Login to access all website features
    - Creature Comforts allows visitors to browse and view most of its content (products, search results, posts).
    However, a visitor can only do so much by browsing anonymously on the website. 
    In order to avail of all of the blog's options or to finalize a purchase, a visitor must register and log in.

- Online shop offering bespoke products
    - A selection of products suited to different needs are available via the box concept offered by Creature Comforts.
    - Moreover, it is possible for visitors to look up specific products quickly using key words via the search bar.
    - A few clicks are sufficient for a visitor to add items to his/her cart, review his/her selection, checkout and receive the desired box at regular intervals.
    

- Blog where members can inspire each other
    - All visitors can view the contributions of others to the Creature Comforts' blog.
    - Registered visitors can create posts and topics and follow subjects that interests them.
    - Visitors can also access other users' profiles and reach out to them using their profile details if they share similar ideas. 

- Contact form
    - For visitors who want to reach out to the webmaster, using the contact form provided on the website makes the process easy and straightforward.
    All comments are acknowledged.

- FAQs
    - On the FAQs page, visitors can obtain information about the box subscription system itself. 
    They can review privacy policy, terms and conditions, and Creature Comforts' promise to their customers as well.

- About 
    - This page is meant for visitors that remain curious about the concept behind Creature Comforts and the reasoning explaining the box contents.
    

## Technologies Used

- [CSS](https://simple.wikipedia.org/wiki/Cascading_Style_Sheets)
    
    Cascading Style Sheets, or CSS, are a way to change the look of HTML and XHTML web pages. 
    CSS was used in this project for the user interface and overall website look - button sizing, background image, etc.

- [HTML](https://simple.wikipedia.org/wiki/HTML)
    
    HyperText Markup Language (HTML) is a markup language for creating a webpage.  They can include writing, links, pictures, and even sound and video. HTML is used to mark and describe each of these kinds of content so the web browser can display them correctly.
    HTML was essential to this project as it builds up the views and DOM elements of the web app, structured by Flask.
 
- [JQuery](https://jquery.com)
     
     The project uses JQuery to simplify DOM manipulation.
- [Modernizr](https://modernizr.com/)

    Modernizr tells you what HTML, CSS and JavaScript features the user’s browser has to offer. I use it for this project in relation to the loading animation on big viewport preceding the parallax image.
    
- [EmailJS](https://www.emailjs.com/)
    
    A Javascript library using client-side code to connect to supported email services. I used this service to generate the contact form template and connect to my existing Gmail account.

    
- [Python 3.6.5](https://www.python.org/)
    
    Python is a clear and powerful object-oriented programming language, comparable to Perl, Ruby, Scheme, or Java. Most of this project's elements are built using Python via Jinja2.
    
- [Gunicorn 'Green Unicorn'](https://gunicorn.org/)

    The Gunicorn "Green Unicorn" is a Python Web Server Gateway Interface HTTP server. 
    
- [Jinja2](http://jinja.pocoo.org/)
    
    Jinja2 is a full featured template engine for Python. This was used for the dynamic elements of the website, along with the forms management.

- [Django](https://www.djangoproject.com/) (Version 2.1.)

    - Django is a free, open-source high-level Python Web framework that encourages rapid development and clean, pragmatic design. The Creature Comforts Project was built and rely entirely on the Django framework.
        
        Specific Django Resources:
        - [Built-in template tags and filters](https://docs.djangoproject.com/en/2.1/ref/templates/builtins/) This was helpful with my understanding of csrf_token, safe filter, etc.
        - [The Django admin documentation generator](https://docs.djangoproject.com/en/2.1/ref/contrib/admin/admindocs/)
        - [Argon2](https://pypi.org/project/argon2_cffi/) It allows for the best password hashing function (Argon2 was declared the winner of the Password Hashing Competition (PHC)). Argon2 is used in this project to ash the password submitted upon user registration.
        - [Misaka](https://github.com/FSX/misaka) It is a library that allows users to use markdown inside of the posts.
        - [django-braces](https://django-braces.readthedocs.io/en/latest/) Mixins for Django's class-based views.
        - [Q Objects](https://docs.djangoproject.com/en/2.1/ref/models/querysets/#django.db.models.Q) This permits the construction of complex database queries using | (OR) and & (AND) operators.

- [Heroku](https://www.heroku.com/)

    Heroku is a cloud platform based on a managed container system, with integrated data services and a powerful ecosystem, for deploying and running modern apps. This project was deployed on the Heroku cloud platform.
    
     - [Heroku Postgres](https://www.heroku.com/postgres)
        
        PostgreSQL is one of the world's most popular relational database management systems. I transitioned my database from SQLite to PostgreSQL while deploying my website with Heroku.

- [Bootstrap](http://getbootstrap.com/) (v4.1.3)

    Bootstrap is an open source toolkit for developing with HTML, CSS, and JS. During the creation of Creature Comforts, I used Bootstrap to establish and maintain good UI/UX over all aspects of the website (forms, navigation, product display, etc.).
- [Font Awesome](https://fontawesome.com/)
    Font Awesome is a font and icon toolkit based on CSS and LESS. It was made by Dave Gandy for use with Twitter Bootstrap, and later was incorporated into the BootstrapCDN.

- [AWS](https://aws.amazon.com/)      
  
    AWS offers a complete range of cloud storage services to support both application and archival compliance requirements. 
    
    - [S3](https://aws.amazon.com/s3/)
    
        Amazon Simple Storage Service (Amazon S3) is an object storage service that offers industry-leading scalability, data availability, security, and performance.
        
    - [IAM](https://aws.amazon.com/iam/)
    
        AWS Identity and Access Management (IAM) enables you to manage access to AWS services and resources securely. Using IAM, you can create and manage AWS users and groups, and use permissions to allow and deny their access to AWS resources.
    
    - [AWS SDK for Python (Boto3)](https://aws.amazon.com/sdk-for-python/)
    
        Boto3 is the AWS SDK for Python and allows an easy integration with Python applications, services or libraries with AWS services, such as Amazon S3.

## [Testing](testing.pdf)

 Due to the thoroughness of my tests' description, I have included my testing process in another file referenced [here](testing.pdf). As it is a lengthy document, I converted it to PDF instead of using Markdown.
 Hopefully this will be easier to read in that format.
 If needed or prefered, the Word (.docx) version of the testing document is also available [here](testing.docx).
 
## Installation & Deployment
**While in development**

- I created the web app using [PyCharm](https://www.jetbrains.com/pycharm/), which is a Python IDE. The app was tested in a development environment with Django's debug mode (in settings: Debug=True).
The Debug mode is a massive perk while in development, as to refer to the Django documentation itself [[1]](https://docs.djangoproject.com/en/2.1/ref/settings/#std:setting-DEBUG):
    > One of the main features of debug mode is the display of detailed error pages. If your app raises an exception when DEBUG is True, Django will display a detailed traceback, including a lot of metadata about your environment, such as all the currently defined Django settings (from settings.py).
The secret key and other config variables were stored in an environment file during development. 

- I also included '*' in the ALLOWED_HOSTS field in order to work with the Django app using the localhost.
These variables are relevant to the Django project and the issuance of email via the reset password option.

**Preparing for deployment**
- I then logged in my Heroku account and created an app (ci-vero-fullstack). A Heroku-hosted remote that’s associated with my app was created at the same time.
I linked my "nuagesdencre/ci-fullstack" Github repository to the Heroku app for deployment from its master branch.

- On the Heroku website, using the dashboard's Setting tab, I accessed the Config Vars section where I entered all variables I had referred to locally in my environment file.
    These variables are essential for all the features of my project to function (such as the checkout feature, the reset password feature, etc.).
    (SECRET_KEY, STRIPE_SECRET, STRIPE_PUBLISHABLE, EMAIL_PASSWORD, EMAIL_ADDRESS )

- In order to avoid relying on the ephemeral storage system of Heroku, I opted for media file hosting with AWS.
I added the relevant environment variables (AWS_ACCESS_KEY, AWS_SECRET_ACCESS_KEY) in order to access my AWS bucket and the uploaded data. I made sure to use the COLLECTSTATIC command to gather my local static files and bring them to the database. 
In the Config Vars screen of the Heroku dashboard, I disabled the collectstatic during a deploy by Heroku by adding in the Config Vars DISABLE_COLLECTSTATIC with the value 1.

- Once again, to avoid losing user created data, I also created a PostgreSQL database using the heroku command **"heroku addons:create heroku-postgresql:hobby-dev"**.
 I had to change from SQLite database (file based) to PostgreSQL on Heroku for my database to retain its contents once the website is deployed online. 
 To quote the Heroku website [[2]](https://devcenter.heroku.com/articles/sqlite3):
 
     > SQLite runs in memory, and backs up its data store in files on disk. While this strategy works well for development, Heroku’s Cedar stack has an ephemeral filesystem." 
     
     I commented out my local database and include the
     link to the Heroku generated PostgreSQL database instead. I initialized the PostgreSQL database and pushed the migrations. 
     I used the module dj_database_url within my Django project so that I could refer to the url directly in my settings.py (in my case, via a variable in the environment file).

**In production**
  
- In my settings.py file, I changed the app environment to production and removed the debugging option (DEBUG=False). 
I also removed ' * ' (wildcard) from the ALLOWED_HOSTS fields. 
I made sure to include the appropriate information in my Procfile (**web: gunicorn creaturecomforts.wsgi:application**). 

    A Procfile is a mechanism for declaring what commands are run by my application’s web dynos (lightweight Linux containers dedicated to running my application web processes) on the Heroku platform.[[3]](https://devcenter.heroku.com/articles/dynos)

- I manually requested the deployment from the master branch.
 I reviewed the logs via the Heroku dashboard once the deployment confirmed and opened the app using my web browser to ensure everything was working properly.
Lastly, I tested the checkout feature relying on Stripe to ensure everything was processed smoothly. 

## Hurdles

- Stripe Payment

    - I encountered an issue with the checkout as the stripe.js script was called before JQuery. It took me a little while to figure out the issue, as I initially was thrown off by the error 'stripe_id required'.
I had to realize the stripe_id was not generated because the script did not run in the first place.

- UI/UX of the website

    - As usual, I had a lot of feedback from my friends and family members regarding the website. 
It was quite difficult to come up with an elegant concept that pleased everyone, but I did it after consulting each of my 'advisors' on their preferred user experience.

- Profile Image

    - I had a typo in the user profile page that did not display the profile_image but instead checked if the user had provided any profile data.
This typo was thankfully found during the final testing process of the project.

## Credits

Usage of Class based views for the blog section of the website, and function based views for the user, shop, cart and product sections.
- [Class-based views](https://docs.djangoproject.com/en/2.1/topics/class-based-views/)
- [Using mixins with class-based views](https://docs.djangoproject.com/en/2.1/topics/class-based-views/mixins/)
- [Class-Based Views vs. Function-Based Views](https://simpleisbetterthancomplex.com/article/2017/03/21/class-based-views-vs-function-based-views.html)
- [What is the difference between Class Based Views and Function Based Views?](https://www.bedjango.com/blog/class-based-views-vs-function-based-views/)
        -..."we use generic views with class if the functionality contains CRUD operations or it’s more complex, as it's more optimal."
- [Built-in template tags and filters](https://docs.djangoproject.com/en/2.1/ref/templates/builtins/)        
- [Slug](https://stackoverflow.com/questions/427102/what-is-a-slug-in-django?rq=1)
- [super()](https://docs.djangoproject.com/en/2.1/topics/db/models/)
    - It’s important to remember to call the superclass method – that’s that super().save(*args, **kwargs) business – to ensure that the object still gets saved into the database. 
    If you forget to call the superclass method, the default behavior won’t happen and the database won’t get touched.

### Content

The concept and contents of Creature Comforts are inspired by 'CrateJoy' [[link here]](https://www.cratejoy.com/), but otherwise up entirely original, made up to serve in the context of a web development course. 

I combined business elements similar to those of existing box delivery companies, my own fascination for the Danish art of living well and current self-care trends.
This website was created for educational purposes only and I do not claim to be an expert in any of the above aspects.

### Media

Icons other than Font Awesome - displayed on Creature Comforts were sourced on [Flaticon](https://www.flaticon.com/) and [Invision](https://www.invisionapp.com/inside-design/design-resources/). 

Only Flaticon required attribution and it is provided in the footer of the home page, as per the website's basic license requirements [here](https://support.flaticon.com/hc/en-us/articles/207248209). 
The Flaticons were only used on that specific page.

All pictures used on Creature Comforts were  found on [Pexels](https://www.pexels.com/) and [Pixabay](https://pixabay.com/).
The pictures are under public domain and do not require attribution. They have been heavily modified for the purpose of this project.

The background pattern of 'funky lines' was found on [Subtle Patterns](https://www.toptal.com/designers/subtlepatterns/).
## Acknowledgements

It is the last project that I submit for the CI Software Development Course. I am amazed at the progress I have made since I first started, what a contrast from my earlier days coding!
Biggest thanks to my friends and family who supported me during this process and did their best to pinpoint the weaknesses and praise the strengths of Creature Comforts.
I received the best advice and moral support from my mentor, who I hope is pleased with the outcome of my Code Institute journey.
 #### A big, enthusiastic thank you!
 ###
 
Please get in touch if you have any comments or questions.

vero@nuagesdencre.com