# Testing


### Contents
- [Testing Stories for UX](#testing-user-stories-from-the-user-experience-ux-section)
- [Validator Testing](#validator-testing)
  * [HTML](#html)
  * [CSS](#css)
  * [Javascript](#javascript)
  * [Python](#python)
  * [Lighthouse](#lighthouse)
- [Browser Testing](#browser-testing)
- [Device Testing](#device-testing)
- [Manual Testing](#manual-testing)
  * [Site Navigation](#site-navigation)
  * [Home Page](#home-page)
- [Bugs](#bugs)
  * [Fixed Bugs](#fixed-bugs)
  * [Unfixed Bugs](#unfixed-bugs)
- [Automated Testing](#automated-testing)

***


## Testing User Stories from the User Experience (UX) Section


### EPIC | *Early Deployment*
<br>

*[As a developer, I can create an account with Heroku to process setting up the app so that I can deploy my site to Heroku](https://github.com/chris-townsend/PP4-Kitchen_Tales/issues/1)*

![Create Heroku account](static/images/heroku-create-account.webp)


*[As a developer, I can add my config vars to my app in Heroku so that I can allow deployment to production](https://github.com/chris-townsend/PP4-Kitchen_Tales/issues/2)*

![Heroku config vars input](static/images/heroku-config-vars.webp)
![Add heroku config vars](static/images/heroku-config-var-setup.webp)


*[As a developer, I can create a Procfile within my project so that the application will run in Heroku](https://github.com/chris-townsend/PP4-Kitchen_Tales/issues/3)*

![Create Procfile](static/images/kitchen-tales-create-procfile.webp)

   - **More information on setting up the Procfile can be found within the [Django](#django) section of the readme**


*[As a developer, I can create a Cloudinary account so that I can store my media files](https://github.com/chris-townsend/PP4-Kitchen_Tales/issues/4)*

![Create Cloudinary account](static/images/create-cloudinary-account.webp)


*[As a developer, I can connect my GitHub account for the final deployment stages so that I can allow deployment to production](https://github.com/chris-townsend/PP4-Kitchen_Tales/issues/5)*

![Connect GitHub account](static/images/heroku-deployment-method.webp)


#

### EPIC | *Initial Django Setup*
<br>

*[As a developer, I can set up Django and supporting libraries so that I can start developing the site](https://github.com/chris-townsend/PP4-Kitchen_Tales/issues/6)*

![Setup Django](static/images/heroku-connected-app.webp)


*[As a developer, I want to set up my environment to secure my private keys so that I do not expose them in an insecure way](https://github.com/chris-townsend/PP4-Kitchen_Tales/issues/7)*

***Detailed information of the initial Django setup can be found [here](../PP4-Kitchen_Tales/README.md#installing-django-and-supporting-libraries)***


*[As a developer, I should install the necessary Django components so that I can address authentication, registration, and account management for users](https://github.com/chris-townsend/PP4-Kitchen_Tales/issues/8)*

***Detailed information of the initial Django setup can be found [here](../PP4-Kitchen_Tales/README.md#installing-django-and-supporting-libraries)***


*[As a developer, I should install the necessary Django components so that I can display a comments section that is more appealing to the user](https://github.com/chris-townsend/PP4-Kitchen_Tales/issues/9)*

***Detailed information of the initial Django setup can be found [here](../PP4-Kitchen_Tales/README.md#installing-django-and-supporting-libraries)***

*[As a developer, I should set up the necessary database items so that the database is viewable through Heroku](https://github.com/chris-townsend/PP4-Kitchen_Tales/issues/40)*

***Detailed information of setting up the ElephantSQL database can be found [here](../PP4-Kitchen_Tales/README.md#elephant-sql)***


#

### EPIC | *Website Functionality*
<br>

*[As a first-time user, I can immediately understand the purpose of the website, and I know if it's what I'm looking for](https://github.com/chris-townsend/PP4-Kitchen_Tales/issues/10)*

![Kichen Tales welcome message](static/images/kitchen-tales-welcome.webp)


*[As a User, I can view recipes, without having to sign-up to enjoy the site's content](https://github.com/chris-townsend/PP4-Kitchen_Tales/issues/11)*

![Kichen Tales recipes tab](static/images/kitchen-tales-recipes-tab.webp)

![Kichen Tales recipes](static/images/kitchen-tales-recipes.webp)


*[As a User, I can view recipes on my mobile so that I don't have to rely on using a computer](https://github.com/chris-townsend/PP4-Kitchen_Tales/issues/13)*

![Kichen Tales mobile friendly recipe](static/images/kitchen-tales-mobile-recipe.webp)

![Kichen Tales mobile friendly test](static/images/kitchen-tales-mobile-friendly-test.webp)

***For more detailed information about mobile testing, please click [here](#device-testing)***


*[As a User, I can view comments on recipes so that I can read other user's feedback](https://github.com/chris-townsend/PP4-Kitchen_Tales/issues/34)*

![Kichen Tales comment section](static/images/kitchen-tales-comment-section.webp)


*[As a Logged-in User, I can comment on recipes so that I can leave my feedback for others](https://github.com/chris-townsend/PP4-Kitchen_Tales/issues/35)*

![Kichen Tales comment section](static/images/kitchen-tales-leave-comment.webp)


*[As a developer, I can add a favicon so that the site looks more distinguishable](https://github.com/chris-townsend/PP4-Kitchen_Tales/issues/41)*

![Kichen Tales tab](static/images/kitchen-tales-tab.webp)

![Kichen Tales favicon](static/images/kitchen-tales-favicon-large.webp)

#

### EPIC | *Navigation*
<br>

*[As a User, I can navigate around the site so that I can easily view desired content](https://github.com/chris-townsend/PP4-Kitchen_Tales/issues/14)*

![Kichen Tales navbar](static/images/kitchen-tales-navbar.webp)

![Kichen Tales navbar hover](static/images/kitchen-tales-navbar-hover.webp)

- By using CSS's hover effect, the user know's what tab they are clicking on as it underlines the title. 

![Kichen Tales navbar authorized user](static/images/kitchen-tales-navbar-auth-user.webp)

- A logged-in user can see their own dropdown-menu options by clicking on their name with the user icon. This menu gives the option for a user to add a new recipe, see there own created recipes, their favourite starred recipes and an option to logout of their account.


*[As a User, I can search for the desirable recipe by keyword so that I can find a specific recipe fast](https://github.com/chris-townsend/PP4-Kitchen_Tales/issues/15)*

![Kichen Tales search bar](static/images/kitchen-tales-search-bar.webp)

![Kichen Tales searched results](static/images/kitchen-tales-search-results.webp)

#

### EPIC | *User Recipe Management*
<br>

*[As a logged-in User, I can create recipes so that I can add them to the site](https://github.com/chris-townsend/PP4-Kitchen_Tales/issues/16)*

![Kichen Tales add recipe tab](static/images/kitchen-tales-add-recipe-tab.webp)

![Kichen Tales add recipe page](static/images/kitchen-tales-add-recipe.webp)

![Kichen Tales add recipe text](static/images/kitchen-tales-add-recipe-text.webp)


*[As a logged-in User, I can view all the recipes that I have created so that I can go back to them at a later date](https://github.com/chris-townsend/PP4-Kitchen_Tales/issues/17)*

![Kichen Tales my recipes tab](static/images/kitchen-tales-my-recipes-tab.webp)

![Kichen Tales my recipes page](static/images/kitchen-tales-my-recipes.webp)

*[As a logged-in User, I can update and edit my recipes so that I can update any changes or mistakes that I have made](https://github.com/chris-townsend/PP4-Kitchen_Tales/issues/18)*

If the logged-in user is the author of the recipe, an edit button is shown next to the recipe image. When a user hovers over the edit button, it is displayed underlined.

![Kichen Tales update button on hover](static/images/kitchen-tales-edit-button.webp)

![Kichen Tales update recipe page](static/images/kitchen-tales-update-recipe.webp)


*[As a logged-in User, I can delete any personal recipes so that I can remove them if necessary](https://github.com/chris-townsend/PP4-Kitchen_Tales/issues/19)*

![Kichen Tales delete recipe button on hover](static/images/kitchen-tales-delete-button.webp)
![Kichen Tales delete recipe page](static/images/kitchen-tales-delete-recipe-page.webp)


*[As a logged-in User, I can view my liked recipes so that I can return to them easily](https://github.com/chris-townsend/PP4-Kitchen_Tales/issues/39)*

![Kichen Tales saved recipes tab](static/images/kitchen-tales-saved-recipes-tab.webp)

![Kichen Tales liked recipes page](static/images/kitchen-tales-liked-recipes-page.webp)

*[As a logged-in User, I can like or star a recipe so that I can bookmark it for later](https://github.com/chris-townsend/PP4-Kitchen_Tales/issues/42)*

![Kichen Tales like this recipe text and icon](static/images/kitchen-tales-click-to-bookmark.webp)

![Kichen Tales number of likes](static/images/kitchen-tales-number-of-likes.webp)

#

### EPIC | *User Account Management*
<br>

*[As a User, I can register for an account so that I can interact with the site content](https://github.com/chris-townsend/PP4-Kitchen_Tales/issues/22)*

![Kichen Tales sign up tab](static/images/kitchen-tales-sign-up-tab.webp)

![Kichen Tales sign up button](static/images/kitchen-tales-sign-up-button.webp)

![Kichen Tales sign up text](static/images/kitchen-tales-sign-up-text.webp)


*[As a User, I can log into my account so that I can manage my recipes](https://github.com/chris-townsend/PP4-Kitchen_Tales/issues/24)*

![Kichen Tales sign in tab](static/images/kitchen-tales-sign-in.webp)

![Kichen Tales sign in page](static/images/kitchen-tales-sign-in-page.webp)


*[As a User, I can safely log out of my account so that I can disconnect from the site](https://github.com/chris-townsend/PP4-Kitchen_Tales/issues/25)*

![Kichen Tales sign out tab](static/images/kitchen-tales-sign-out-tab.webp)

![Kichen Tales sign out page](static/images/kitchen-tales-sign-out-page.webp)


*[As a logged-in User, I can see my login status so that I know if I am logged in or out of my account](https://github.com/chris-townsend/PP4-Kitchen_Tales/issues/26)*

![Kichen Tales login status](static/images/kitchen-tales-login-status.webp)

![Kichen Tales navbar status for logged in user](static/images/kitchen-tales-logged-in-navbar.webp)

#

### EPIC | *Admin Features & Owner Objectives*
<br>

*[As a Site admin, I can create, edit and delete recipes and comments so that I can control the site content](https://github.com/chris-townsend/PP4-Kitchen_Tales/issues/28)*

![Kichen Tales admin panel](static/images/django-admin-panel.webp)

![Kichen Tales admin recipe panel](static/images/django-recipe-panel.webp)

![Kichen Tales admin comment panel](static/images/django-comment-panel.webp)


*[As a Site admin, I can authorize comments so that I can review the content before it's made public](https://github.com/chris-townsend/PP4-Kitchen_Tales/issues/29)*

![Kichen Tales admin panel approve comments](static/images/django-admin-approve-comment.webp)


*[As a Site owner, I would like to display my social icons so that I can promote my other channels](https://github.com/chris-townsend/PP4-Kitchen_Tales/issues/31)*

![Kichen Tales social icons](static/images/kitchen-tales-social-icons.webp)


***

## Validator Testing

![HTML w3c validator](static/images/HTML-w3c-validation.webp)

The *[W3C HTML validator](https://validator.w3.org/)* was used to test all HTML pages, **no errors** were reported in the final deployment.


### HTML

| Page                   | Status      |              | URL         |
| ---                    |        ---: |  ---         |        ---: |
|                        | *logged-in* | *logged-out* |             |
|404.html                |             |              |             |
|500.html                |             |              |             |
|add_recipe.html         |   *pass*    |   *n/a*      |  *[result](https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fkitchen-tales.herokuapp.com%2Fadd_recipe%2F#l189c24)*           |
|all_recipes.html        |   *pass*    |   *pass*     |  *[result](https://validator.w3.org/nu/?doc=https%3A%2F%2Fkitchen-tales.herokuapp.com%2Fall_recipes%2F)*    |
|base.html               |   *pass*    |   *pass*     |  *[result](https://validator.w3.org/nu/?doc=https%3A%2F%2Fkitchen-tales.herokuapp.com%2F)*    |
|delete_comment.html     |   *pass*    |   *n/a*      |  *[result](https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fkitchen-tales.herokuapp.com%2Fdelete_comment%2F62%2F#l189c24)*           |
|delete_recipe.html      |   *pass*    |   *n/a*      | *[result](https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fkitchen-tales.herokuapp.com%2Fdelete_recipe%2F62%2F#l189c24)*   |
|footer.html             |   *pass*    |   *pass*     | *[result](https://validator.w3.org/nu/?doc=https%3A%2F%2Fkitchen-tales.herokuapp.com%2F)*    |
|index.html              |   *pass*    |   *pass*     | *[result](https://validator.w3.org/nu/?doc=https%3A%2F%2Fkitchen-tales.herokuapp.com%2F)*    | 
|my_recipes.html         |   *pass*    |   *n/a*      | *[result](https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fkitchen-tales.herokuapp.com%2Fmy_recipes%2F#l189c24)* |
|my_starred_recipes.html |   *pass*    |   *n/a*      |  *[result](https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fkitchen-tales.herokuapp.com%2Fmy_starred_recipes%2F#l189c24)*|
|newsletter.html         |   *pass*    |   *pass*     |  *[result](https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fkitchen-tales.herokuapp.com%2Fnewsletter#l189c24)*    |
|recipe_detail.html      |   *pass*    |   *pass*     |  *[result](https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fkitchen-tales.herokuapp.com%2Frecipe_detail%2Fbutternut-squash-sage-risotto%2F#l189c24)*    |
|recipe_paginator.html   |   *pass*    |    *pass*    |      -      |
|search_results.html     |   *pass*    |    *pass*    | *[result](https://validator.w3.org/nu/?doc=https%3A%2F%2Fkitchen-tales.herokuapp.com%2Fsearch_results%2F)* |
|update_comment.html     |   *pass*    |    *n/a*     | *[result](https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fkitchen-tales.herokuapp.com%2Fupdate_comment%2F62%2F#l189c24)*            |
|update_recipe.html      |   *pass*    |    *n/a*     | *[result](https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fkitchen-tales.herokuapp.com%2Fupdate_recipe%2F62%2F#l189c24)* |
|login.html              |   *pass*    |    *pass*    | *[result](https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fkitchen-tales.herokuapp.com%2Faccounts%2Flogin%2F#l189c24)*           |
|logout.html             |   *pass*    |    *n/a*     | *[result](https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fkitchen-tales.herokuapp.com%2Faccounts%2Flogout%2F#l189c24)*            |
|signup.html             |   *n/a*     |    *pass*    | *[result](https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fkitchen-tales.herokuapp.com%2Faccounts%2Fsignup#l189c24)*           |

***

### CSS 

The *[W3C CSS Validator](https://jigsaw.w3.org/css-validator/)* was used to validate the project, the results are shown below with **no errors reported.**

![CSS w3c validator](static/images/CSS-w3c-validation.webp)
![CSS Result](static/images/CSS-validation-pass.webp)

- *[ CSS results](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fkitchen-tales.herokuapp.com%2F&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en)*

***

### JavaScript

*[JSHint](https://jshint.com/)* was used to check the JavaScript within the base template. The JavaScript code has been placed in `<script>` tags at the bottom of the `base.html` template and as there is very little JavaScript code, I felt it was not worth placing in its own file. The results came back with no errors but a few undefined variables. I have left this as it is with a detailed comment above the variables to explain their function.

![JSHint Logo](static/images/testing-jshint.webp)
![JavaScript Code to test](static/images/testing-jshint-code.webp)
![JShint test result](static/images/testing-jshint-result.webp)


***


### Python

***

### Lighthouse 

***

## Browser Testing
#


***

## Device Testing
#

***

## Manual Testing
#
***


## Bugs
#
### Fixed Bugs

### Unfixed Bugs

***


## Automated Testing
#

[Back to top ⇧](#contents)





