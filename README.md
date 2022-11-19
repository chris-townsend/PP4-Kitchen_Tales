# Kitchen Tales



The live link can be found here - [Kitchen Tales](https://)

![Am i responsive]()

## Contents

- [Kitchen Tales](#kitchen-tales)
  * [Objective](#objective)
  * [Brief & Target Audience](#brief)
  * [User Experience (UX)](#user-experience-ux)
    + [User Stories](#user-stories)
    + [Design](#design)
      - [Colour Scheme](#colour-scheme)
      - [Imagery](#imagery)
      - [Fonts](#fonts)
      - [Wireframes](#wireframes)
  * [Agile Methodology](#agile-methodology)
  * [Data Model](#data-model)
  * [Testing](#testing)
  * [Security Features](#security-features)
    + [User Authentication](#user-authentication)
    + [Form Validation](#form-validation)
    + [Database Security](#database-security)
    + [Custom error pages](#custom-error-pages-)
  * [Features](#features)
    - [Features Left to Implement](#future-features)
    - [Languages Used](#languages-used)
  - [Technologies Used](#programs-frameworks--libraries-used)
  * [Deployment](#deployment)
    - [Heroku](#heroku)
    - [Forking the GitHub Repository](#forking-this-repository)
    - [Making a local clone](#cloning-this-repository)
  * [Credits](#credits)
    + [Content](#content)
    + [Media](#media)
  * [Acknowledgments](#acknowledgments)

***
## Objective
#

***

## Brief & Target Audience
#
A visitor to Kitchen Tales would be someone who is most likely an adult who enjoys their food and trying new recipes
***

## User Experience (UX)
#


### User Stories
#


#### EPIC | Early Deployment
- 

#### EPIC | Initial Django Setup
- 

#### EPIC | User Recipe Management
- 

#### EPIC | Website Functionality
-

#### EPIC | Navigation
-

#### EPIC | Admin Features & Owner Objectives
-

#### EPIC | User Account Management
-

***

#### User stories not yet implemented
#

The following user stories were scoped out of the project due to time constraints and labelled as "Won't Have" on the project board on Github. It is intended that these user stories will be implemented at a later date. 

***

### Design
#
The site has a very simple and clean design which was purposely chosen in order to keep in theme with the site's goal. i.e. invoking a sense of calm in the user and reducing stress when it comes to everyday cooking. 
***

#### Colour Scheme
#
Colour palette from Coolors

![Colour Palette]()

***

#### Imagery
#
***

#### Fonts
#
***

#### Wireframes
#

<details>

 <summary>Landing Page</summary>

![Landing Page]()
</details>

<details>

<summary>All Recipes</summary>

![All Recipes]()
</details>


<details>

<summary>Add Recipe</summary>

![Add Recipe]()
</details>

<details>

<summary>My Recipes</summary>

![My Recipes]()
</details>

<details>

<summary>My Bookmarks</summary>

![My Bookmarks]()
</details>

***

## Agile Methodology
#
Github projects was used to manage the development process using an agile approach. Please see link to project board [here](https://github.com/chris-townsend)

The 7 Epics listed above were documented within the Github project as Milestones. A Github Issue was created for each User Story which was then allocated to a milestone(Epic). Each User Story has defined acceptance criteria to make it clear when the User Story has been completed. The acceptance criteria are further broken down into tasks to facilitate the User Story's execution.

## Data Model
I used principles of Object-Oriented Programming throughout this project and Django’s Class-Based Generic Views.  

Django AllAuth was used for the user authentication system.

In order for the users to create recipes a custom recipe model was required. The recipe author is a foreign key to the User model given a recipe can only have one author.

The Comment model allows users to comment on individual recipes and the Recipe is a foreign key in the comment model given a comment can only be linked to one recipe. 


The diagram below details the database schema.

![Database Schema]()

***
## Testing
#

Testing and results can be found [here](/TESTING.md)

***
## Security Features and Defensive Design
#
### User Authentication
#
- Django's LoginRequiredMixin is used to make sure

### Form Validation
If incorrect or empty data is added to a form, the form won't submit and a warning will appear to the user informing them what field raised the error. 

### Database Security
The database url and secret key are stored in the env.py file to prevent unwanted connections to the database and this was set up before the first push to Github.

Cross-Site Request Forgery (CSRF) tokens were used on all forms throughout this site.

### Custom error pages:

Custom Error Pages were created to give the user more information on the error and to provide them with buttons to guide them back to the site.

- 400 Bad Request - The Easy Eater is unable to handle this request.
- 403 Page Forbidden - Looks like you're trying to access forbidden content. Please log out and sign in to the correct account.
- 404 Page Not Found - The page you're looking for doesn't exist.
- 500 Server Error - The Easy Eater is currently unable to handle this request

## Features
#

### Header

![header]()

**Logo**
- A customised logo was created using Hatchful by Shopify which is a free logo generator.
- This logo is positioned in the top left of the navigation bar. The logo is linked to the home page for ease of navigation for the user.

**Navigation Bar**


![header]()


### Footer

![footer]()

- The footer section includes links to Facebook, Instagram, Twitter and Youtube.
- Clicking the links in the footer opens a separate browser tab to avoid pulling the user away from the site.

### Home Page



![header](docs/readme_images/features/call_out.png)



### User Account Pages

**Sign Up**

![sign-up]()

**Log In**

![header]()

**Log Out**

![header]()

- Django allauth was installed and used to create the Sign up, Log in and Log out functionality. 
- Success messages inform the user if they have logged in/ logged out successfully.

### Browse Recipes

![header]()


### Recipe Detail Page

**Recipe Header Section**


**Recipe Action Buttons**


**Recipe Details Section**




**Comments Section**



### Add Recipe Form


### Update Recipe Form

### Delete Recipe


### My Recipes Page


### My Bookmarks Page



### Error Pages

Custom Error Pages were created to give the user more information on the error and to guide them back to the site.


- 400 Bad Request - 
- 403 Page Forbidden -
- 404 Page Not Found - 
- 500 Server Error - 

***

### Future Features
#
***

## Deployment - Heroku
#

To deploy this page to Heroku from its GitHub repository, the following steps were taken:

### Create the Heroku App:
- Log in to [Heroku](https://dashboard.heroku.com/apps) or create an account.
- On the main page click the button labelled New in the top right corner and from the drop-down menu select "Create New App".
- Enter a unique and meaningful app name.
- Next select your region.
- Click on the Create App button.

### Attach the Postgres database:
- In the Resources tab, under add-ons, type in Postgres and select the Heroku Postgres option.
- Copy the DATABASE_URL located in Config Vars in the Settings Tab.

### Prepare the environment and settings.py file:
- In your GitPod workspace, create an env.py file in the main directory.
- Add the DATABASE_URL value and your chosen SECRET_KEY value to the env.py file. 
- Update the settings.py file to import the env.py file and add the SECRETKEY and DATABASE_URL file paths.
- Comment out the default database configuration.
- Save files and make migrations.
- Add Cloudinary URL to env.py
- Add the cloudinary libraries to the list of installed apps.
- Add the STATIC files settings - the url, storage path, directory path, root path, media url and default file storage path.
- Link the file to the templates directory in Heroku.
- Change the templates directory to TEMPLATES_DIR
- Add Heroku to the ALLOWED_HOSTS list the format ['app_name.heroku.com', 'localhost']

### Create files / directories
- Create requirements.txt file
- Create three directories in the main directory; media, storage and templates.
- Create a file named "Procfile" in the main directory and add the following: web: gunicorn project-name.wsgi

### Update Heroku Config Vars
Add the following Config Vars in Heroku:
- SECRET_KEY value 
- CLOUDINARY_URL
- PORT = 8000
- DISABLE_COLLECTSTATIC = 1

### Deploy
- NB: Ensure in Django settings, DEBUG is False
- Go to the deploy tab on Heroku and connect to GitHub, then to the required repository. 
- Scroll to the bottom of the deploy page and either click Enable Automatic Deploys for automatic deploys or Deploy Branch to deploy manually. Manually deployed branches will need re-deploying each time the repo is updated.
- Click View to view the deployed site.

The site is now live and operational.

***

### Forking the GitHub Repository
#

By forking the GitHub Repository you can make a copy of the original repository You can view and/or make changes without affecting the original repository by using the following steps...

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/) you would like to fork.

![GitHub Repository](./readme-content/images/github-locate-repository.webp)

2. At the top of the Repository, just above the "Settings" Button on the menu, locate the "Fork" Button and you should now have a copy of the original repository in your account.

![GitHub Fork](./readme-content/images/github-fork.webp)

### Cloning this repository
#

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/).
![GitHub Repository](./readme-content/images/github-locate-repository.webp)

2. On the repository main page, click the drop-down menu called Code.

    ![GitHub Code Drowndown menu](./readme-content/images/github-clone.webp)

3. To clone the repository using HTTPS, copy the link.

    ![GitHub copy URL](./readme-content/images/github-copy-url.webp)

4. Open Git Bash
5. Change the current working directory to the location where you want the cloned directory to be made.
6. Type `git clone`, and then paste the URL you copied in Step 3.


7. Press Enter. Your local clone will be created.

***
## Languages Used
#

  [![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)](https://en.wikipedia.org/wiki/Python_(programming_language))

   [![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)](https://en.wikipedia.org/wiki/HTML)

   [![CSS3](https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white)](https://en.wikipedia.org/wiki/CSS)

## Programs, Frameworks & Libraries Used
#



## Credits
#

- [Django Docs](https://docs.djangoproject.com/en/4.0/)
- [Bootstrap 4.6 Docs](https://getbootstrap.com/docs/4.6/getting-started/introduction/)
- [Code Institute - Blog Walkthrough Project](https://github.com/Code-Institute-Solutions/)

***

## Acknowledgments
#

