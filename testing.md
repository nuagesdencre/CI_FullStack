# Veronique's Full Stack Project **Creature Comforts**

# Testing
- ### Website Responsiveness
    - Overall Responsiveness and browser compatibility
    
        - [Browserling](www.browserling.com/)
        
            This website has been tested on multiple devices and browsers to ensure utmost responsiveness.
            I have also used the website 'Browserling' for that purpose.
- ### Navigation  
   
    I. The navigation bar at the top of the screen displays the name 'Amphora' and if I click on it at any point while I am browsing, I am brought back to the home page.
    
    - I.I. When I visit the page using a large viewport, the navigation bar is at the top of the screen and displays the options available. An user icon indicates where I have to click for user-relevant options (login or register during my first visit).
    
    - I.II. While visiting using my smartphone, the navigation bar is triggered when I click on the hamburger menu at the top-left of the screen. The user-related options are highlighted in the menu.
    
    ##### Elements affected by user status (logged in or not)
    II. 
    If I am logged in, the user options available in the navigation bar change: 'Login' and 'Register' are replaced by 'Profile' and 'Logout'.
    If I click on 'Log Out', an alert message advises me that I successfully logged out and I am brought back to the home page, from wherever I was on the website. The user-relevant are defaulted to 'Login' and 'Register'.
    
    **Information displayed**
    
    I. The home page displays an introductory paragraph along with two pictures and quotes. The website is responsive, so the position of these elements change according to the size of the viewport used.
       
- ### Footer

     I. The footer remains identical on all pages of the website. 
     
    - ### Social media Icons
    - ### External links
        - Link to Github
        - Link to Nuagesdencre
        
    - ### About (CC'S Concept)

        ##### This page's features are not affected by the visitor' status (if user is logged or anonymous).
       I. This page provides me with a definition of 'amphora' and displays FAQs. The purpose and functionality of the project are presented here.
        
    - ### Contact

        ##### This page's features are not affected by the visitor' status (if user is logged or anonymous).
        I. I can use a contact form on this page to reach out to the webmaster.
         - The forms' required fields are: name; location; email address; message.
         - An error message appears if the requirements for various fields are not met when I click the submit button ('Done!').
    
            The contact form's fields have been manually tested with incorrect data to ensure relevance of the error messages.
        
        II. When I click the 'Send your Message' button, if the fields requirements have been met, a loading animation runs while my information is sent through.
        Once done, an on-screen alert confirms that my message has been sent. If there was a problem sending the message, an alert would populate with the error as a JSON string.
        I am redirected to Amphora's home page once I close the alert.
                 
        III. If I provide a valid email address when submitting the contact form, an auto-reply will be issued to my attention, thanking me for my feedback.
    
    - ### About (CC'S Concept)

        ##### This page's features are not affected by the visitor' status (if user is logged or anonymous).
        I. Lorem.
    
- ### Home page

- ### Blog section

    - #### Main page (View Topics)

        - ##### While a visitor is anonymous:
        
            I. Lorem ipsum.
                
           II. Lorem ipsum.
            
           III. Lorem ipsum.
           
        - #####  While a visitor is logged in:
    
    - #### Topics detailed page

        - ##### While a visitor is anonymous:
        
        - #####  While a visitor is logged in:
    
    - #### Profile page

        - ##### While a visitor is anonymous:
        - #####  While a visitor is logged in:
   
    - #### Posts detailed page

        - ##### While a visitor is anonymous:
        - #####  While a visitor is logged in:
        
- ### Shop section
    - #### Main page (View All Products)

        - ##### While a visitor is anonymous:
            I. Lorem ipsum.
                
           II. Lorem ipsum.
            
           III. Lorem ipsum.
        - #####  While a visitor is logged in:
        
     - #### Cart page

        - ##### While a visitor is anonymous:
            I. Lorem ipsum.
                
           II. Lorem ipsum.
            
           III. Lorem ipsum.
        - #####  While a visitor is logged in:
    
     - #### Search results page
        ##### This feature is not affected by the visitor' status (if user is logged or anonymous).
         
         I. I can access the search product feature via the navigation bar or the 'Search' button available on the repository's page.
                
        - ##### While a visitor is anonymous:
            I. Lorem ipsum.
                
           II. Lorem ipsum.
            
           III. Lorem ipsum.
        - #####  While a visitor is logged in:

- ### User identification 

    - #### Register
    
        I. On the register page, I need to provided a username, an email and a password (that I need to confirm) before clicking the 'Register now' button.
        There is a message reminding me that the fields are case-sensitive.
         
         - An error message appears if the requirements for various fields are not met when I click the submit button ('Register now!').
    
         The registration form's fields have been manually tested with incorrect data to ensure relevance of its error messages.
       
        I.I. If I registered before, I can click on the link below the 'Register now' button to access the login page instead.       
        
        II. Once registered, I am redirected to the login page, where I need to provide my email and password. (**refer to Login page below**)
        
    - #### Account and profile
    
        I. On the account page, my username and email address are displayed.
        
        II. I can update my email by typing in the editable field and clicking the 'Update email' button.
        
        III. I can access the content I provided so far on Amphora by clicking on 'Your Entries' button. This leads me to the detailed view of my profile 
        where entries, separated by type, and comments that I have authored are listed. Because I do not need to be logged in to create or edit a category, they are not included on my profile.
        I can click on any of the displayed content to access its location within Amphora directly.
        
    - #### Login
    
        I. When I log in, I need to provide my email and password.
         
        - I.I. The login page displays a message reminding me that the fields are case-sensitive.
            
        - I.II. There are two other links under the login input fields: a link leading to the 'register' page and another leading to the 'Forgot your password' option.
        
        II. Once logged in, I am redirected to my account page.
        
    - #### Logout 
        
        I. The logout option is only available in the navigation bar if I am logged in already.
        
        II. If I click on 'Log Out', an alert message advises me that I successfully logged out and I am brought back to the home page, from wherever I was on the website. The user-relevant menu options are defaulted to 'Login' and 'Register'.
    
    - #### Password reset functionality
    
    I. If I registered in the past but I have forgotten my password, I can access the reset password function via the login page.
    
    II. I provide my email address and click on the 'Send request' button. Incorrect information will result in nothing being issued and no password request possible.
    
    III. Once I click the 'Send request' button, I am redirected to the login page. A message appears at the top of the page to let me know my request has been processed and that the next steps will be emailed to me.
    
    IV. If I look in my email, I have a message with the title "Password Reset Request" with a link back to Amphora. I click on the link or copy it as suggested. This brings me to a Password reset page, where I need to enter a new password and confirm it.
    
    V. Once the new password is submitted, I am redirected to the login page where a new message confirms my password has been reset successfully.

#### Error handling
- A 404 error is returned by a web server (the machine where a website is hosted) when it cannot find the page requested. This error is often due to an incorrect or non-existent URL.
I integrated a custom error 404 page to the project in order to direct visitors back to the home page should they encounter this specific issue. However, the website is conceived in a way that encourages visitors to use the website features and navigation options.

- Error 500  
 
#### Python and Django

PyCharm refactoring
Django debugging

### Javascript, CSS & HTML Validation

To the best of my ability, I conducted and documented tests to ensure that all of my website's functionality work well, while taking in account the user stories.

- [CSS Validation Service](http://jigsaw.w3.org/css-validator/)
    <p>
    <a href="http://jigsaw.w3.org/css-validator/check/referer">
        <img style="border:0;width:88px;height:31px"
            src="http://jigsaw.w3.org/css-validator/images/vcss-blue"
            alt="Valid CSS!" />
        </a>
    </p>
     I ensured my CSS had no typos, errors or incorrect uses using The CSS Validation service.
     
     I also verified that all DOM elements were readable and easily accessible (i.e. no small links or buttons) on all viewports.

- [JSHINT](https://jshint.com/about/)
    
    - I used JSHINT to pinpoint any bug or typo in my scripts.

- [Nu Html Checker](https://validator.w3.org/nu/about.html)

    - I used the Nu checker to catch unintended mistakes in my Html documents, such as stand-alone tags.      
