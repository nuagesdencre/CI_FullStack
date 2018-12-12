# Veronique's Full Stack Project **Creature Comforts**
### Code Institute Full Stack Milestone Project
[![Build Status](https://travis-ci.org/nuagesdencre/CI_FullStack.svg?branch=master)](https://travis-ci.org/nuagesdencre/CI_FullStack)

**sales pitch**

## UX
 - Colour psychology:
    -[Color in Design: Influence on Users' Actions](https://tubikstudio.com/color-in-design-influence-on-users-actions/)
    -[Color Theory Brief](https://uxplanet.org/color-theory-brief-guide-for-designers-76e11c57eaa)
    
- [Original Wireframe](./planning/creaturecomforts.png)
- [Planning](./planning/userstories_creaturecomforts.xlsx)

- User stories
 [Meet our Users!](./planning/USERS_STORIES.jpg?raw=true)
 
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
- Home page introducing the online shop
- User login /Register to access all website features
- Shop with unique product
    - possible to find products using the search bar
- Blog where members can exchange ideas
    - Possible to create posts and topics
    - Follow option to track topics that interest you
    - You can access other users' profiles to reach out to them if they share similar ideas 
- Contact form
- FAQs
    - To obtain information about the box subscription system itself
    - To review privacy policy, terms and conditions, Creature Comforts' promise to their clients
- About page
    - To learn more about the concept behind Creature Comforts
    
## Potential future features
- View Orders
## Technologies Used

- [CSS](https://simple.wikipedia.org/wiki/Cascading_Style_Sheets)
    
    Cascading Style Sheets, or CSS, are a way to change the look of HTML and XHTML web pages. 
    CSS was used in this project for the user interface and overall website look - button sizing, background image, etc.

- [HTML](https://simple.wikipedia.org/wiki/HTML)
    
    HyperText Markup Language (HTML) is a markup language for creating a webpage.  They can include writing, links, pictures, and even sound and video. HTML is used to mark and describe each of these kinds of content so the web browser can display them correctly.
    HTML was essential to this project as it builds up the views and DOM elements of the web app, structured by Flask.
 
- [JQuery](https://jquery.com)
     
     The project uses JQuery to simplify DOM manipulation.
    
- [EmailJS](https://www.emailjs.com/)
    
    A Javascript library using client-side code to connect to supported email services. I used this service to generate the contact form template and connect to my existing Gmail account.

    
- [Python 3.6.5](https://www.python.org/)
    
    Python is a clear and powerful object-oriented programming language, comparable to Perl, Ruby, Scheme, or Java. Most of this project's elements are built using Python via Jinja2.
    
    
- [Jinja2](http://jinja.pocoo.org/)
    
    Jinja2 is a full featured template engine for Python. 
     It has full unicode support, an optional integrated sandboxed execution environment, widely used and BSD licensed. This was used for the dynamic elements of the website, along with the forms management.

- [Django](https://www.djangoproject.com/) (Version 2.1.)

    - Django is a free, open-source high-level Python Web framework that encourages rapid development and clean, pragmatic design. The Creature Comforts Project was built and rely entirely on the Django framework.
    - https://docs.djangoproject.com/en/2.1/ref/templates/builtins/ (csrf_token,safe, etc.)
    - https://docs.djangoproject.com/en/2.1/ref/contrib/admin/admindocs/
    - [Argon2](https://pypi.org/project/argon2_cffi/)
    - [Misaka](https://github.com/FSX/misaka) It is a library allows users to use markdown inside of the posts.
    -[django-braces](https://django-braces.readthedocs.io/en/latest/) Mixins for Django's class-based views.

- [Heroku](https://www.heroku.com/)

    Heroku is a cloud platform based on a managed container system, with integrated data services and a powerful ecosystem, for deploying and running modern apps. This project was deployed on the Heroku cloud platform.
    
     - [Heroku Postgres](https://www.heroku.com/postgres)
        
        PostgreSQL is one of the world's most popular relational database management systems. I transitioned my database from SQLAlchemy (SQLite) to PostgreSQL while deploying my website with Heroku.

- [Bootstrap](http://getbootstrap.com/) (v4.1.3)

    Bootstrap is an open source toolkit for developing with HTML, CSS, and JS. During the creation of Creature Comforts, I used Bootstrap to establish and maintain good UI/UX over all aspects of the website (forms, navigation, product display, etc.).

- [AWS](https://aws.amazon.com/)        
    AWS offers a complete range of cloud storage services to support both application and archival compliance requirements. 
    - [S3](https://aws.amazon.com/s3/)
    
        Amazon Simple Storage Service (Amazon S3) is an object storage service that offers industry-leading scalability, data availability, security, and performance.
    - [IAM](https://aws.amazon.com/iam/)
    
        AWS Identity and Access Management (IAM) enables you to manage access to AWS services and resources securely. Using IAM, you can create and manage AWS users and groups, and use permissions to allow and deny their access to AWS resources.

## Testing
#### Countinuous Integration
[![Build Status](https://travis-ci.org/nuagesdencre/CI_FullStack.svg?branch=master)](https://travis-ci.org/nuagesdencre/CI_FullStack)

## Installation & Deployment

This project has been deployed using Heroku.
- This project can be deployed again using the below button.

  [![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)
    
    This option is available since I provide an app.json file as per the guidelines found [here](https://devcenter.heroku.com/articles/heroku-button).
*******

- I created the web app using [PyCharm](https://www.jetbrains.com/pycharm/), which is a Python IDE. The app was tested in a development environment with a debugging option.
The secret key and other config variables were stored in an environment file during development. 
These variables are relevant to the Django project and the issuance of email via the reset password option.

- I then logged in my Heroku account and created an app (ci-vero-fullstack). A Heroku-hosted remote that’s associated with my app was created at the same time.
I linked my "nuagesdencre/ci-fullstack" Github repository to the Heroku app for deployment from its master branch.

- On the Heroku website, using the dashboard, I entered the IP and PORT into the Heroku Config Vars fields (0.0.0.0 and 5000), along with my environment file's other variables.

- media file hosting with AWS

- I also created a PostgreSQL database using the heroku command **"heroku addons:create heroku-postgresql:hobby-dev"**.

     I had to change from SQLite database (file based) to PostgreSQL on Heroku for my database to retain its contents once the website is deployed online. I commented out my local database and include the
link to the Heroku generated PostgreSQL database instead. I intialized the PostgreSQL database and pushed the migrations.

- I changed the app environment to production and removed the debugging option.

- I manually requested the deployment from the master branch.
 I reviewed the logs via the Heroku dashboard once the deployment confirmed and opened the app using my web browser to ensure everything was working properly.

- continous integration with travis 

## [Testing](testing.md)
 Due to the length of my tests' description, I have included my breakdown in another file referenced [here](testing.md).
 
## Hurdles

- Stripe Payment
- UI/UX of the website

## Credits

Usage of Class based views for the blog section of the website, and function based views for the user, shop, cart and product sections.
    -[Class-based views](https://docs.djangoproject.com/en/2.1/topics/class-based-views/)
    -[Using mixins with class-based views](https://docs.djangoproject.com/en/2.1/topics/class-based-views/mixins/)
    -[Class-Based Views vs. Function-Based Views](https://simpleisbetterthancomplex.com/article/2017/03/21/class-based-views-vs-function-based-views.html)
    -[What is the difference between Class Based Views and Function Based Views?](https://www.bedjango.com/blog/class-based-views-vs-function-based-views/)
            -..."we use generic views with class if the functionality contains CRUD operations or it’s more complex, as it's more optimal."
    -[Built-in template tags and filters](https://docs.djangoproject.com/en/2.1/ref/templates/builtins/)        
    -[Slug](https://stackoverflow.com/questions/427102/what-is-a-slug-in-django?rq=1)
    -[super()](https://docs.djangoproject.com/en/2.1/topics/db/models/)
        It’s important to remember to call the superclass method – that’s that super().save(*args, **kwargs) business – to ensure that the object still gets saved into the database. 
        If you forget to call the superclass method, the default behavior won’t happen and the database won’t get touched.
    
### Content

- The concept and content of Creature Comforts is made up entirely to serve in the context of a web development course. 
It has been largely inspired from existing box delivery companies and current self-care trends.
This website was created for educational purposes only.

### Media

The icons were retrieved on [Flaticon](https://www.flaticon.com/) and [Invision](https://www.invisionapp.com/inside-design/design-resources/). 
Only Flaticon required attribution and it is provided in the footer of the home page, as per the website's basic license requirements [here](https://support.flaticon.com/hc/en-us/articles/207248209). 
The Flaticons were only used on that specific page.

All pictures used on Creature Comforts were  found on [Pexels](https://www.pexels.com/) and [Pixabay](https://pixabay.com/).
The pictures do not require attribution. They have been heavily modified for the purpose of this project.

## Acknowledgements

It is the last project that I submit for the CI Software Development Course. I am amazed at the progress I have made since I first started, what a contrast from my earlier days coding!
Biggest thanks to my friends and family who supported me during this process and did their best to pinpoint the weaknesses and perks of Creature Comforts.
I received the best advice and moral support from my mentor, who I hope is pleased with the outcome of my Code Institute journey.
 #### Thank you!
 ###
 
Please get in touch if you have any comments or questions.

vero@nuagesdencre.com