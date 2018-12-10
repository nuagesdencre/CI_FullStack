# Veronique's Full Stack Project **Creature Comforts**
### Code Institute Full Stack Milestone Project
[![Build Status](https://travis-ci.org/nuagesdencre/CI_FullStack.svg?branch=master)](https://travis-ci.org/nuagesdencre/CI_FullStack)
One or two paragraphs providing an overview of your project.
Essentially, this part is your sales pitch.
 - key words: ease, comfort, calm, relaxing, pretty, subtle, organised, fluff, texture, warmth
 
## UX
 - Colour psychology:
    -[Color in Design: Influence on Users' Actions](https://tubikstudio.com/color-in-design-influence-on-users-actions/)
    -[Color Theory Brief](https://uxplanet.org/color-theory-brief-guide-for-designers-76e11c57eaa)
Use this section to provide insight into your UX process, focusing on who this website is for, what it is that they want to achieve and how your project is the best way to help them achieve these things.
In particular, as part of this section we recommend that you provide a list of User Stories, with the following general structure:
- As a user type, I want to perform an action, so that I can achieve a goal.
This section is also where you would share links to any wireframes, mockups, diagrams etc. that you created as part of the design process. These files should themselves either be included in the project itself (in an separate directory), or just hosted elsewhere online and can be in any format that is viewable inside the browser.
## Features
In this section, you should go over the different parts of your project, and describe each in a sentence or so.
 - A Django app must perform a particular functionality within the web application (i.e. registration app, comments app, ...)

### Existing Features
- Feature 1 - allows users X to achieve Y, by having them fill out Z
- ...
For some/all of your features, you may choose to reference the specific project files that implement them, although this is entirely optional.
In addition, you may also use this section to discuss plans for additional features to be implemented in the future:
### Features Left to Implement
- Another feature idea
## Technologies Used
In this section, you should mention all of the languages, frameworks, libraries, and any other tools that you have used to construct this project. For each, provide its name, a link to its official site and a short sentence of why it was used.
- [Python]()
    - Lorem.
- [Django]()
    - Lorem. Version 2.1.
    - https://docs.djangoproject.com/en/2.1/ref/templates/builtins/ (csrf_token,safe, etc.)
    - https://docs.djangoproject.com/en/2.1/ref/contrib/admin/admindocs/
    -[super()](https://docs.djangoproject.com/en/2.1/topics/db/models/)
        It’s important to remember to call the superclass method – that’s that super().save(*args, **kwargs) business – to ensure that the object still gets saved into the database. If you forget to call the superclass method, the default behavior won’t happen and the database won’t get touched.
    - xyz
- [JQuery](https://jquery.com)
    - The project uses **JQuery** to simplify DOM manipulation.
- [Argon2](https://pypi.org/project/argon2_cffi/)
- [Misaka](https://github.com/FSX/misaka) It is a library allows users to use markdown inside of the posts.
-[django-braces](https://django-braces.readthedocs.io/en/latest/) Mixins for Django's class-based views.
- Emailjs

Usage of Class based views for the blog section of the website, and function based views for the user, shop, cart and product sections.
-[Class-based views](https://docs.djangoproject.com/en/2.1/topics/class-based-views/)
-[Using mixins with class-based views](https://docs.djangoproject.com/en/2.1/topics/class-based-views/mixins/)
-[Class-Based Views vs. Function-Based Views](https://simpleisbetterthancomplex.com/article/2017/03/21/class-based-views-vs-function-based-views.html)
-[What is the difference between Class Based Views and Function Based Views?](https://www.bedjango.com/blog/class-based-views-vs-function-based-views/)
        -..."we use generic views with class if the functionality contains CRUD operations or it’s more complex, as it's more optimal."
-[Built-in template tags and filters](https://docs.djangoproject.com/en/2.1/ref/templates/builtins/)        
-[Slug](https://stackoverflow.com/questions/427102/what-is-a-slug-in-django?rq=1)
## Testing
#### Countinuous Integration
[![Build Status](https://travis-ci.org/nuagesdencre/CI_FullStack.svg?branch=master)](https://travis-ci.org/nuagesdencre/CI_FullStack)
In this section, you need to convince the assessor that you have conducted enough testing to legitimately believe that the site works well. Essentially, in this part you will want to go over all of your user stories from the UX section and ensure that they all work as intended, with the project providing an easy and straightforward way for the users to achieve their goals.
Whenever it is feasible, prefer to automate your tests, and if you've done so, provide a brief explanation of your approach, link to the test file(s) and explain how to run them.
For any scenarios that have not been automated, test the user stories manually and provide as much detail as is relevant. A particularly useful form for describing your testing process is via scenarios, such as:
1. Contact form:
    1. Go to the "Contact Us" page
    2. Try to submit the empty form and verify that an error message about the required fields appears
    3. Try to submit the form with an invalid email address and verify that a relevant error message appears
    4. Try to submit the form with all inputs valid and verify that a success message appears.
In addition, you should mention in this section how your project looks and works on different browsers and screen sizes.
You should also mention in this section any interesting bugs or problems you discovered during your testing, even if you haven't addressed them yet.
If this section grows too long, you may want to split it off into a separate file and link to it from here.
## Deployment

- media file hosting
- heroku set up
- specific config or library
This section should describe the process you went through to deploy the project to a hosting platform (e.g. GitHub Pages or Heroku).
In particular, you should provide all details of the differences between the deployed version and the development version, if any, including:
- Different values for environment variables (Heroku Config Vars)?
- Different configuration files?
- Separate git branch?
In addition, if it is not obvious, you should also describe how to run your code locally.
## Credits
### Content
- The text for section Y was copied from the [Wikipedia article Z](https://en.wikipedia.org/wiki/Z)
### Media
The icons were retrieved on [Flaticon](https://www.flaticon.com/) and [Invision](https://www.invisionapp.com/inside-design/design-resources/). 
Only Flaticon required attribution and it is provided in the footer of the home page, as per the website's basic license requirements [here](https://support.flaticon.com/hc/en-us/articles/207248209). 
The Flaticons were only used on that specific page.

All pictures used on Creature Comforts were  found on [Pexels](https://www.pexels.com/) and [Pixabay](https://pixabay.com/).
The pictures do not require attribution. They have been heavily modified for the purpose of this project.

### Acknowledgements
- I received inspiration for this project from X

