# Testing

### Contents
- [Testing Stories for UX](#testing-user-stories-from-the-user-experience-ux-section)
- [Validator Testing](#validator-testing)
  * [HTML](#html)
  * [CSS](#css)
  * [Javascript](#javascript)
  * [Python](#python)
  * [Lighthouse](#lighthouse)
  * [WAVE accessibility tool](#wave-accessibility-evaluation-tool)
- [Browser Testing](#browser-testing)
- [Device Testing](#device-testing)
  * [Mobile](#mobile)
- [Manual Testing](#manual-testing)
  * [Navigation](#navigation)
  * [Homepage](#homepage-content)
  * [Footer](#homepage---footer)
  * [All Recipes](#recipes)
  * [Recipe Detail](#recipe-detail)
  * [My Recipes](#my-recipes)
  * [My Starred Recipes](#my-starred-recipes)
  * [Django allauth pages](#django-all-auth-pages)
  * [Add Recipe](#add-recipe)
  * [Update Recipe](#update-recipe)
  * [Delete Recipe](#delete-recipe)
  * [Update Comment](#update-comment)
  * [Delete Comment](#delete-comment)
  * [Newsletter Page](#newsletter)
- [Bugs](#bugs)
  * [Fixed Bugs](#fixed-bugs)
  * [Unfixed Bugs](#unfixed-bugs)
- [Automated Testing](#automated-testing)
  * [`test_forms.py`](https://github.com/chris-townsend/PP4-Kitchen_Tales/blob/main/recipes/test_forms.py)
  * [`test_models.py`](https://github.com/chris-townsend/PP4-Kitchen_Tales/blob/main/recipes/test_models.py)
  * [`test_views.py`](https://github.com/chris-townsend/PP4-Kitchen_Tales/blob/main/recipes/test_views.py)
<br>

*Please note: To open any external links in a new browser tab, please press **CTRL + Click***

***

## Testing User Stories from the User Experience (UX) Section

### EPIC | *Early Deployment*
<br>

*[As a developer, I can create an account with Heroku to process setting up the app so that I can deploy my site to Heroku](https://github.com/chris-townsend/PP4-Kitchen_Tales/issues/1)*

![Create Heroku account](docs/testing/user-testing/heroku-create-account.webp)

- ***Detailed information about setting up Heroku can be found [here](/README.md#heroku)***

*[As a developer, I can add my config vars to my app in Heroku so that I can allow deployment to production](https://github.com/chris-townsend/PP4-Kitchen_Tales/issues/2)*

![Heroku config vars input](docs/testing/user-testing/heroku-config-vars.webp)
![Add heroku config vars](docs/testing/user-testing/heroku-config-var-setup.webp)

- ***Information about setting up the config vars within Heroku can be found [here](/README.md#create-the-heroku-app)***

*[As a developer, I can create a Procfile within my project so that the application will run in Heroku](https://github.com/chris-townsend/PP4-Kitchen_Tales/issues/3)*

![Create Procfile](docs/testing/user-testing/kitchen-tales-create-procfile.webp)

- ***Information about setting up the Procfile can be found within the [Django](/README.md#within-gitpod) section of the readme***

*[As a developer, I can create a Cloudinary account so that I can store my media files](https://github.com/chris-townsend/PP4-Kitchen_Tales/issues/4)*

![Create Cloudinary account](docs/testing/user-testing/create-cloudinary-account.webp)

- ***Information about setting up the Cloudinary account can be found [here](/README.md#installing-django-and-supporting-libraries)***

*[As a developer, I can connect my GitHub account for the final deployment stages so that I can allow deployment to production](https://github.com/chris-townsend/PP4-Kitchen_Tales/issues/5)*

![Connect GitHub account](docs/testing/user-testing/heroku-deployment-method.webp)

- ***Information about connecting my GitHub account through Heroku can be found [here](/README.md#create-the-heroku-app)***

#

### EPIC | *Initial Django Setup*
<br>

*[As a developer, I can set up Django and supporting libraries so that I can start developing the site](https://github.com/chris-townsend/PP4-Kitchen_Tales/issues/6)*

![Setup Django](docs/testing/user-testing/heroku-connected-app.webp)

- ***Detailed information about the initial Django setup can be found [here](/README.md#installing-django-and-supporting-libraries) within the Django section of the README.md***

*[As a developer, I want to set up my environment to secure my private keys so that I do not expose them in an insecure way](https://github.com/chris-townsend/PP4-Kitchen_Tales/issues/7)*

- ***Information about setting up the environment safely can be found [here](/README.md#installing-django-and-supporting-libraries)***

*[As a developer, I should install the necessary Django components so that I can address authentication, registration, and account management for users](https://github.com/chris-townsend/PP4-Kitchen_Tales/issues/8)*

- ***Information about installing Django and supporting libraries can be found [here](/README.md#installing-django-and-supporting-libraries)***

*[As a developer, I should install the necessary Django components so that I can display a comments section that is more appealing to the user](https://github.com/chris-townsend/PP4-Kitchen_Tales/issues/9)*

- ***Information about installing Django components can be found [here](/README.md#installing-django-and-supporting-libraries)***

*[As a developer, I should set up the necessary database items so that the database is viewable through Heroku](https://github.com/chris-townsend/PP4-Kitchen_Tales/issues/40)*

- ***Information about setting up the ElephantSQL database can be found [here](/README.md#elephant-sql)***

#

### EPIC | *Website Functionality*
<br>

*[As a first-time user, I can immediately understand the purpose of the website, and I know if it's what I'm looking for](https://github.com/chris-townsend/PP4-Kitchen_Tales/issues/10)*

![Kichen Tales welcome message](docs/testing/user-testing/kitchen-tales-welcome.webp)

- The 'Welcome to Kitchen Tales' section when you first arrive on the homepage should be enough for users to understand the concept of the website. There is a button to sign up to create an account and share recipes and also a relatable image of some cooked dishes and a menu.

*[As a User, I can view recipes, without having to sign-up to enjoy the site's content](https://github.com/chris-townsend/PP4-Kitchen_Tales/issues/11)*

![Kichen Tales recipes tab](docs/testing/user-testing/kitchen-tales-recipes-tab.webp)

- Any user can view all recipes from the recipes tab in the nav section at the top of every page.

![Kichen Tales recipes](docs/testing/user-testing/kitchen-tales-recipes.webp)

*[As a User, I can view recipes on my mobile so that I don't have to rely on using a computer](https://github.com/chris-townsend/PP4-Kitchen_Tales/issues/13)*

![Kichen Tales mobile friendly recipe](docs/testing/user-testing/kitchen-tales-mobile-recipe.webp)

- The site was tested on a variety of devices to ensure it was mobile-friendly, please click [here](/TESTING.md#device-testing) to view a full list of tested devices.

![Kichen Tales mobile friendly test](docs/testing/user-testing/kitchen-tales-mobile-friendly-test.webp)

***For more detailed information about mobile testing, please click [here](#device-testing)***

*[As a User, I can view comments on recipes so that I can read other user's feedback](https://github.com/chris-townsend/PP4-Kitchen_Tales/issues/34)*

![Kichen Tales comment section](docs/testing/user-testing/kitchen-tales-comment-section.webp)

- The comments section is displayed below each recipe on a recipe detail page. Any user can view comments but you must be logged in to post, edit and delete comments.

*[As a Logged-in User, I can comment on recipes so that I can leave my feedback for others](https://github.com/chris-townsend/PP4-Kitchen_Tales/issues/35)*

![Kichen Tales comment section](docs/testing/user-testing/kitchen-tales-leave-comment.webp)

- When a user is logged in, a text field will be displayed for the user to post a comment.

*[As a developer, I can add a favicon so that the site looks more distinguishable](https://github.com/chris-townsend/PP4-Kitchen_Tales/issues/41)*

![Kichen Tales tab](docs/testing/user-testing/kitchen-tales-tab.webp)

![Kichen Tales favicon](docs/testing/user-testing/kitchen-tales-favicon-large.webp)

- A favicon has been created using [favicon.io](https://favicon.io/) to make the site look more distinguishable and professional. The image is hosted on Cloudinary and linked in the head of the `base` template.

#

### EPIC | *Navigation*
<br>

*[As a User, I can navigate around the site so that I can easily view desired content](https://github.com/chris-townsend/PP4-Kitchen_Tales/issues/14)*

![Kichen Tales navbar](docs/testing/user-testing/kitchen-tales-navbar.webp)

![Kichen Tales navbar hover](docs/testing/user-testing/kitchen-tales-navbar-hover.webp)

- Utilizing *CSS's* hover effect, the user knows what tab they are clicking on as it underlines the heading when it's being hovered over. 

![Kichen Tales navbar authorized user](docs/testing/user-testing/kitchen-tales-navbar-auth-user.webp)

- A logged-in user can see their dropdown-menu options by clicking on their name with the user icon. This menu gives the option for a user to add a new recipe, see their created recipes, and their favourite starred recipes, and an option to log out of their account.

*[As a User, I can search for the desirable recipe by keyword so that I can find a specific recipe fast](https://github.com/chris-townsend/PP4-Kitchen_Tales/issues/15)*

![Kichen Tales search bar](docs/testing/user-testing/kitchen-tales-search-bar.webp)

- Any user can search for a recipe by using the search bar feature within the nav bar at the top of every page. 

![Kichen Tales searched results](docs/testing/user-testing/kitchen-tales-search-results.webp)

- The search results are fairly specific and it's currently set to search results by title so you might get slightly different results from using a capital letter vs not. With more time, I would like to add more searchable features to the site.

#

### EPIC | *User Recipe Management*
<br>

*[As a logged-in User, I can create recipes so that I can add them to the site](https://github.com/chris-townsend/PP4-Kitchen_Tales/issues/16)*

![Kichen Tales add recipe tab](docs/testing/user-testing/kitchen-tales-add-recipe-tab.webp)

- To create a new recipe, go to your drop-down menu from the nav section and select the 'Add-Recipe' tab. This will then redirect you to the `add_recipe` page which will allow a user to fill out the form and create a recipe. 

![Kichen Tales add recipe page](docs/testing/user-testing/kitchen-tales-add-recipe.webp)

![Kichen Tales add recipe text](docs/testing/user-testing/kitchen-tales-add-recipe-text.webp)

- A logged-in user can also add a new recipe from the homepage.

*[As a logged-in User, I can view all the recipes that I have created so that I can go back to them at a later date](https://github.com/chris-townsend/PP4-Kitchen_Tales/issues/17)*

![Kichen Tales my recipes tab](docs/testing/user-testing/kitchen-tales-my-recipes-tab.webp)

![Kichen Tales my recipes page](docs/testing/user-testing/kitchen-tales-my-recipes.webp)

- User-created recipes can be found easily by clicking on the drop-down menu within the nav section. After clicking on the My-Recipes tab, this will open up recipes created by the user.

*[As a logged-in User, I can update and edit my recipes so that I can update any changes or mistakes that I have made](https://github.com/chris-townsend/PP4-Kitchen_Tales/issues/18)*

![Kichen Tales update button on hover](docs/testing/user-testing/kitchen-tales-edit-button.webp)

- If the logged-in user is the author of the recipe, an edit button is shown next to the recipe image. When a user hovers over the edit button, it is displayed underlined.

![Kichen Tales update recipe page](docs/testing/user-testing/kitchen-tales-update-recipe.webp)

- Clicking the Edit tab will open the `update_recipe` page with the prepopulated data displayed.

*[As a logged-in User, I can delete any personal recipes so that I can remove them if necessary](https://github.com/chris-townsend/PP4-Kitchen_Tales/issues/19)*

![Kichen Tales delete recipe button on hover](docs/testing/user-testing/kitchen-tales-delete-button.webp)

- If the logged-in user is the author of the recipe, a delete button is shown next to the recipe image. When a user hovers over the delete button, it is displayed underlined.

![Kichen Tales delete recipe page](docs/testing/user-testing/kitchen-tales-delete-recipe-page.webp)

- Clicking the Delete tab will open the `delete_recipe` page which will give the user three options, Cancel - which will take you back to the recipe detail page. Update Instead - which will take you to the `update_recipe` page with the prepopulated data for that recipe and last, Delete Recipe, which will remove the recipe from the database and return you to a user's recipes.

*[As a logged-in User, I can view my liked recipes so that I can return to them easily](https://github.com/chris-townsend/PP4-Kitchen_Tales/issues/39)*

![Kichen Tales saved recipes tab](docs/testing/user-testing/kitchen-tales-saved-recipes-tab.webp)

- My liked recipes can be found by clicking on the drop-down menu within the nav section. After clicking on the Saved-Recipes tab, this will open logged-in users starred recipes.

![Kichen Tales liked recipes page](docs/testing/user-testing/kitchen-tales-liked-recipes-page.webp)

*[As a logged-in User, I can like or star a recipe so that I can bookmark it for later](https://github.com/chris-townsend/PP4-Kitchen_Tales/issues/42)*

![Kichen Tales like this recipe text and icon](docs/testing/user-testing/kitchen-tales-click-to-bookmark.webp)

- Click to bookmark this recipe and an outline of a star is displayed next to the recipe image and just below the image for mobile. A user can click the star icon and it will save the recipe to their saved recipes list. 

![Kichen Tales number of likes](docs/testing/user-testing/kitchen-tales-number-of-likes.webp)

- After a user has clicked the star icon, the recipe displays the total amount of stars received from all users.

#

### EPIC | *User Account Management*
<br>

*[As a User, I can register for an account so that I can interact with the site's content](https://github.com/chris-townsend/PP4-Kitchen_Tales/issues/22)*

![Kichen Tales sign up tab](docs/testing/user-testing/kitchen-tales-sign-up-tab.webp)

- Users can sign-up for an account by clicking on the drop-down menu MyAccount and then selecting **Register** from the list.

![Kichen Tales sign up button](docs/testing/user-testing/kitchen-tales-sign-up-button.webp)

- For users which are not logged in, a banner is displayed on the homepage which invites people to register to share recipes.

![Kichen Tales sign up text](docs/testing/user-testing/kitchen-tales-sign-up-text.webp)

- A user can also sign up by clicking on the text above which is displayed on a recipe detail page next to the star icon. 

*[As a User, I can log into my account so that I can manage my recipes](https://github.com/chris-townsend/PP4-Kitchen_Tales/issues/24)*

![Kichen Tales sign in tab](docs/testing/user-testing/kitchen-tales-sign-in.webp)

- Users can sign in to their account by clicking on the MyAccount dropdown menu and after clicking on Sign-in.

![Kichen Tales sign in page](docs/testing/user-testing/kitchen-tales-sign-in-page.webp)

- This will take the user to the sign-in page where a username and password are requested. You can select a small tick box to remember login credentials to make it easier for future sign-ins.

*[As a User, I can safely log out of my account so that I can disconnect from the site](https://github.com/chris-townsend/PP4-Kitchen_Tales/issues/25)*

![Kichen Tales sign out tab](docs/testing/user-testing/kitchen-tales-sign-out-tab.webp)

- Users can safely sign out of their account by clicking on their drop-down menu and after selecting Logout from the bottom of the list.

![Kichen Tales sign out page](docs/testing/user-testing/kitchen-tales-sign-out-page.webp)

- Clicking on Logout will take the user to a confirmation page to confirm signing out. 

*[As a logged-in User, I can see my login status so that I know if I am logged in or out of my account](https://github.com/chris-townsend/PP4-Kitchen_Tales/issues/26)*

![Kichen Tales login status](docs/testing/user-testing/kitchen-tales-login-status.webp)

- At first, I left the MyAccount tab as it was for signed-in users but soon realised this was not as intuitive for the user to realize their login status unless they clicked on their MyAccount menu. I have now changed this heading to the user's name and a profile icon so that a user will instantly know when there logged-in as they will be able to see their profile name in the nav section.

![Kichen Tales navbar status for logged in user](docs/testing/user-testing/kitchen-tales-logged-in-navbar.webp)

- I have organized the items within the drop-down menu of importance, with Logout being the least likely page a user will want to navigate to when signed in.

#

### EPIC | *Admin Features & Owner Objectives*
<br>

*[As a Site admin, I can create, edit and delete recipes and comments so that I can control the site content](https://github.com/chris-townsend/PP4-Kitchen_Tales/issues/28)*

![Kichen Tales admin panel](docs/testing/user-testing/django-admin-panel.webp)

- Admins have full access to CRUD functionality for all recipes and comments within the Django admin panel.

![Kichen Tales admin recipe panel](docs/testing/user-testing/django-recipe-panel.webp)

- The *'Recipes'* admin panel has been created within `admin.py`. Recipes are sorted by status and created date for organization.

![Kichen Tales admin comment panel](docs/testing/user-testing/django-comment-panel.webp)

- The *Comment* admin panel has been set up in a similar way to *Recipes* and displays comments by created date with the newest comments to be approved at the top.

*[As a Site admin, I can authorize comments so that I can review the content before it's made public](https://github.com/chris-townsend/PP4-Kitchen_Tales/issues/29)*

![Kichen Tales admin panel approve comments](docs/testing/user-testing/django-admin-approve-comment.webp)

- Comments need to be approved by a site admin before they are published publically. The user should receive an alert when a comment has been posted stating that the comment is under review. 

*[As a Site owner, I would like to display my social icons so that I can promote my other channels](https://github.com/chris-townsend/PP4-Kitchen_Tales/issues/31)*

![Kichen Tales social icons](docs/testing/user-testing/kitchen-tales-social-icons.webp)

- Social Icons are displayed at the bottom of every page, this includes links to Facebook, Instagram, Youtube, and Twitter. All links open in a new tab for user convenience.

<br>

[Back to top ⇧](#contents)

***

## Validator Testing

![HTML w3c validator](docs/testing/html/html-w3c-validation.webp)

The *[W3C HTML validator](https://validator.w3.org/)* was used to test all HTML pages, and **no errors** were reported in the final deployment.

### HTML

| Page                   | Status      |              | URL         |
| ---                    |   :---:     |    :---:     |    :---:    |
|                        | *logged-in* | *logged-out* |             |
|`403.html`                |   *pass*    |   *pass*     |      -      |  
|`404.html`                |   *pass*    |   *pass*     |      -      |
|`500.html`                |   *pass*    |   *pass*     |      -      |
|`add_recipe.html`         |   *pass*    |   *n/a*      |  *[result](https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fkitchen-tales.herokuapp.com%2Fadd_recipe%2F#l189c24)*           |
|`all_recipes.html`        |   *pass*    |   *pass*     |  *[result](https://validator.w3.org/nu/?doc=https%3A%2F%2Fkitchen-tales.herokuapp.com%2Fall_recipes%2F)*    |
|`base.html`               |   *pass*    |   *pass*     |  *[result](https://validator.w3.org/nu/?doc=https%3A%2F%2Fkitchen-tales.herokuapp.com%2F)*    |
|`delete_comment.html`     |   *pass*    |   *n/a*      |  *[result](https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fkitchen-tales.herokuapp.com%2Fdelete_comment%2F62%2F#l189c24)*           |
|`delete_recipe.html`      |   *pass*    |   *n/a*      | *[result](https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fkitchen-tales.herokuapp.com%2Fdelete_recipe%2F62%2F#l189c24)*   |
|`footer.html`             |   *pass*    |   *pass*     | *[result](https://validator.w3.org/nu/?doc=https%3A%2F%2Fkitchen-tales.herokuapp.com%2F)*    |
|`index.html`            |   *pass*    |   *pass*     | *[result](https://validator.w3.org/nu/?doc=https%3A%2F%2Fkitchen-tales.herokuapp.com%2F)*    | 
|`my_recipes.html`         |   *pass*    |   *n/a*      | *[result](https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fkitchen-tales.herokuapp.com%2Fmy_recipes%2F#l189c24)* |
|`my_starred_recipes.html` |   *pass*    |   *n/a*      |  *[result](https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fkitchen-tales.herokuapp.com%2Fmy_starred_recipes%2F#l189c24)*|
|`newsletter.html`         |   *pass*    |   *pass*     |  *[result](https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fkitchen-tales.herokuapp.com%2Fnewsletter#l189c24)*    |
|`recipe_detail.html`      |   *pass*    |   *pass*     |  *[result](https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fkitchen-tales.herokuapp.com%2Frecipe_detail%2Fbutternut-squash-sage-risotto%2F#l189c24)*    |
|`recipe_paginator.html`   |   *pass*    |    *pass*    |      -      |
|`search_results.html`     |   *pass*    |    *pass*    | *[result](https://validator.w3.org/nu/?doc=https%3A%2F%2Fkitchen-tales.herokuapp.com%2Fsearch_results%2F)* |
|`update_comment.html`     |   *pass*    |    *n/a*     | *[result](https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fkitchen-tales.herokuapp.com%2Fupdate_comment%2F62%2F#l189c24)*            |
|`update_recipe.html`      |   *pass*    |    *n/a*     | *[result](https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fkitchen-tales.herokuapp.com%2Fupdate_recipe%2F62%2F#l189c24)* |
|`login.html`              |   *pass*    |    *pass*    | *[result](https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fkitchen-tales.herokuapp.com%2Faccounts%2Flogin%2F#l189c24)*           |
|`logout.html`             |   *pass*    |    *n/a*     | *[result](https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fkitchen-tales.herokuapp.com%2Faccounts%2Flogout%2F#l189c24)*            |
|`signup.html`             |   *n/a*     |    *pass*    | *[result](https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fkitchen-tales.herokuapp.com%2Faccounts%2Fsignup#l189c24)*           |

***

### CSS 

The *[W3C CSS Validator](https://jigsaw.w3.org/css-validator/)* was used to validate the project, the results are shown below with **no errors reported.**

![CSS w3c validator](docs/testing/css/css-w3c-validation.webp)
![CSS Result](docs/testing/css/css-validation-pass.webp)

- *[ CSS results](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fkitchen-tales.herokuapp.com%2F&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en)*

***

### JavaScript

*[JSHint](https://jshint.com/)* was used to check the JavaScript within the base template. The JavaScript code has been placed in `<script>` tags at the bottom of the `base.html` template and as there is very little JavaScript code, I felt it was not worth placing in its own file. The results came back with no errors but a few undefined variables. I have left this as it is with a detailed comment above the variables to explain their function.

![JSHint Logo](docs/testing/javascript/testing-jshint.webp)
![JavaScript Code to test](docs/testing/javascript/testing-jshint-code.webp)
![JShint test result](docs/testing/javascript/testing-jshint-result.webp)

***

### Python

Code Institutes *[PEP8](https://pep8ci.herokuapp.com/)* linter was used to test the Python files. The table below shows the pages tested and their result, all pages are **error-free** in the final deployment.

![Code Institute's Python linter](docs/testing/python/ci-python-linter.webp)


| Page                   | `kitchentales` |  `recipes`   | 
| ---                    |      :---:     |    :---:     |    
| `admin.py`             |     *n/a*      |    *pass*    |
| `apps.py`              |     *n/a*      |    *pass*    | 
| `forms.py`             |     *n/a*      |    *pass*    |
| `models.py`            |     *n/a*      |    *pass*    | 
| `urls.py`              |     *pass*     |    *pass*    |
| `views.py`             |     *n/a*      |    *pass*    |  
| `test_forms.py`        |     *n/a*      |    *pass*    |
| `test_models.py`       |     *n/a*      |    *pass*    |
| `test_views.py`        |     *n/a*      |    *pass*    |

***

### Lighthouse 

I have run the website through Google Chrome's Lighthouse audit application and the results are shown below:
 
| Page                     |    Desktop     |    Mobile    | 
| ---                      |      :---:     |    :---:     | 
| `403.html`               |![lighthouse result desktop 403](docs/testing/lighthouse/lighthouse-desktop-403.webp)                      |![lighthouse result mobile 403](docs/testing/lighthouse/lighthouse-mobile-403.webp)                      |   
| `404.html`               |![lighthouse result desktop 404](docs/testing/lighthouse/lighthouse-desktop-404.webp)                      |![lighthouse result mobile 404](docs/testing/lighthouse/lighthouse-mobile-404.webp)                      |
| `500.html`               |![lighthouse result desktop 500](docs/testing/lighthouse/lighthouse-desktop-500.webp)                      |![lighthouse result mobile 500](docs/testing/lighthouse/lighthouse-mobile-500.webp)              | 
| `add_recipe.html`        |![lighthouse result desktop add recipe](docs/testing/lighthouse/lighthouse-desktop-add-recipe.webp)         |![lighthouse result mobile add recipe](docs/testing/lighthouse/lighthouse-mobile-add-recipe.webp)          |
| `all_recipes.html`       |![lighthouse result desktop all recipes](docs/testing/lighthouse/lighthouse-desktop-all-recipes.webp)        |![lighthouse result mobile all recipes](docs/testing/lighthouse/lighthouse-mobile-all-recipes.webp)  |
| `index.html`             |![lighthouse result desktop index](docs/testing/lighthouse/lighthouse-desktop-index.webp)              |![lighthouse result mobile index](docs/testing/lighthouse/lighthouse-mobile-index.webp)               | 
| `delete_comment.html`    |![lighthouse result desktop delete comment](docs/testing/lighthouse/lighthouse-desktop-delete-comment.webp)     |![lighthouse result mobile delete comment](docs/testing/lighthouse/lighthouse-mobile-delete-comment.webp)              |
| `my-recipes.html`        |![lighthouse result desktop my recipes](docs/testing/lighthouse/lighthouse-desktop-my-recipes.webp)         |![lighthouse result mobile my recipes](docs/testing/lighthouse/lighthouse-mobile-my-recipes.webp)          |  
| `my_starred_recipes.html`|![lighthouse result desktop my starred recipes](docs/testing/lighthouse/lighthouse-desktop-my-liked-recipes.webp)   |![lighthouse result mobile my starred recipes](docs/testing/lighthouse/lighthouse-mobile-my-liked-recipes.webp)              |
| `newsletter.html`        |![lighthouse result desktop newsletter](docs/testing/lighthouse/lighthouse-desktop-newsletter.webp)         |![lighthouse result mobile newsletter](docs/testing/lighthouse/lighthouse-mobile-newsletter.webp)              |
| `recipe_detail.html`     |![lighthouse result desktop recipe detail](docs/testing/lighthouse/lighthouse-desktop-recipe-detail.webp)      |![lighthouse result mobile recipe detail](docs/testing/lighthouse/lighthouse-mobile-recipe-detail.webp)              |
| `search_results.html`    |![lighthouse result desktop search results](docs/testing/lighthouse/lighthouse-desktop-search-results.webp)    |![lighthouse result mobile search results](docs/testing/lighthouse/lighthouse-mobile-search-results.webp)              |
| `update_comment.html`    |![lighthouse result desktop update comment](docs/testing/lighthouse/lighthouse-desktop-update-comment.webp)    |![lighthouse result mobile update comment](docs/testing/lighthouse/lighthouse-mobile-update-comment.webp)              |
| `update_recipe.html`     |![lighthouse result desktop update recipe](docs/testing/lighthouse/lighthouse-desktop-update-recipe.webp)     |![lighthouse result mobile update recipe](docs/testing/lighthouse/lighthouse-mobile-update-recipe.webp)              |
| `login.html`             |![lighthouse result desktop login](docs/testing/lighthouse/lighthouse-desktop-login.webp)  |![lighthouse result mobile login](docs/testing/lighthouse/lighthouse-mobile-login.webp)              |
| `logout.html`            |![lighthouse result desktop logout](docs/testing/lighthouse/lighthouse-desktop-signout.webp)|![lighthouse result mobile logout](docs/testing/lighthouse/lighthouse-mobile-signout.webp)              | 
| `signup.html`            |![lighthouse result desktop signup](docs/testing/lighthouse/lighthouse-desktop-signup.webp) |![lighthouse result mobile signup](docs/testing/lighthouse/lighthouse-mobile-signup.webp)              |

<br>

The results are satisfactory and the suggested modification with regards to the issue within the console appears to give a lower score for *Best Practices* throughout mobile and desktop tests. Please see *[issue #64](https://github.com/chris-townsend/PP4-Kitchen_Tales/issues/64)* for further information regarding the Audit usage of navigator.userAgent, navigator.appVersion & navigator.platform and a potential future issue to fix the current warning. The other suggestion is relating to the sizing of the site logo. This is a design choice, the image looks much better when it hasn't been cropped. If more time were available, image editing software could be utilised to edit the image but the effect is negligible. Overall the site runs better on desktop, but the performance could be improved for mobile when adding and updating a recipe, this is mostly due to using *Summernote* widgets for certain fields. This has been left as it is for now as the overall performance of the site is good. 

![lighthouse low score](docs/testing/lighthouse/lighthouse-enable-text-compression.webp)

<br>

***

### WAVE accessibility evaluation tool

Most pages of the site were tested through the [WAVE evaluation tool](https://wave.webaim.org/), The results are documented as images in the [`docs/testing/accessibility/`](https://github.com/chris-townsend/PP4-Kitchen_Tales/tree/main/docs/testing/accessibility) directory.

The overall result is good and the two alerts are for Adjacent links which go to the same URL. One of these is for the *'Home'* tab in the nav section and the second one is the sign-up button on the homepage in the welcome section, the signup button allows the user to intuitively sign-up without having to open the *MyAccount* tab in the nav section.      

 <br>

[Back to top ⇧](#contents)

***

## Browser Testing

The Website was tested on Google Chrome, Internet Explorer and Microsoft Edge with no issues reported. Family members and friends were asked to review the site and point out any bugs or problems if encountered.

***

## Device Testing

The website has been viewed on a variety of devices such as Desktop, Laptop, Oneplus 5t, iPhone SE, iPhone 8, iPad & Samsung Galaxy S21 to ensure that the responsive design worked as intended. [Chrome DevTools](https://developer.chrome.com/docs/devtools/) was used to test the responsiveness on different devices.

### Mobile 

All pages have been tested through Google's [Mobile friendly test](https://search.google.com/test/mobile-friendly), the results are displayed below:



| Page                     |    Result      |  URL    |
| ---                      |      :---:     |   :---: |
| `403.html`               |    *pass*      |    -    |
| `404.html`               |    *pass*      |    -    |
| `500.html`               |    *pass*      |    -    |
| `add_recipe.html`        |   *pass*       | *[result](https://search.google.com/test/mobile-friendly/result?id=aOHBnnl3q2jqRJLkO4_a1Q)*    |
| `all_recipes.html`       |   *pass*       | *[result](https://search.google.com/test/mobile-friendly/result?id=SQ3Ve7ab9qAzr8q4B1AP7g)*    |
| `index.html`             |   *pass*       | *[result](https://search.google.com/test/mobile-friendly/result?id=ZQ5JeN0J8_jCrs9AL-XSJA)*    |
| `delete_comment.html`    |   *pass*       |  *[result](https://search.google.com/test/mobile-friendly/result?id=5DLzP6zScRzRy2gBUH89DQ)*    |
| `delete_recipe.html`     |   *pass*       | *[result](https://search.google.com/test/mobile-friendly/result?id=Sm8GiQESmvpbkrqUSqSJjA)*    |
| `my-recipes.html`        |   *pass*       | *[result](https://search.google.com/test/mobile-friendly/result?id=5u4qBbuuRxDLr8LM_QYGjQ)*    |
| `my_starred_recipes.html`|   *pass*       | *[result](https://search.google.com/test/mobile-friendly/result?id=S1NwkY_ro0IdeyDjlhdIdA)*    |
| `newsletter.html`        |   *pass*       | *[result](https://search.google.com/test/mobile-friendly/result?id=DrcZuU6x3WnlnhslIWkenw)*    |
| `recipe_detail.html`     |   *pass*       | *[result](https://search.google.com/test/mobile-friendly/result?id=Fph8ccy1CKWQy9xQmGfuHA)*    |
| `search_results.html`    |   *pass*       |  *[result](https://search.google.com/test/mobile-friendly/result?id=fByRDAqrCjNM8N1eJ4DPhw)*    |
| `update_comment.html`    |    *pass*      |  *[result](https://search.google.com/test/mobile-friendly/result?id=dfQ-514X3tHc3ZdwCPmfcQ)*      |
| `update_recipe.html`     |   *pass*       |  *[result](https://search.google.com/test/mobile-friendly/result?id=aA7MKDRWPfvomdeN44znqA)*    |
| `login.html`             |   *pass*       | *[result](https://search.google.com/test/mobile-friendly/result?id=xmBoy-5AJASdU-s9G3uXzg)*    |
| `logout.html`            |   *pass*       | *[result](https://search.google.com/test/mobile-friendly/result?id=fnUDeMALErhOhEv-SZHeHA)*    |
| `signup.html`            |   *pass*       | *[result](https://search.google.com/test/mobile-friendly/result?id=3WljjfpwBdCXQ1KCJv-ieg)*    |


***

## Manual Testing

The process and outcomes of manual testing are described in depth in the following section:

### *Navigation*
<br>

| Page/Status     | Element             |   Action    | Expected Result           | Pass/Fail   |
| ---             | ---                 |   :---:     |    :---:                  |    :---:    |
|**Homepage**     |**Navbar**           |             |                           |             |
|                 |*Home link*          |   *click*   | *Redirect to homepage*    |  **pass**   |
|                 |*Recipes link*       |   *click*   | *Open `all_recipes` page* |  **pass**   |
|                 |*Kitchen Tales logo* |   *click*   | *Redirect to homepage*    |  **pass**   |
|                 |*Search Recipes button*|   *click* | *Open `search_results` page*| **pass**  |
|                 |                     |   *hover*   | *Display lighter colour* |**pass**|
| **logged out**  |*MyAccount drop-down*|   *click*   | *Open drop-down menu*     |  **pass**   |  
|                 |*Sign-in link*       |   *click*   | *Open `login` page*       |  **pass**   |
|                 |*Register link*      |   *click*   | *Open `signup` page*      |  **pass**   |
| **logged in**   |*MyAccount drop-down*|  *display*  | *Change to username & user icon*|**pass**|
|                 |*Add-Recipe link*    |   *click*   | *Open `add_recipe` page*  |  **pass**   |
|                 |*My-Recipes link*    |   *click*   | *Open `my_recipes` page*  |  **pass**   |
|                 |*Saved-Recipes link* |   *click*   | *Open `my_starred_recipes` page*|**pass**|
|                 |*Logout link*        |   *click*   | *Open `logout` page*      |  **pass**   |
|                 |*All nav headings*   |   *hover*  |*Display darker text & underlined*| **pass** |
|                 |                     |             |                                 |            |
|**Mobile view**  |                     |             |                                 |           |
|                 |**Navbar**           |  *display*   |*Hamburger menu when the screen size is less than 900px*  | **pass**            |
|                 |*Home link*          |   *click*   | *Redirect to homepage*    |  **pass**   |
|                 |*Recipes link*       |   *click*   | *Open `all_recipes` page* |  **pass**   |
|                 |*Kitchen Tales logo* |   *click*   | *Redirect to homepage*    |  **pass**   |
|                 |*Search Recipes button*|   *click* | *Open `search_results` page*| **pass**  |
|                 |*MyAccount drop-down*| *display*   | *Display in hamburger menu* | **pass**  |
| **logged out**  |                     |   *click*   | *Open drop-down menu*     |  **pass**   |  
|                 |*Sign-in link*       |   *click*   | *Open `login` page*       |  **pass**   |
|                 |*Register link*      |   *click*   | *Open `signup` page*      |  **pass**   |
| **logged in**   |*MyAccount drop-down*|  *display*  | *Change to username & user icon*|**pass**|
|                 |*Add-Recipe link*    |   *click*   | *Open `add_recipe` page*  |  **pass**   |
|                 |*My-Recipes link*    |   *click*   | *Open `my_recipes` page*  |  **pass**   |
|                 |*Saved-Recipes link* |   *click*   | *Open `my_starred_recipes` page*|**pass**|
|                 |*Logout link*        |   *click*   | *Open `logout` page*      |  **pass**   |


### Homepage - *Content*
<br>

| Page/Status     | Element             |   Action    | Expected Result     |   Pass/Fail     |
| ---             | ---                 |   :---:     |    :---:            |    :---:        |
|**Homepage**     |**Welcome to Kitchen Tales section**|         |                     |                 |
|                 | *Image*             | *display*   |*Image displayed*    | **pass**        |
|**logged-out**   |*Sign up today link* | *click*     |*Open `signup` page* | **pass**        |
|                 |                     | *hover*     |*Dark background/light text*| **pass** |
|**logged-in**    |*Welcome text*       | *display*   |*Welcome text with username*| **pass** |
|                 |*Add recipe link*    | *click*     |*Open `add_recipe` page* | **pass**    |
|                 |                     | *hover*     |*Dark background/light text*| **pass** | 
| **All user's**   |**Image carousel section**|        |                     |                 |
|                 | *Images*            | *display*   |*Image displayed*    | **pass**        |
|                 |                     |*aria-label check*|*Display aria-labels* |**pass**   |
|                 | *Carousel-control button*| *click*|*Go to next image*   | **pass**        |
| **All user's**   |**Card section**     |             |                     |                 |
|                 | *Images*            | *display*   |*Image displayed*    | **pass**        |
|                 |                     | *aria-label check*|*Display aria-labels*|           |
|                 |*Recipe App/Cheese Club images*|*hover*|*Rotate image 180°*| **pass**      |
| **All user's**   |**Newsletter section**|            |                     |                 |
|                 | *Subscribe button*  | *click*     |*Open `newsletter` page* | **pass**    |
|                 |                     | *hover*     |*Dark background/light text*| **pass** |
|**Mobile view**  |                     |             |                       |               |
|                 |**Welcome to Kitchen Tales section**|         |                     |                 |
|                 | *Image*             | *display*   |*Image not displayed*    | **pass**    |
|**logged-out**   |*Sign up today link* | *click*     |*Open `signup` page* | **pass**        |
|**logged-in**    |*Welcome text*       | *display*   |*Welcome text with username*| **pass** |
|                 |*Add recipe link*    | *click*     |*Open `add_recipe` page* | **pass**    |
| **All user's**   |**Image carousel section**|        |                     |                 |
|                 | *Images*            | *display*   |*Image displayed*    | **pass**        |
|                 | *Carousel-control button*| *click*|*Go to next image*   | **pass**        |
| **All user's**   |                     |             |                     |                 |
|                 | **Card section**    | *display*   |*Responsive*| **pass**   |
| **All user's**   |**Newsletter section**|            |                     |                 |
|                 | *Subscribe button*  | *click*     |*Open `newsletter` page* | **pass**    |
|                 |                     | *hover*     | *Dark background/light text* | **pass** |


### Homepage - *Footer*
<br>

| Page/Status     | Element             |   Action    | Expected Result     |   Pass/Fail     |
| ---             | ---                 |   :---:     |    :---:            |    :---:        |
|**Homepage**     |**Social Icons**     | *click*     | *Open in a new tab* |  **pass**       |
|                 |                     | *hover*     | *Change scale **1.2***  |  **pass**   |
|                 |                     | *aria-label check*| *Display aria-labels*| **pass** |
|**Mobile view**  |                     |             |                      |                |
|                 |                     | *display*   | *Responsive layout*   | **pass**      |
|                 |                     | *click*     | *Open in a new tab* |  **pass**       |


### *Recipes*
<br>

| Page/Status     | Element           |   Action      | Expected Result            | Pass/Fail   |
| ---             | ---               |   :---:       |    :---:                   |    :---:    |
|`all_recipes`    |**Navbar**         | *display*     | *Display navbar*           |   **pass**  |
|                 |**Recipe card**    |*display image*| *Correct recipe image clipped*|**pass**  |
|                 |  *Image*          |*hover*        | *Rotate image 180°*        | **pass**    |
|                 |  *Content*     |*display*|*Title, Cook & Prep time, Like counter*| **pass**  |
|                 |                   | *order display*|*Order from newest to oldest*| **pass**  |
|                 |                   | *click*       | *Open recipe detail page*    | **pass**  |
|                 |**Paginator buttons**  | *display*     |*Display pagination buttons if more than 8 recipes* | **pass**         |
|                 | ***Next** button* | *click*       |*Display the next page of recipes*| **pass**   |
|                 |                   | *if clicked display*|*First/Previous buttons*| **pass**   |
|                 |                   | *hover*       | *Lighter background colour*  | **pass**   |
|                 | ***Last** button* | *click*       |*Display the last page of recipes*| **pass**   |
|                 |                   | *hover*       | *Lighter background colour*  | **pass**   |
|                 | ***First** button*| *click*       |*Display the first page of recipes*| **pass**  |
|                 |                   | *hover*       | *Lighter background colour*  | **pass**   |
|                 |***Previous** button*| *click*     |*Display the previous page of recipes*| **pass**|
|                 |                   | *hover*       | *Lighter background colour*  | **pass**   |
| **Mobile view** |                   |               |                              |            |
|                 |**Navbar**         | *display*     | *Hamburger menu*             | **pass**   |
|                 |**Recipe card**    |*display*      |        *Responsive layout*|**pass**     |
|                 |                   | *click*       | *Open recipe detail page*    | **pass**  |
|                 |**Paginator buttons**  | *display*     |*Display pagination buttons if more than 8 recipes* | **pass**         |
|                 | ***Next** button* | *click*       |*Display the next page of recipes*| **pass**   |
|                 |                   | *if clicked display*|*First/Previous buttons*| **pass**   |
|                 | ***Last** button* | *click*       |*Display the last page of recipes*| **pass**   |
|                 | ***First** button*| *click*       |*Display the first page of recipes*| **pass**  |
|                 |***Previous** button*| *click*     |*Display the previous page of recipes*| **pass**|
|                 |**Footer**           | *display*   | *Responsive layout*              | **pass**|


### *Recipe Detail*
<br>

| Page/Status     | Element           |   Action      | Expected Result            | Pass/Fail   |
| ---             | ---               |   :---:       |    :---:                   |    :---:    |
|`recipe_detail`  |**Navbar**         | *display*     | *Display navbar*           |   **pass**  |
|                 |**Recipe Content** | *display*     | *Display image, title, author, prep & cook time, last updated date, and like status*| **pass**    |
|                 |                    | *display*    |*Ingredients & method side by side*| **pass**          |
|                 |**Comments**        | *display*    | *Comments from other users including date & comment author*| **pass**    |
|                 |                  | *display*     | *Comments are ordered from oldest to newest*|
|                 |**Social icons**    | *display*    | *Display social icons*     | **pass**    |
|                 |                    | *hover*      | *Change scale **1.2***     | **pass**    |
|**logged-out**   |*Star button & sign up link* |*click*| *Open `signup` page*     | **pass**    |
|                 |                           |*hover*| <u>*Underline text*</u>           | **pass**    |
|**logged-in**    |*Star button outline & text*| *click*| *Clicking the outlined star changes it to a solid star and displays the number of likes*     | **pass** |
|                 |                    | *click*       | *Recipe saved to a logged-in user `my_starred_recipes`* | **pass**   | 
|                 |          | *click*| *Success message to alert the user that the recipe has been saved* | **pass**     |
|                 |*Star button solid state* | *click* | *Clicking the solid star changes it to an outline star*     | **pass** | 
|                 |                    |*click*        | *Remove saved recipe from a logged-in user `my_starred_recipes`* | **pass**   | 
|                 |                    |*click* | *Success message to alert the user that the recipe has been removed from their `my_starred_recipes`* | **pass**     |
|                 | **Comments**    | *display*    | *Text input box with submit button*| **pass**|
|                 | *Submit button* | *hover*    | *Lighter background colour* | **pass**     |
|                 |                 | *click*    |  *Form submits and the page updates* | **pass**  |
|                 |                 | *click*    | *Success message to alert the user that their comment is under review* | **pass**     |
|                 | No data         | *click*   | *Error message displayed and form won't submit* | **pass** | 
|**logged-in *author***|               | *display*       | **Edit** *&* **Delete** *buttons* | **pass**   |
|                      |*Edit & Delete buttons* | *hover*| *<u>Underline</u> & make text darker*| **pass**|
|                      | *Edit button*       |  *click*  | *Open `update_recipe` page* | **pass**|
|                      | *Delete button*     |  *click*  | *Open `delete_recipe` page* | **pass**|
|**logged-in *comment author*** |      | *display*       | **Edit** *&* **Delete** *buttons* | **pass**    |
|                      |*Edit & Delete Icons* | *hover*| *Display lighter colour*| **pass**   | 
|                      | *Edit comment button*       |  *click*  | *Open `update_comment` page* | **pass**|
|    | *Delete comment button*     |  *click*  | *Open `delete_comment` page*|**pass**|     
| **Mobile view**      |             |         |                             |                      |   
|                      |**Navbar**         | *display*     | *Hamburger menu*           |   **pass**  |
|                      |**Recipe Content** | *display*     | *Display responsive layout*| **pass**    |
|                 |                    | *display*    |*Display ingredients & method separately*| **pass**          |
|                 |  **Comments**      | *display*     | *Comments are ordered from oldest to newest*| **pass**           |
|                 |**Social icons**    | *display*    | *Responsive design*     | **pass**    |  


### *My Recipes*
<br>

| Page/Status     | Element           |   Action      | Expected Result            | Pass/Fail   |
| ---             | ---               |   :---:       |    :---:                   |    :---:    |
|`my_recipes`     |**Navbar**         | *display*     | *Display navbar*           |   **pass**  |
| **logged-in**   |`my_recipes` page  | *display*     | *Only display the logged-in users created recipes*| **pass**|
|                 |                   | *access*      | *If an unauthorized user tries to access this page by changing the URL, redirect to the sign-in page*| **pass** |
|                 |**Recipe card**    |*display image*| *Correct recipe image clipped*|**pass**  |
|                 |  *Image*          |*hover*        | *Rotate image 180°*        | **pass**    |
|                 |  *Content*     |*display*|*Title, Cook & Prep time, Like counter*| **pass**  |
|                 |                   | *order display*|*Order from newest to oldest*| **pass**  |
|                 |                   | *click*        | *Open recipe detail page*   | **pass**  |
|                 |**Paginator buttons**  | *display*     |*Display pagination buttons if more than 8 recipes* | **pass**         |
|                 | ***Next** button* | *click*       |*Display the next page of recipes*| **pass**   |
|                 |                   | *if clicked display*|*First/Previous buttons*| **pass**   |
|                 |                   | *hover*       | *Lighter background colour*  | **pass**   |
|                 | ***Last** button* | *click*       |*Display the last page of recipes*| **pass**   |
|                 |                   | *hover*       | *Lighter background colour*  | **pass**   |
|                 | ***First** button*| *click*       |*Display the first page of recipes*| **pass**  |
|                 |                   | *hover*       | *Lighter background colour*  | **pass**   |
|                 |***Previous** button*| *click*     |*Display the previous page of recipes*| **pass**|
|                 |                   | *hover*       | *Lighter background colour*  | **pass**   |
|                 |**Footer**         | *display*     | *Social icons are displayed at the bottom of the page* | **pass**|
|                 |                   | *hover*      | *Change scale **1.2***     | **pass**    |  
| **Mobile view**  |             |         |                             |                      |   
|                      |**Navbar**         | *display*     | *Hamburger menu*             |   **pass**  |
| **logged-in**   |`my_recipes` page  | *display*     |      *Responsive layout*              | **pass**|
|                 |                   | *order display*|*Order from newest to oldest*| **pass**  |
|                 | **Recipe Card**   | *click*        | *Open recipe detail page*   | **pass**  |
|                 |**Paginator buttons**  | *display*     |*Display pagination buttons if more than 8 recipes* | **pass**         |
|                 | ***Next** button* | *click*       |*Display the next page of recipes*| **pass**   |
|                 | ***Last** button* | *click*       |*Display the last page of recipes*| **pass**   |
|                 | ***First** button*| *click*       |*Display the first page of recipes*| **pass**  |
|                 |***Previous** button*| *click*     |*Display the previous page of recipes*| **pass**|
|                 |**Footer**         | *display*     | *Social icons responsive* | **pass**|


### *My Starred Recipes*
<br>

| Page/Status     | Element           |   Action      | Expected Result            | Pass/Fail   |
| ---             | ---               |   :---:       |    :---:                   |    :---:    |
|`my_starred_recipes`|**Navbar**         | *display*     | *Display navbar*        |   **pass**  |
| **logged-in**   |`my_starred_recipes` | *display*     | *Only display the logged-in users starred recipes*| **pass**|
|                 |                   | *access*      | *If an unauthorized user tries to access this page by changing the URL, redirect to the sign-in page*| **pass** |
|                 |**Recipe card**    |*display image*| *Correct recipe image clipped*|**pass**  |
|                 |  *Image*          |*hover*        | *Rotate image 180°*        | **pass**    |
|                 |  *Content*     |*display*|*Title, Cook & Prep time, Like counter*| **pass**  |
|                 |                   | *order display*|*Order from newest to oldest*| **pass**  |
|                 |                   | *click*        | *Open recipe detail page*   | **pass**  |
|                 |**Paginator buttons**  | *display*     |*Display pagination buttons if more than 8 recipes* | **pass**         |
|                 | ***Next** button* | *click*       |*Display the next page of recipes*| **pass**   |
|                 |                   | ***if** clicked display*|*First/Previous buttons*| **pass**   |
|                 |                   | *hover*       | *Lighter background colour*  | **pass**   |
|                 | ***Last** button* | *click*       |*Display the last page of recipes*| **pass**   |
|                 |                   | *hover*       | *Lighter background colour*  | **pass**   |
|                 | ***First** button*| *click*       |*Display the first page of recipes*| **pass**  |
|                 |                   | *hover*       | *Lighter background colour*  | **pass**   |
|                 |***Previous** button*| *click*     |*Display the previous page of recipes*| **pass**|
|                 |                   | *hover*       | *Lighter background colour*  | **pass**   |
|                 |**Footer**         | *display*     | *Social icons are displayed at the bottom of the page* | **pass**|
|                 |                   | *hover*      | *Change scale **1.2***     | **pass**    |
| **Mobile view**  |             |         |                             |                      |   
|                      |**Navbar**         | *display*     | *Hamburger menu*             |   **pass**  |
| **logged-in**   |`my_starred_recipes` page  | *display*     |      *Responsive layout*              | **pass**|
|                 |                   | *order display*|*Order from newest to oldest*| **pass**  |
|                 | **Recipe Card**   | *click*        | *Open recipe detail page*   | **pass**  |
|                 |**Paginator buttons**  | *display*     |*Display pagination buttons if more than 8 recipes* | **pass**         |
|                 | ***Next** button* | *click*       |*Display next page of recipes*| **pass**   |
|                 | ***Last** button* | *click*       |*Display last page of recipes*| **pass**   |
|                 | ***First** button*| *click*       |*Display first page of recipes*| **pass**  |
|                 |***Previous** button*| *click*     |*Display previous page of recipes*| **pass**|
|                 |**Footer**         | *display*     | *Social icons responsive* | **pass**|


### *Django All Auth Pages*
<br>

| Page/Status     | Element           |   Action          | Expected Result            | Pass/Fail   |
| ---             | ---               |   :---:           |    :---:                   |    :---:    |
|`signup`         |**Navbar**         | *display*         | *Display navbar*           |   **pass**  |
|                 | *Login link*      | *click*           | *Redirect to `login` page*  |   **pass**  |
|                 | ***Username field***  | *leave empty*     |  *Error message*           | **pass**    |
|                 |                   | *enter valid data*| *Form submits*             |  **pass**   |
|                 |                   | *enter invalid format* | *Form won't submit*   | **pass**    | 
|                 |                   | *enter invalid format* | *Error message*       | **pass**    |
|                 | ***Email field***     | *leave empty*       | *Form submits*           | **pass**    | 
|                 |                   | *enter invalid format*|  *Error message*       | **pass**    |
|                 |                   | *enter invalid format*| *Form won't submit*    | **pass**    |
|                 |                   | *enter valid data*| *Form submits*             | **pass**    |
|                 | ***Password field***  | *leave empty*       | *Error message*          | **pass**    |
|                 |                   | *enter valid data*| *Form submits*             |  **pass**   |
|                 |                   | *password does not match* | *Error message*         | **pass**    |
|                 |                   | *password does not match* | *Form won't submit*     | **pass**    |
|                 | ***Signup button*** | *hover*            |*Lighter background colour*|**pass**   |
|                 |                   | *click*         | *Form submits*          | **pass**    |
|                 |                   | *click*         | *Return to homepage*    | **pass**    |
|                 |                   | *click*         | *Success message to alert the user of a successful login* | **pass** |
|                 |                   |                     | *Automatically close alert after 2.8sec*| **pass**  |
|**Mobile view**  |                   |                    |                            |            |    
|                 | `signup` page     | *display*        | *Responsive*               |**pass**     |
|                 | **Navbar**        | *display*        | *Hamburger menu*           | **pass**    |
|                 | *Login link*      | *click*           | *Redirect to `login` page*  |   **pass**  |
|                 | ***Username field***  | *leave empty*     |  *Error message*           | **pass**    |
|                 |                   | *enter valid data*| *Form submits*             |  **pass**   |
|                 |                   | *enter invalid format* | *Form won't submit*   | **pass**    | 
|                 |                   | *enter invalid format* | *Error message*       | **pass**    |
|                 | ***Email field***     | *leave empty*       | *Form submits*           | **pass**    | 
|                 |                   | *enter invalid format*|  *Error message*       | **pass**    |
|                 |                   | *enter invalid format*| *Form won't submit*    | **pass**    |
|                 |                   | *enter valid data*| *Form submits*             | **pass**    |
|                 | ***Password field***  | *leave empty*       | *Error message*          | **pass**    |
|                 |                   | *enter valid data*| *Form submits*             |  **pass**   |
|                 |                   | *password does not match* | *Error message*         | **pass**    |
|                 |                   | *password does not match* | *Form won't submit*     | **pass**    |
|`login`         |**Navbar**         | *display*         | *Display navbar*           |   **pass**  |
|                 | *Sign up link*      | *click*           | *Redirect to `signup` page*  |   **pass**  |
|                 | ***Username field***  | *leave empty*     |  *Error message*           | **pass**    |
|                 |                   | *enter valid data*| *Form submits*             |  **pass**   |
|                 |                   | *enter invalid format* | *Form won't submit*   | **pass**    | 
|                 |                   | *enter invalid format* | *Error message*       | **pass**    |
|                 | ***Password field***  | *leave empty*       | *Error message*          | **pass**    |
|                 |                   | *enter valid data*| *Form submits*             |  **pass**   |
|                 |                   | *password does not match* | *Error message*         | **pass**    |
|                 |                   | *password does not match* | *Form won't submit*     | **pass**    |
|                 | ***Sign-in button***| *hover*            | *Lighter background colour* | **pass**|
|                 |                         | *click*    | *Form submits*          | **pass**    |
|                 |                   | *click*         | *Return to homepage*    | **pass**    |
|                 |                   | *click*         | *Success message to alert the user of a successful login* | **pass** |
|                 |                   |                      | *Automatically close alert after 2.8sec*| **pass**  |
|**Mobile view**   |                  |                   |                           |             |
|                  | `login` page     | *display*        | *Responsive*               |**pass**     |
|                 | **Navbar**        | *display*        | *Hamburger menu*           | **pass**    |
|                 | *Sign up link*      | *click*           | *Redirect to `signup` page*  |   **pass**  |
|                 | ***Username field***  | *leave empty*     |  *Error message*           | **pass**    |
|                 |                   | *enter valid data*| *Form submits*             |  **pass**   |
|                 |                   | *enter invalid format* | *Form won't submit*   | **pass**    | 
|                 |                   | *enter invalid format* | *Error message*       | **pass**    |
|                 | ***Password field***  | *leave empty*       | *Error message*          | **pass**    |
|                 |                   | *enter valid data*| *Form submits*             |  **pass**   |
|                 |                   | *password does not match* | *Error message*         | **pass**    |
|                 |                   | *password does not match* | *Form won't submit*     | **pass**    |
|                 | ***Sign-in button***|*click*    | *Form submits*          | **pass**    |
|                 |                   | *click*         | *Return to homepage*    | **pass**    |
|                 |                   | *click*         | *Success message to alert the user of a successful login* | **pass** |
|                 |                   |                      | *Automatically close alert after 2.8sec*| **pass**  |
|`logout`         |**Navbar**         | *display*         | *Display navbar*           |   **pass**  |
|                 |***Sign out button***| *hover*          | *Lighter background colour*| **pass**    |
|                 |                   | *click*    | *Form submits*               | **pass**    |
|                 |                   | *click*         | *Return to homepage*    | **pass**    |
|                 |                   | *click*         | *Success message to alert the user of a successful logout* | **pass** |
|                 |                   |                 | *Automatically close alert after 2.8sec*| **pass**  |
|                 |**Footer**         | *display*     | *Social icons are displayed at the bottom of the page* | **pass**|
|                 |                   | *hover*      | *Change scale **1.2***     | **pass**    |
|**Mobile view**       |                   |              |                            |              |
|`logout`         |**Navbar**         | *display*    | *Display hamburger menu*   |   **pass**  |
|                 |***Sign out button*** | *click*    | *Form submits*               | **pass**    |
|                 |                   | *click*         | *Return to homepage*    | **pass**    |
|                 |                   | *click*         | *Success message to alert the user of a successful logout* | **pass** |
|                 |                   |                 | *Automatically close alert after 2.8sec*| **pass**  |


### *Add recipe*
<br>

| Page/Status     | Element           |   Action          | Expected Result            | Pass/Fail   |
| ---             | ---               |   :---:           |    :---:                   |    :---:    |
|`add_recipe`     |**Navbar**         | *display*         | *Display navbar*           |   **pass**  |
|                 |                   | *access*          | *If an unauthorized user tries to access this page by changing the URL, redirect to 403 error page*| **pass** |
|  **logged-in**  | **Form**          | *leave empty*     |  *Form won't submit*       | **pass**    |
|                 |                   | *display*      | *Summernote display for ingredients, method, and notes*| **pass**  | 
|                 | *Image **Choose file** button*| *click*        | *Open device storage*      | **pass**    |
|                 |                | *display*      | *Placeholder image if no image selected*| **pass**|
|                 |                  | *display*      | *selected image name displayed*| **pass** |
|                 | ***Title field*** |  *no duplicates*   | *Error message*            | **pass**    |
|                 |                  |  *no duplicates*   | *Form won't submit*        | **pass**    |
|                 |                  | *max length* |*No more than 48 characters long* | **pass**    |
|                 |***Prep & Cook time field***| *display*          | *default 0 mins*             |**pass**     |   
|                 |                 | *max length*|*No more than 8 characters long* | **pass**     |
|                 | ***Cancel button*** | *hover* | *Lighter background colour*     | **pass**     |
|                 |                     | *click* | *Redirect to `all_recipes`*      | **pass**     |
|                 | ***Add recipe button*** | *hover* | *Lighter background colour* | **pass**     |
|                 |                     | *click* | *Form submits*                  | **pass**     |
|                 |                     | *click* | *Redirect to the newly created `recipe_detail` page*| **pass**     |
|                 |                     | *click* | *Success message to alert the user of a successfully added new recipe* | **pass** |
|                 |          |          | *Automatically close alert after 2.8sec*  | **pass**     |
|                 |**Footer**         | *display*     | *Social icons are displayed at the bottom of the page* | **pass**|
|                 |                   | *hover*      | *Change scale **1.2***     | **pass**    |
|**Mobile view**  |                   |              |                            |              |
|`add_recipe`     |**Navbar**         | *display*         | *Hamburger menu*      |   **pass**  |
|                 | `add_recipe` page | *display*         | *Responsive*          |  **pass**   |
|                 | ***Cancel button***| *click* | *Redirect to `all_recipes`*      | **pass**     |
|                 |***Add recipe button*** | *click* | *Form submits*                  | **pass**     |
|                 |                     | *click* | *Redirect to the newly created `recipe_detail` page*| **pass**     |
|                 |                     | *click* | *Success message to alert the user of a successfully added new recipe* | **pass** |
|                 |          |          | *Automatically close alert after 2.8sec*  | **pass**     |
|                 |**Footer**         | *display*     | *Responsive layout* | **pass**|


### *Update recipe*
<br>

| Page/Status     | Element           |   Action          | Expected Result            | Pass/Fail   |
| ---             | ---               |   :---:           |    :---:                   |    :---:    |
|`update_recipe`     |**Navbar**         | *display*         | *Display navbar*           |   **pass**  |
|                 |                   | *access*          | *If an unauthorized user tries to access this page by changing the URL, redirect to 403 error page*| **pass** |
|                 |  ***Form***       | *display*         |*Prepopulated data with last recipe content*| **pass** |
|                 |                   | *leave field empty* | *Form won't submit* | **pass**        |
|                 | ***Cancel button*** | *hover* | *Lighter background colour*     |      **pass**   |
|                 |                     | *click* | *Redirect to the last `recipe_detail` page*| **pass**  |
|                 |***Update recipe button*** | *hover* | *Lighter background colour* | **pass**     |
|                 |                     | *click* | *Form submits*                  | **pass**     |
|                 |                     | *click* | *Go to updated `recipe_detail` page*| **pass**     |
|                 |                     | *click* | *Success message to alert the user of the successful update of their recipe* | **pass** |
|                 |          |          | *Automatically close alert after 2.8sec*  | **pass**     |
|                 |**Footer**         | *display*     | *Social icons are displayed at the bottom of the page* | **pass**|
|                 |                   | *hover*      | *Change scale **1.2***     | **pass**    |
|**Mobile view**  |                   |              |                            |              |
|`update_recipe`     |**Navbar**         | *display*         | *Hamburger menu*      |   **pass**  |
|                 | `update_recipe` page | *display*         | *Responsive*          |  **pass**   |
|                 | ***Cancel button***| *click* | *Redirect to last `recipe_detail` page* | **pass**     |
|                 |***Update recipe button*** | *click* | *Form submits*                  | **pass**     |
|                 |                     | *click* | *Go to updated `recipe_detail` page*| **pass**     |
|                 |                     | *click* | *Success message to alert the user of successfully updating their recipe* | **pass** |
|                 |          |          | *Automatically close alert after 2.8sec*  | **pass**     |
|                 |**Footer**         | *display*     | *Responsive layout* | **pass**             |


### *Delete recipe*
<br>

| Page/Status     | Element           |   Action          | Expected Result            | Pass/Fail   |
| ---             | ---               |   :---:           |    :---:                   |    :---:    |
|`delete_recipe`     |**Navbar**         | *display*         | *Display navbar*           |   **pass**  |
|                 |                   | *access*          | *If an unauthorized user tries to access this page by changing the URL, redirect to 403 error page*| **pass** |
|                 | ***Text***           | *display*   |  *Display recipe_title within text*| **pass** | 
|                 | ***Cancel button*** | *hover* | *Lighter background colour*     |      **pass**   |
|                 |                     | *click* | *Redirect to the last `recipe_detail` page*| **pass**  |
|                 |***Update instead button*** | *hover* | *Lighter background colour* | **pass**     |
|                 |                     | *click* | *Go to `update_recipe` page with populated data*| **pass**      |
|                 | ***Delete button*** | *display*| *Warning red coloured box*| **pass**             |
|                 |                     | *hover* | *Darker background colour*     |      **pass**    |
|                 |                     | *click* | *Recipe removed from database* | **pass**
|                 |                     | *click* | *Redirect to `my_recipes` page*| **pass**  |
| |   |*click* | *Success message to alert the user of successfully deleting their recipe* | **pass** |
|                 |          |          | *Automatically close alert after 2.8sec*  | **pass**     |
|                 |**Footer**         | *display*     | *Social icons are displayed at the bottom of the page* | **pass**|
|                 |                   | *hover*      | *Change scale **1.2***     | **pass**    |
|**Mobile view**  |                   |              |                            |              |
|`delete_recipe`     |**Navbar**         | *display*         | *Hamburger menu*      |   **pass**  |
|                 | `delete_recipe` page | *display*         | *Responsive*          |  **pass**   |
|                 | ***Cancel button***| *click* | *Redirect to the last `recipe_detail` page* | **pass**     |
|                 |***Update Instead button*** | *click* | *Go to `update_recipe` page*  | **pass**     |
|                 | ***Delete button*** | *click* | *Recipe removed from database* | **pass** |
|                 |                     | *click* | *Redirct to `my_recipes` page*| **pass**  |
|                 |                     |*click*  | *Success message to alert the user of successfully deleting their recipe* | **pass**|
|                 |          |          | *Automatically close alert after 2.8sec*  | **pass**     |
|                 |**Footer**         | *display*     | *Responsive layout* | **pass**|

### *Update comment*
<br>

| Page/Status     | Element           |   Action      | Expected Result            | Pass/Fail   |
| ---             | ---               |   :---:       |    :---:                   |    :---:    |
|`update_comment`     |**Navbar**         | *display* | *Display navbar*           |   **pass**  |
|                 |                   | *access*          | *If an unauthorized user tries to access this page by changing the URL, redirect to 403 error page*| **pass** |
|                 |  ***Form***       | *display*         |*Prepopulated data with last recipe content*| **pass** |
|                 |                   | *leave field empty* | *Form won't submit* | **pass**        |
|                 | ***Cancel button*** | *hover* | *Lighter background colour*     |      **pass**   |
|                 |                     | *click* | *Redirect to the last `recipe_detail` page*| **pass**  |
|                 |***Update comment button*** | *hover* | *Lighter background colour* | **pass**     |
|                 |                     | *click* | *Form submits*                | **pass**     |
|                 |                     | *click* | *Redirect to the updated `recipe_detail` page*| **pass**     |
|                 |                     | *click* | *Success message to alert the user of a successful update of their comment* | **pass** |
|                 |          |          | *Automatically close alert after 2.8sec*  | **pass**     |
|                 |**Footer**         | *display*     | *Social icons are displayed at the bottom of the page* | **pass**|
|                 |                   | *hover*      | *Change scale **1.2***     | **pass**    |
|**Mobile view**  |                   |              |                            |              |
|`update_comment`     |**Navbar**         | *display*         | *Hamburger menu*      |   **pass**  |
|                 | `update_comment` page | *display*         | *Responsive*          |  **pass**   |
|                 |**Footer**         | *display*     | *Responsive layout* | **pass**|


### *Delete comment*
<br>

| Page/Status     | Element           |   Action      | Expected Result            | Pass/Fail   |
| ---             | ---               |   :---:       |    :---:                   |    :---:    |
|`delete_comment`     |**Navbar**         | *display* | *Display navbar*           |   **pass**  |
|                 |                   | *access*          | *If an unauthorized user tries to access this page by changing the URL, redirect to 403 error page*| **pass** |
| **logged-in**   |`delete_comment` page  | *display* | *The recipe title displayed in the confirmation message*| **pass**|
|                 |***Cancel button***| *click*       | *Return to `recipe_detail` page*   | **pass**    |
|                 |                   |  *hover*      | *Lighter background colour* | **pass**    |
|                 |***Delete button***|  *hover*      | *Darker background colour*  | **pass**    |
|                 |                   | *click*       | *Remove recipe from database*| **pass**   |
|                 |                   | *click*       | *Return to `my_recipes` page*|**pass**|
|                 |                     | *click* | *Success message to alert the user of the successful deletion of their comment* | **pass** |
|                 |          |          | *Automatically close alert after 2.8sec*  | **pass**     |
|                 |**Footer**         | *display*     | *Social icons are displayed at the bottom of the page* | **pass**|
|                 |                   | *hover*      | *Change scale **1.2***     | **pass**    |
|**Mobile view**  |                   |              |                            |              |
|`delete_comment`     |**Navbar**         | *display*         | *Hamburger menu*      |   **pass**  |
|                 | `delete_comment` page | *display*         | *Responsive*          |  **pass**   |
|                 |**Footer**         | *display*     | *Responsive layout* | **pass**              |


### *Newsletter*
<br>

| Page/Status     | Element           |   Action      | Expected Result            | Pass/Fail   |
| ---             | ---               |   :---:       |    :---:                   |    :---:    |
|`newsletter`     |**Navbar**         | *display*     | *Display navbar*           |   **pass**  |
|                 |**Form**           | *display*     | *Email field*              |  **pass**   |
|                 |                   | *leave empty* | *Error message*            | **pass**    |
|                 |                   |*invalid format*| *Error message*           | **pass**    |
|                 |**Subscribe button**| *hover*       | *Alternate colour*        | **pass**    |
|                 |                    | *click*       | *Email saved to database*  | **pass**    |
|                 |                    | *click*       | *Redirect to the homepage* | **pass**    |
|                 |                    | *click*       | *Success message of successfully subscribing* | **pass** |
|                 |                     |          | *Automatically close alert after 2.8sec*  | **pass**     |
|                 |**Footer**         | *display*     | *Social icons are displayed at the bottom of the page* | **pass**|
|                 |                   | *hover*      | *Change scale **1.2***     | **pass**    |


***

## Bugs

Issues were created on GitHub and noted with a `bug` label.
<br>

### Fixed Bugs

1. [auth.User.None displayed next to the 'star' icon](https://github.com/chris-townsend/PP4-Kitchen_Tales/issues/43)

*resolved - [593fc8e](https://github.com/chris-townsend/PP4-Kitchen_Tales/commit/593fc8e319ec4791a2098c2a25d226258d64b89c) The wrong item was being rendered
into the template*

`{{ recipe.like_recipe }` --> `{{ recipe.number_of_likes }}`

2. [Alert message not being displayed within coloured alert box](https://github.com/chris-townsend/PP4-Kitchen_Tales/issues/44)

*resolved - [5e7e796](https://github.com/chris-townsend/PP4-Kitchen_Tales/commit/5e7e796bee681e03ead4b4b709886dc166542865) Missing closing div tag*

3. [IntegrityError when a logged-in user attempts to submit a comment](https://github.com/chris-townsend/PP4-Kitchen_Tales/issues/45)

*resolved - missing line of code within the if/else statement of the post function*

`comment.post_id = recipe.id` in `views.py`

4. [Comment approval alert not being displayed in the correct place](https://github.com/chris-townsend/PP4-Kitchen_Tales/issues/46)

*resolved - [62976b1](https://github.com/chris-townsend/PP4-Kitchen_Tales/commit/62976b1af0ec5fe870a5f92f0817c221d44ac1d5)*

 *Import messages from django.contrib -*  `from django.contrib import messages`

 *Add success message to post variable after the comment gets saved -* 

  `messages.success(self.request, 'Your comment is awaiting approval')`

5. [FieldError within Recipe model form](https://github.com/chris-townsend/PP4-Kitchen_Tales/issues/47)

*resolved - Follow the error code and remove `created_date` from the fields*

6. [NameError: 'self' is not defined within MyRecipesView](https://github.com/chris-townsend/PP4-Kitchen_Tales/issues/49)

*resolved - Create a function that modifies the original queryset to only display recipes created by the logged-in user*

7. [Incorrect link from 'Sign up to star & bookmark recipes'](https://github.com/chris-townsend/PP4-Kitchen_Tales/issues/48)

*resolved - [93eaa72](https://github.com/chris-townsend/PP4-Kitchen_Tales/commit/93eaa7205849792b3e41595496f019574fcf062f)*

*Change the link to the correct location - `<a href="{% url 'account_signup' %}"`*

8. [The search icon is not being displayed correctly](https://github.com/chris-townsend/PP4-Kitchen_Tales/issues/50)

*resolved - [bbd95c7](https://github.com/chris-townsend/PP4-Kitchen_Tales/commit/bbd95c76d0b86f47692c8d768e7f6b2e56a592aa)*

*Create a form and style with bootstrap classes*

9. [NoReverseMatch error after setting an incorrect URL to cancel deleting a comment on a recipe](https://github.com/chris-townsend/PP4-Kitchen_Tales/issues/51)

*resolved - [3a01ac0](https://github.com/chris-townsend/PP4-Kitchen_Tales/commit/3a01ac05a1eff73fb020401b637e8d154e9d33c4)*

*Change the href within the `delete_comment.html` template to cancel deleting a comment.* Add missing code `.post` from the Comment model.

10. [Navbar 'active' class not working correctly after page change](https://github.com/chris-townsend/PP4-Kitchen_Tales/issues/52)

*resolved - Remove the current **active** class from Home in the base template. Add JavaScript to manage the `<li>` items when active and remove them when a user changes the page.*

*Credit - [Bootstrap navbar Active State not working](https://stackoverflow.com/questions/24514717/bootstrap-navbar-active-state-not-working)*

11. [Placeholder image automatically added to a new recipe instead of the user-uploaded image](https://github.com/chris-townsend/PP4-Kitchen_Tales/issues/53)

*resolved - [09f9c79](https://github.com/chris-townsend/PP4-Kitchen_Tales/commit/09f9c79793272f6c000d202c9f3f30df8cb2f6bd)*

*Missing code within `AddRecipeView` in `views.py` - `recipe.image = request.FILES['image']`*

12. [MultiValueDictKeyError when a user goes to update a recipe](https://github.com/chris-townsend/PP4-Kitchen_Tales/issues/54)

*resolved - [aa6c9f8](https://github.com/chris-townsend/PP4-Kitchen_Tales/commit/aa6c9f8e8344f044ba26c53f23bbb3b82e9ed7e3)*

*Add the correct line of code and remove commented-out unused code*

#

### Unfixed Bugs

1. [Placeholder image automatically set when updating a recipe](https://github.com/chris-townsend/PP4-Kitchen_Tales/issues/55)

*When a user goes to update their recipe, the placeholder image replaces their image unless it has been specified again. This should be an easy fix by adding to the if/else statement*

This bug related to the recipe model was attempted to be fixed with commit [aec7728](https://github.com/chris-townsend/PP4-Kitchen_Tales/commit/aec7728ce67fe8c912b14b2bccdac25225c61f23). Initially, it was believed that by adding an image_url field to the recipe model and adjusting the recipe_detail template to take this field into account would resolve the issue. However, despite these efforts, the bug persists.


***

## Automated Testing

Several unit tests were written to test the views, forms, and database models. These can be found in the [`recipes`](https://github.com/chris-townsend/PP4-Kitchen_Tales/tree/main/recipes) folder and test files begin with `test_`.

<details>

 **<summary>Coverage report</summary>**

![Automated testing coverage report](docs/testing/automated/coverage-report.webp)

</details>

<br>

*Coverage report generated from* [*Coverage.py*](https://coverage.readthedocs.io/en/7.1.0/)

#

<br>

[Back to top ⇧](#contents)

[Back to *README.md*](/README.md#testing)
***
