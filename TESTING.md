# Testing


### Contents
- [Testing Stories for UX](#testing-user-stories-from-the-user-experience-ux-section)
- [Validator Testing](#validator-testing)
  * [HTML](#html)
    + [Fixed Errors](#fixed-errors)
    + [Unfixed Errors](#unfixed-errors)
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


*[As a logged-in User, I can view all the recipes that I have created so that I can go back to them at a later date](https://github.com/chris-townsend/PP4-Kitchen_Tales/issues/17)*

![Kichen Tales my recipes tab](static/images/kitchen-tales-my-recipes-tab.webp)

![Kichen Tales my recipes page](static/images/kitchen-tales-my-recipes.webp)

*[As a logged-in User, I can update and edit my recipes so that I can update any changes or mistakes that I have made](https://github.com/chris-townsend/PP4-Kitchen_Tales/issues/18)*


*[As a logged-in User, I can delete any personal recipes so that I can remove them if necessary](https://github.com/chris-townsend/PP4-Kitchen_Tales/issues/19)*


*[As a logged-in User, I can give a recipe a rating so that I can provide feedback](https://github.com/chris-townsend/PP4-Kitchen_Tales/issues/20)*


*[As a logged-in User, I can view my liked recipes so that I can return to them easily](https://github.com/chris-townsend/PP4-Kitchen_Tales/issues/39)*

*[As a logged-in User, I can like or star a recipe so that I can bookmark it for later](https://github.com/chris-townsend/PP4-Kitchen_Tales/issues/42)*

#

### EPIC | *User Account Management*
<br>

*[As a User, I can register for an account so that I can interact with the site content](https://github.com/chris-townsend/PP4-Kitchen_Tales/issues/22)*


*[As a User, I can log into my account so that I can manage my recipes](https://github.com/chris-townsend/PP4-Kitchen_Tales/issues/24)*


*[As a User, I can safely log out of my account so that I can disconnect from the site](https://github.com/chris-townsend/PP4-Kitchen_Tales/issues/25)*


*[As a logged-in User, I can see my login status so that I know if I am logged in or out of my account](https://github.com/chris-townsend/PP4-Kitchen_Tales/issues/26)*

#

### EPIC | *Admin Features & Owner Objectives*
<br>

*[As a Site admin, I can create, edit and delete recipes and comments so that I can control the site content](https://github.com/chris-townsend/PP4-Kitchen_Tales/issues/28)*


*[Authorize recipes and comments - As a Site admin, I can authorize recipes and comments so that I can review the content before it's made public](https://github.com/chris-townsend/PP4-Kitchen_Tales/issues/29)*


*[As a Site owner, I would like to display my social icons so that I can promote my other channels](https://github.com/chris-townsend/PP4-Kitchen_Tales/issues/31)*


***

## Validator Testing
#

### HTML

#### Fixed Errors

#### Unfixed Errors

***

### CSS 

***

### Javascript

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





