# Kitchen Tales



The live link can be found here - [Kitchen Tales](https://)

![Am i responsive]()

## Contents

- [Kitchen Tales](#kitchen-tales)
  * [Objective](#objective)
  * [Brief & Target Audience](#brief)
  * [User Experience (UX)](#user-experience-ux)
    + [Epics](#epics)
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
    - [Programs](#programs)
    - [Frameworks](#frameworks)
    - [Libraries](#libraries)
  - [Development](#development)
    - [GitHub](#github)
    - [Django](#django)
  * [Deployment](#deployment)
    - [Heroku](#heroku)
    - [ElephantSQL](#elephant-sql)
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

### Epics 
#
7 Epics were created as Milestones which were then further developed into 42 User Stories. The details on each epic, along with the user stories linked to each one can be found [here](https://github.com/chris-townsend/PP4-Kitchen_Tales/milestones).

[1.](https://github.com/chris-townsend/PP4-Kitchen_Tales/milestone/1) Early Deployment 

[2.](https://github.com/chris-townsend/PP4-Kitchen_Tales/milestone/2) Initial Django Setup

[3.](https://github.com/chris-townsend/PP4-Kitchen_Tales/milestone/3) Website Functionality

[4.](https://github.com/chris-townsend/PP4-Kitchen_Tales/milestone/4) Navigation

[5.](https://github.com/chris-townsend/PP4-Kitchen_Tales/milestone/5) User Recipe Management

[6.](https://github.com/chris-townsend/PP4-Kitchen_Tales/milestone/6) User Account Management

[7.](https://github.com/chris-townsend/PP4-Kitchen_Tales/milestone/7) Admin Features & Owner Objectives

### User Stories
#
From the Epics, 42 User stories were developed. Some of my initial user stories were based around setting up the environment and deploying early. Each story was assigned a classification of must-have, should-have, could-have or won't have. Each story was also assigned user story points, based on my best estimation of the difficulty/time of completing each story. I gave the project a total of 



#### EPIC | **Early Deployment**
#

[#1](https://github.com/chris-townsend/PP4-Kitchen_Tales/issues/1) **Create Heroku App** - *As a **developer**, I can create an account with Heroku to process setting up the app** so that **I can deploy my site to Heroku***

[#2](https://github.com/chris-townsend/PP4-Kitchen_Tales/issues/2) **Create Config Vars & static files** - *As a **developer**, I can **add my config vars to my app in Heroku** so that **I can allow deployment to production**

[#3](https://github.com/chris-townsend/PP4-Kitchen_Tales/issues/3) **Create Procfile** - *As a **developer**, I can **create a Procfile within my project** so that **the application will run in Heroku***

[#4](https://github.com/chris-townsend/PP4-Kitchen_Tales/issues/4) **Cloudinary Setup** - *As a **developer**, I can **create a Cloudinary account** so that **I can store my media files***

[#5](https://github.com/chris-townsend/PP4-Kitchen_Tales/issues/5) **Deploy using GitHub** - *As a **developer**, I can **connect my GitHub account for the final deployment stages** so that **I can allow deployment to production***


#### EPIC | **Initial Django Setup**
#

[#6](https://github.com/chris-townsend/PP4-Kitchen_Tales/issues/6) **Django Setup** - *As a **developer**, I can **set up Django and supporting libraries** so that **I can start developing the site***

[#7](https://github.com/chris-townsend/PP4-Kitchen_Tales/issues/7) **Django Secure my secret keys** - *As a **developer**, I want to **set up my environment to secure my private keys** so that **I do not expose them in an insecure way***

[#8](https://github.com/chris-townsend/PP4-Kitchen_Tales/issues/8) **Install Django-allauth** - *As a **developer**, I should **install the necessary Django components** so that **I can address authentication, registration, and account management for users***

[#9](https://github.com/chris-townsend/PP4-Kitchen_Tales/issues/9) **Install Django-crispy-forms** - *As a **developer**, I should **install the necessary Django components** so that **I can display a comments section that is more appealing to the user***

[#40](https://github.com/chris-townsend/PP4-Kitchen_Tales/issues/40) **Create a database** - *As a **developer**, I should **set up the necessary database items** so that **the database is viewable through Heroku***


#### EPIC | Website Functionality
#

[#10](https://github.com/chris-townsend/PP4-Kitchen_Tales/issues/10) **Simple page design** - *As a **first-time user**, I can **immediately understand the purpose of the website**, and I know if it's **what I'm looking for***

[#11](https://github.com/chris-townsend/PP4-Kitchen_Tales/issues/11) **View a recipe** - *As a **user**, I can **view recipes**, without having to sign-up to **enjoy the site's content***

[#12](https://github.com/chris-townsend/PP4-Kitchen_Tales/issues/12) **View most liked recipes** - *As a **User**, I can **view the most liked recipes** so that **I can find inspiration and find out which recipes are the most popular***

[#13](https://github.com/chris-townsend/PP4-Kitchen_Tales/issues/13) **Responsive on a mobile device** - *As a **User**, I can **view recipes on my mobile** so that **I don't have to rely on using a computer***

[#34](https://github.com/chris-townsend/PP4-Kitchen_Tales/issues/34) **View comments** - *As a **User**, I can **view comments on recipes** so that I can **read other user's feedback***

[#35](https://github.com/chris-townsend/PP4-Kitchen_Tales/issues/35) **Comment on a recipe** - *As a **Logged-in User**, I can **comment on recipes** so that **I can leave my feedback for others***

[#37](https://github.com/chris-townsend/PP4-Kitchen_Tales/issues/37) **Contact the site owner** - *As a **User**, I can **contact the site owner** so that **I can offer my feedback***

[#41](https://github.com/chris-townsend/PP4-Kitchen_Tales/issues/41) **Create a favicon** - *As a **developer**, I can **add a favicon** so that **the site looks more distinguishable***


#### EPIC | Navigation
#

[#14](https://github.com/chris-townsend/PP4-Kitchen_Tales/issues/14) **Site Navigation** - *As a **User**, I can **navigate around the site** so that **I can easily view desired content***

[#15](https://github.com/chris-townsend/PP4-Kitchen_Tales/issues/15) **Search for a recipe** - *As a **User**, I can **search for the desirable recipe by keyword** so that **I can find a specific recipe fast***


#### EPIC | User Recipe Management
#

[#16](https://github.com/chris-townsend/PP4-Kitchen_Tales/issues/16) **Create a recipe** - *As a **logged-in User**, I can **create recipes** so that **I can add them to the site**

[#17](https://github.com/chris-townsend/PP4-Kitchen_Tales/issues/17) **View my recipes** - *As a **logged-in User**, I can **view all the recipes that I have created** so that **I can go back to them at a later date***

[#18](https://github.com/chris-townsend/PP4-Kitchen_Tales/issues/18) **Update/Edit my recipes** - *As a **logged-in User**, I can **update and edit my recipes** so that I can **update any changes or mistakes that I have made***

[#19](https://github.com/chris-townsend/PP4-Kitchen_Tales/issues/19) **Delete a recipe** - *As a **logged-in User**, I can **delete any personal recipes** so that I can **remove them if necessary***

[#20](https://github.com/chris-townsend/PP4-Kitchen_Tales/issues/20) **Rate a recipe** - *As a **logged-in User** I can **give a recipe a rating so that I can provide feedback***

[#21](https://github.com/chris-townsend/PP4-Kitchen_Tales/issues/21) **Print a recipe** - *As a **User**, I would **like the option to print a recipe** so that **I can have a paper copy***

[#39](https://github.com/chris-townsend/PP4-Kitchen_Tales/issues/39) **View my liked recipes** - *As a **logged-in user** I can **view my liked recipes** so that **I can return to them easily***

[#42](https://github.com/chris-townsend/PP4-Kitchen_Tales/issues/42) **Like a recipe** - *As a **logged-in User**, I can **like or star a recipe** so that **I can bookmark it for later***


#### EPIC | User Account Management
#

[#22](https://github.com/chris-townsend/PP4-Kitchen_Tales/issues/22) **Register for an account** - *As a **User**, I can **register for an account** so that I can **interact with the site content***

[#23](https://github.com/chris-townsend/PP4-Kitchen_Tales/issues/23) **Register for an account using my social media** - *As a **User**, I can **register for an account by using one of my social media accounts** so that **I can use an alternative method of signing up***

[#24](https://github.com/chris-townsend/PP4-Kitchen_Tales/issues/24) **Login to my account** - *As a **User**, I can **log into my account** so that I can **manage my recipes***

[#25](https://github.com/chris-townsend/PP4-Kitchen_Tales/issues/25) **Logout of my account** - *As a **User**, I can **safely log out of my account** so that **I can disconnect from the site***

[#26](https://github.com/chris-townsend/PP4-Kitchen_Tales/issues/26) **Login status** - *As a **logged-in User**, I can **see my login status** so that **I know if I am logged in or out of my account***

[#27](https://github.com/chris-townsend/PP4-Kitchen_Tales/issues/27) **Change my password** - *As a **logged-in User**, I can **change my password** so that **I can keep my account secure***


#### EPIC | Admin Features & Owner Objectives
#

[#28](https://github.com/chris-townsend/PP4-Kitchen_Tales/issues/28) **Admin CRUD features** - *As a **Site admin**, I can **create, edit and delete recipes and comments** so that **I can control the site content**

[#29](https://github.com/chris-townsend/PP4-Kitchen_Tales/issues/29) **Authorize recipes and comments** - *As a **Site admin**, I can **authorize recipes and comments** so that **I can review the content before it's made public***

[#30](https://github.com/chris-townsend/PP4-Kitchen_Tales/issues/30) **Add a captcha for sign-up** - *As a **Site Admin**, I would like to **ensure that my site users are real** so that **I can prevent any spam content***

[#31](https://github.com/chris-townsend/PP4-Kitchen_Tales/issues/31) **Display my social icons** - *As a **Site owner**, I would like to **display my social icons** so that I can **promote my other channels***

[#32](https://github.com/chris-townsend/PP4-Kitchen_Tales/issues/32) **Populate a recipe database using an API** - *As a **Site owner**, I can **provide a database of existing recipes** so that **I can provide my users with content***

[#33](https://github.com/chris-townsend/PP4-Kitchen_Tales/issues/33) **Offer a subscription service** - *As a **Site owne**r, I can **offer exclusive content** by creating a **subscription service for a small fee***

[#36](https://github.com/chris-townsend/PP4-Kitchen_Tales/issues/36) **Comment approval** - *As a **Logged-in User** who has posted a comment, **I would like to know if it's been approved or not** so that **I can see if it's being displayed on the site***

[#38](https://github.com/chris-townsend/PP4-Kitchen_Tales/issues/38) **Ban a user** - *As a **Site admin**, I can **ban a user** so that **they are blocked if they violate the site rules***


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

- 400 Bad Request - unable to handle this request.
- 403 Page Forbidden - Looks like you're trying to access forbidden content. Please log out and sign in to the correct account.
- 404 Page Not Found - The page you're looking for doesn't exist.
- 500 Server Error - Kitchen Tales is currently unable to handle this request

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


- 400 Bad Request - unable to handle this request.
- 403 Page Forbidden -
- 404 Page Not Found - 
- 500 Server Error - 

***

### Future Features
#
***


# Development

This site was made using [GitHub](#github) & [Gitpod](https://www.gitpod.io/). The site was further developed using [Django](#django), a Python web-framework.

## GitHub

### Create the repository
#

1. Sign into Github and navigate to [Code Institute's Gitpod template](https://github.com/Code-Institute-Org/gitpod-full-template).
![GitHub Code Institute template](static/images/github-use-this-template.webp)
 - At the top of the repository click **Use this template** followed by **Create a new repository**.
 ![GitHub Code Institute template](static/images/github-create-new-repository.webp)

*Alternatively:*

1. Click the GitHub label in the top left of the nav section.
![GitHub create repository](static/images/github-label.webp)

2. Select **New** next to **Top Repositories**.     
![GitHub click new repository](static/images/github-new.webp)

3. Select the **template** you wish to use.                
![GitHub select template](static/images/github-select-template.webp)

4. Give the repository a name and description and then click **Create repository**.
![GitHub create repository](static/images/github-create-repository.webp)

The repository has now been created and is ready for editing through the gitpod terminal.
 
***

## Django

### Installing Django and supporting libraries
#


To initialise a Django project, first Django must be installed within your Python environment. This is done via the command ``pip3 install 'django<4' gunicorn``

**Django 3.2 is the LTS (Long Term Support) version of Django and is therefore preferable to use over the newest Django 4.**

**1.** Install Django and gunicorn: ``pip3 install 'django<4' gunicorn``

- Gunicorn is the server we want to run our project on Heroku.

**2.** Install supporting libraries: ``pip3 install dj_database_url==0.5.0 psycopg2``

- Needed to connect to the PostgresSQL database but later gets transferred to elephantSQL.

**3.** Install Cloudinary libraries: ``pip3 install dj3-cloudinary-storage``

- Cloudinary will be used to store our static media files.

**4.** Create a ``requirements.txt`` file: ``pip3 freeze --local > requirements.txt``

**The ``requirements.txt`` file contains all the applications and dependencies that are required to run the application.**

**5.** Create a Django project (*kitchentales*): ``django-admin startproject 'PROJ_NAME' .`` 
**(Don’t forget the ``.`` at the end of the project name to tell Django admin we want to create our project in the current directory.)**

 - This should have created a new directory called your ``'PROJ_NAME'`` and a ``manage.py`` file. Wthin your project folder you should see the file settings and URL files added to the directory.

**6.** Create an App name (*recipes*): ``python3 manage.py startapp 'APP_NAME'``

- Now the App has been installed, you need to add it to your ``INSTALLED_APPS`` within ``settings.py``

 - ``INSTALLED_APPS = [
    …
    'recipes',
]``

**7.** Save changes and then **Migrate changes** in the terminal - ``python3 manage.py migrate``

- Whenever a new app is created, migrations are automatically created and these changes need migrating. By migrating the changes, it adds all of the changes to the database.

**8.** Run the server and you should see the basic skeleton project up and running - ``python3 manage.py runserver``

![Django successful set-up](static/images/django-success.webp)

### Attaching the Database
#

Create a new env.py file at the top level directory - ``env.py``

#### - Within ``env.py``:

| Instruction | Code |
| --- | --- |
| **1.** Import os library | ``import os`` |
| **2.** Set environment variables | ``os.environ["DATABASE_URL"] = "Paste in Heroku DATABASE_URL Link"`` |
| **3.** Add in secret key | ``os.environ["SECRET_KEY"] = "Make up your own randomSecretKey"`` |

 ### Prepare the environment and settings.py
 #

 #### - Within ``settings.py``:

 | Instruction | Code |
| --- | --- |
| **1.** Reference env.py | `` import os``<br> ``import dj_database_url``<br> ``if os.path.isfile("env.py"): import env``|
| **2.** Remove the insecure secret key **and replace** | ``SECRET_KEY = os.environ.get('SECRET_KEY')``|
| **3.** Comment out the old ``DATABASES`` section | ``#DATABASES = {``<br>``#'default': {``<br>``#'ENGINE': 'django.db.backends.sqlite3',``<br>  ``#'NAME': BASE_DIR / 'db.sqlite3',``<br>``#}``<br>``#}`` |
| **4.** Add new ``DATABASES`` Section | ``DATABASES = {'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))}`` |

- Save all files and now make migrations to complete the changes - ``python3 manage.py migrate``

### Get our static and media files stored on Cloudinary
#

**- Within your [Cloudinary](https://cloudinary.com/users/login#gsc.tab=0) dashboard:**

| Instruction | Code |
| --- | --- |
| **1.** Copy your CLOUDINARY_URL e.g. API environment variable | **From your Cloudinary dashboard** |

#### **- Within ``env.py``:**

| Instruction | Code |
| --- | --- |
| **1.** Add Cloudinary URL to ``env.py`` - be sure to paste in the correct section of the link | ``os.environ["CLOUDINARY_URL"] = "cloudinary://************************"`` |


#### **- Within your [Heroku](https://id.heroku.com/login) dashboard:**

| Instruction | Code |
| --- | --- |
| **1.** Add Cloudinary URL to Heroku Config Vars | Add to Settings tab in Config Vars e.g. ``COUDINARY_URL, cloudinary://************************`` |
| **2.** Add ``DISABLE_COLLECTSTATIC`` to Heroku Config Vars (temporary step which will be removed before deployment) | ``DISABLE_COLLECTSTATIC = 1``

#### **- Within ``settings.py``:**

| Instruction | Code |
| --- | --- |
| **1.** Add Cloudinary Libraries to installed apps | ``INSTALLED_APPS = […,'cloudinary_storage','django.contrib.staticfiles','cloudinary', …,]`` |
| **2.** Tell Django to use Cloudinary to store media and static files - *Place under the Static files* | ``STATIC_URL = '/static/'``<br> ``STATICFILES_STORAGE = 'cloudinary_storage.storage.StaticHashedCloudinaryStorage'``<br>``STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]``<br>``STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')``<br>``MEDIA_URL = '/media/' ``<br>``DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'`` |
| **3.** Link file to the templates directory in Heroku - Place under the ``BASE_DIR`` | ``TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')`` |
| **4.** Change the templates directory to ``TEMPLATES_DIR`` - Place within the ``TEMPLATES`` array | ``TEMPLATES = [``<br>``{``<br>``…,``<br>``'DIRS': [TEMPLATES_DIR],``<br>``…,``<br>``],``<br>``},``<br>``},``<br>``]``<br>
| **5.** Add Heroku Hostname to ``ALLOWED_HOSTS`` *(e.g. kitchentales)* | ``ALLOWED_HOSTS = ["PROJ_NAME.herokuapp.com", "localhost"]`` |

#### **Within Gitpod:**

1. Create three new folders at the top level directory - ``media``, ``static`` & ``templates``.

2. Create a file named **Procfile** at the top level directory - ``Procfile``.

    - Add the following code: ``web: gunicorn PROJ_NAME.wsgi``

**The Procfile must live in your app’s root directory. It does not function if placed anywhere else.**

*The purpose of the Procfile is a mechanism for declaring what commands are run by your application’s dynos on the Heroku platform.*


***
# Deployment

## Heroku

To deploy this page to Heroku from its GitHub repository, the following steps were taken:

### Create the Heroku App:
#

1. Log in to [Heroku](https://dashboard.heroku.com/apps) or create an account.
![Heroku Signup](static/images/heroku-signup.webp)

2. On your Heroku dashboard, click the button labelled **New** in the top right corner and from the drop-down menu select **Create new app**.
![Heroku Dashboard](static/images/heroku-dashboard.webp)
![Create new app](static/images/heroku-create-app.webp)

3. Enter a **unique and meaningful app name** and **choose the region** which is best suited to your location.
![Meaningful app-name](static/images/heroku-meaningful-name.webp)
- Click on the **Create app** button.

4. Select **Settings** from the tabs at the top of the app page.
![Heroku app settings](static/images/heroku-dashboard-settings.webp)

5. Click **Reveal Config Vars**.    
![Heroku app settings](static/images/heroku-config-vars.webp)

6. Input all key-value pairs from the `env.py` file. Ensure `DEBUG` and `DISABLE_COLLECTSTATIC` are not included in the final production.
![Heroku app settings](static/images/heroku-config-var-setup.webp)

| KEY | VALUE |
| --- | --- |
|``DATABASE_URL``|=  ``****``  |
|``SECRET_KEY``  |=  ``****``  |
|``CLOUDINARY_URL`` |=  ``****``  |
|``PORT``  |= `8000` |
|``DISABLE_COLLECTSTATIC``  |=  ``1`` |


7. Below your Config Vars in your app settings, click **Add buildpack**.
![Heroku add buildpack](static/images/heroku-add-buildpack.webp)

8. Select **Python** from the list of buildpacks.
![Heroku select buildpack](static/images/heroku-select-buildpack.webp)
- Remember to click **Save changes**.

9. Select **Deploy** from the tabs at the top of the app page.
![Heroku deploy](static/images/heroku-deploy.webp)

10. Select **Connect to GitHub** from the deployment methods.
![Heroku deployment method](static/images/heroku-deployment-method.webp)

11. Search for the repository to connect to by name.
![Heroku select repository](static/images/heroku-select-repository.webp)

12. Click **Connect**.
![Heroku click connect](static/images/heroku-connect-to-github.webp)

 - Your app should now be connected to your GitHub account.

![Heroku connected app](static/images/heroku-connected-app.webp)

 13. Select **Enable Automatic Deploys** for automatic deployments.

![Heroku automatic deploy](static/images/heroku-automatic-deploys.webp)

- If you would like to deploy manually, select **Deploy Branch**. If you manually deploy, you will need to re-deploy each time the repository is updated.

![Heroku manual deploy](static/images/heroku-manual-deploy.webp)

- For the first time deploying to Heroku you may have to deploy manually but if you select automatic deploys it will update from then onwards.

14. Click **View** to view the deployed site.
![Heroku successful deploy](static/images/heroku-successful-deploy.webp)

***
## Elephant SQL

Heroku announced in September 2022 that they would be ending their free tier hosting at the end of November 2022. As I am a student who is currently registered with the GitHub Student Developer Pack, I can apply for the Heroku credits. The Heroku credits allowed me to transfer my projects from free dynos to Eco dynos to ensure that they continue to work. Unfortunately the student offer does not include the postgres add-on being used to host my postgres database. Code Insitute therefore have recommended students to migrate their databases to a new provider. In this case its ElephantSQL, as they are free. The ``DATABASE_URL`` value now points to the elephantSQL database in my Heroku Config Vars.

As the database provided by Django is only accessible within Gitpod and is not suitable for a production environment. The deployed project on Heroku will not be able to access it. So, you need to create a new database that can be accessed by Heroku. The following steps will create a new PostgreSQL database instance for use within the project.

### Create & attach the Elephant SQL database
#

1. Log in to [ElephantSQL](https://customer.elephantsql.com/instance#) to access your dashboard.
![Elephant SQL dashboard](static/images/elephant-sql-dashboard.webp)

2. Click **Create New Instance** at the top right of the page.        
![Elephant SQL new instance](static/images/elephant-create-new-instance.webp)

3. Set up your **plan**.
- Give your plan a **Name** (this is commonly the name of the project)
- Select the **Tiny Turtle (Free)** plan
- You can leave the **Tags** field blank

![Elephant SQL setup plan](static/images/elephant-setup-plan.webp)

4. Click **Select Region**.        
![Elephant SQL select region](static/images/elephant-select-region.webp)

5. Select a **data center** near you.
![Elephant SQL select data center](static/images/elephant-select-data-center.webp)

6. Click **Review**.                 
![Elephant SQL review data center](static/images/elephant-review-data.webp)

7. Ensure your details are correct and then click **Create instance**.
![Elephant SQL confirm instance](static/images/elephant-confirm-instance.webp)

8. Return to the **ElephantSQL dashboard** and you should see your **database instance name** for this project.
![Elephant SQL dashboard instance](static/images/elephant-dashboard-instance.webp)

9. On your **ElephantSQL dashboard**, click on the **database instance name** for this project.  
![Elephant SQL click instance](static/images/elephant-click-instance.webp)

10. In the **URL section**, click the **copy icon** to copy the **database URL**.
![Elephant SQL copy URL](static/images/elephant-copy-url.webp)

11. Within your **Heroku app**, add `DATABASE_URL` as the `KEY` and paste the URL you just copied in **ElephantSQL** into the `VALUE` column. Your **ElephantSQL** database should now be connected to your **Heroku** app.
![Elephant SQL add database URL ](static/images/elephant-add-database-url.webp)

***

### Forking the GitHub Repository
#
By forking the GitHub Repository you can make a copy of the original repository. You can view and/or make changes without affecting the original repository by using the following steps..

**1.** Log in to GitHub and locate the [GitHub Repository](https://github.com/) you would like to fork.

![GitHub Repository](static/images/github-select-repository.webp)

**2.** At the top of the Repository, just above the **Tabs**, locate the **Fork** Button and you should now have a copy of the repository in your account.

![GitHub Fork](static/images/github-fork-repository.webp)

### Cloning this repository
#
**1.** Log in to GitHub and locate the [GitHub Repository](https://github.com/).
![GitHub Repository](static/images/github-select-repository.webp)

**2.** On the repository main page, click the drop-down menu called Code.

![GitHub Code Drowndown menu](static/images/github-clone-repository.webp)

**3.** To clone the repository using HTTPS, copy the link.

![GitHub copy URL](static/images/github-copy-url.webp)

**4.** Open Git Bash

**5.** Change the current working directory to the location where you want the cloned directory to be made.

**6.** Type `git clone`, and then paste the URL you copied in Step 3.

**7.** Press Enter. Your local clone will be created.

***
## Languages Used
#

  [![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)](https://en.wikipedia.org/wiki/Python_(programming_language))

   [![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)](https://en.wikipedia.org/wiki/HTML)

   [![CSS3](https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white)](https://en.wikipedia.org/wiki/CSS)

***

## Programs, Frameworks & Libraries Used
#

### Programs
#
[**Balsamiq**](https://balsamiq.com/) - Balsamiq was used to create the basic wireframes during the design process.

[**Pixlr**](https://pixlr.com/x/) - Pixlr was used to resize and change the format of my images.

[**Google DevTools**](https://developer.chrome.com/docs/devtools/) - Once the website was made to a basic deployment level, Google DevTools was used frequently to resize objects within the site, very helpful for making my website responsive.

[**Python Tutor**](https://pythontutor.com/) - Python Tutor was used for helping step through non-functioning code and resolve issues.

[**Git**](https://git-scm.com/) - Git was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub.

[**GitHub**](https://github.com/) - GitHub is used to store the project's code after being pushed from Git.

[**Heroku**](http://heroku.com/) - Heroku is a cloud platform that lets people build, deliver, monitor, and scale apps. It supports several programming languages. Heroku was used for the deployment of this project.

[**W3C Markup Validator**](https://validator.w3.org/) - This site was used to ensure that my HTML and CSS were error-free. I had to push my code to ensure it was updated and then add the URL of the website to the address bar which then checked for errors or warnings.

[**Favicon Generator**](https://favicon.io/favicon-converter/) - This was used to create my favicon icon. 

[**JSHint Validator**](https://jshint.com/) - Jshint was used to validate the JavaScript code. It shows any warnings and errors within my code. 

[**PEP8 Validator**](http://pep8online.com/) - The PEP8 validator was used to validate my python code, you can paste your code or upload the file to see the results. It's built with a backend Python framework called Flask. 

[**Cloudinary**](https://imgpile.com/) - A cloud hosting website, used for hosting my images.

[**DrawSQL**](https://drawsql.app/) - DrawSQL is a database diagram tool which was used to visualize relationship diagrams for my databases.

#
### Frameworks
#

[**Django 3.2**](https://www.djangoproject.com/) - A high-level Python web framework that encourages rapid development and clean, pragmatic design.
#

### Libraries 
#

[**Bootstrap 4.6**](https://getbootstrap.com/docs/4.6/getting-started/introduction/) - Bootstrap provides a popular framework for building responsive mobile-first sites with built-in CSS & Javascript libraries.

[**Psycopg2**](https://pypi.org/project/psycopg2/) - A PostgreSQL database adapter for Python.

[**dj-database-url**](https://pypi.org/project/dj-database-url/) - A simple Django utility that allows you to create an environment variable to configure your Django application.

[**Gunicorn**](https://gunicorn.org/) - Gunicorn 'Green Unicorn' is a Python WSGI HTTP Server.

[**django-all-auth**](https://github.com/pennersr/django-allauth) Integrated set of Django applications addressing authentication, registration, account management as well as 3rd party *social* account authentication.

[**django-crispy-forms**](https://django-crispy-forms.readthedocs.io/en/latest/) Used to control the rendering behaviour of my django forms.

[**django-cloudinary-storage**](https://pypi.org/project/django-cloudinary-storage/) Facillitates integration with  Cloudinary by implementing a Django Storage API. This is to enable storage of static and media files.


#
## Credits
#

- [Django Docs](https://docs.djangoproject.com/en/4.0/)
- [Bootstrap 4.6 Docs](https://getbootstrap.com/docs/4.6/getting-started/introduction/)
- [Code Institute - Blog Walkthrough Project](https://github.com/Code-Institute-Solutions/)

***

## Acknowledgments
#

