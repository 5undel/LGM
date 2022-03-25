# Lets Get Moving
LGM is a gym for everyone, regardless of experience or physique.
At LGM, everyone is welcome to improve and feel better.

## UX
- As a new user, you will be able to easily navigate around the page with a simple dropdown menu, two quick links on the main page.

- user can register and obtain gym membership through simple and clear directives

- On the user's page you can save personal info, see how much time they have left on the membership

- Users can submit a booking request to one or more of our coaches


## Features

- Main Page
  ![image](media/main.png)

- Membership
  ![image](media/membership.png)

- Coach
  ![image](media/coach.png)

- Login
  ![image](media/login.png)

- Regester
  ![image](media/reg.png)

- payment
  ![image](media/pay.png)

## Deployment
  #### Local deployment
   - repo is found here https://github.com/5undel/LGM
   - Click the green button "Gitpod"
   - Lunch the site
   - type in the terminal - pip3 install django - to install django to the project
   - In the terminal - pyton manage.py runserver
   -  click the link the pops up in the right bottom corner 
   -Or click Ctrl + http://127.0.0.1:8000/ in the terminal

  #### Heroku Setup and CLI

This project has been deployed to Heroku.
Steps taken to deploy are as follows:

- Create a **requirements.txt** file using the terminal command `pip3 freeze --local > requirements.txt`
- Create a **Procfile** with the terminal command `echo web: python3 run.py > Procfile`
- install whitenoise - `pip install whitenoise` - whitenoise will store the static file and imgaes for the project.
- `git add` and `git commit` the new **requirements** and **Procfile**, then `git push` the project to GitHub.

- Navigate over to Heroku.com
- Click the "new" button, and give the project a name & set the region to Europe.
- From the Heroku dashboard of your newly created application, click on "Deploy" > "Deployment method" and select GitHub.
- Confirm the linking of the Heroku app to the correct GitHub repository.
- Select "Enable Manual Deployment", and then click the "Deploy" button.
- In your app settings on heroku > click Config Vars > This is where you save all your sensitive keys.

 - The live link can be found here - https://lets-get-moving.herokuapp.com/
 - Click the lgin link at the top left, at the login page click the register link to create a account. 

- Create a stripe account.  [stripe](https://stripe.com/en-se?utm_campaign=paid_brand-SE_se_Search_Brand_Stripe-6498153775&utm_medium=cpc&utm_source=google&ad_content=382002499158&utm_term=kwd-295607662702&utm_matchtype=e&utm_adposition=&utm_device=c&gclid=Cj0KCQjw0PWRBhDKARIsAPKHFGhGqisIxU7fhbNJXg34m-DUA8TGVmvdUXP36t5kqUPKwDhp0V2l1XIaAh2WEALw_wcB)

- Verify your business (to use it in production).
- Install stripe package using pip install stripe in the terminal.
- after this you have to freeze the requirements with command `pip3 freeze --local > requirements.txt` in the teminal.

- You have to add this line to your corejs block - "https://js.stripe.com/v3/" 
<br/>
- To obtain the API Keys > log in to the Stripe dashboard > To obtain the production keys, verify your account first > obtain a pair of productions and test keys.

- Configuring stripe >

        ```
          # Stripe
          STRIPE_CURRENCY = 'usd'
          STRIPE_PUBLIC_KEY = os.getenv('STRIPE_PUBLIC_KEY', '')
          STRIPE_SECRET_KEY = os.getenv('STRIPE_SECRET_KEY', '') 
        ```
- Create a env.py to store your sensitive keys, this names most be the same ass your Config Vars from heroku for the system to get them >

        ```
          os.environ["STRIPE_PUBLIC_KEY"] = "Your test key from stripe"
          os.environ["STRIPE_SECRET_KEY"] = "Your secret key from stripe"
        ```


## Test
- Jigsaw - [Jigsaw page](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2F8000-5undel-lgm-jmjnwwifs0s.ws-eu38.gitpod.io%2F&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=sv/)

  ![image](media/jigsaw.png) 
- Lighthouse

  ![image](media/lighthouse.png)

## WEBBROWSER
- Chrome
    ![image](media/chrome.png)

- Edge
    ![image](media/edge.png)

- Fierfox
    ![image](media/firefox.png)

## Credit

- Style and layout - [Bootstrap](https://getbootstrap.com/)
- Background image - [Unsplash](https://unsplash.com/s/photos/gym)
- Countdown time - [stackoverflow](https://stackoverflow.com/questions/38276672/todays-date-30-days-in-javascript)

## Future ideas
 - Future ideas are that the user should be able to book current appointments directly with the chosen coach

 - The owner should be able to have an online store

 - 
