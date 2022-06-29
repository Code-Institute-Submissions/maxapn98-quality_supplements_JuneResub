# Quality Supplements

This is an E-commerce website for an online supplement shop. Users can search for information on products, as well they can read reviews or leave a review about products, purchase them online, and pay online.

## UX

**What is the idea of the project?**

- The idea is to build an online e-commerce web application for a supplement store, with a payment system, and an authentication system including email confirmations and user profiles.

**Who is the shopper?**

- Shoppers of this website are people who are interested in supplements purchase.

### Strategy Plane

**The site’s owner goals:**

- Owner wants to build an online shop for supplements.
- Owner wants users to be able to create user accounts in the web store.
- Owner wants for both registered and non-registered users to be able to navigate website pages, view products, and view reviews.
- Owner thinks that only registered users should have the option to leave reviews.

**The site’s user goals:**

- User should be able to filter products by specific category, price and rating.
- User should be able to view product reviews.
- User should be able to leave a review on products.
- User should be able to register and create an account at our web store.
- User should be able to look view their account, purchased order and account information.
- User should be able to search for a specific product by name or description.
- User should be able to put desired products in the bag and also be able to decide on the quantity he or she wants to purchase.
- User should be able to access shopping bag quickly.
- User should be able to use the bag to view products to be purchased and have the ability to edit the bag contents on the go.
- User should be able to modify the number of products wanted in the bag.

### Scope Plane

**The features that the website should include:**

- [x] Landing page
- [x] Products page
- [x] Login form
- [x] Profile page
- [x] Registration form.
- [x] Shopping bag page
- [x] Contact page
- [x] Ability to Search specific products by name.
- [x] Ability to sort products by category.
- [x] Ability to sort products by rating, and price.
- [x] Ability to enter in the specific product page and look at description, image, price, category
- [x] Ability to add a quantity of the product to a shopping bag
- [x] Ability to see reviews.
- [x] Ability to add a review.
- [x] Ability to add the wanted product to the shopping bag.
- [x] Ability to modify shopping bag quantity of products.
- [x] Ability to checkout
- [x] Ability for online payment.
- [x] Ability to save delivery information.

### Structure Plane

**The information architutre:**

- Flow of information should be clear and consistent throughout the design.
  The interaction design:
- Once opened website user will be informed about the website's information so that he/she can easily start to shop on this website.
- The landing page should also contain visuals in form of images that convey the meaning that this is a website that has something to do with the supplements.
- The landing page should contain a call-to-action to invoke a lead.
- The landing page will be provided with different buttons for categorizing the products.
- On the landing page user can also easily use the search input to find a specific product by its name or description.
- In the right top corner of the website user will be able to see a shopping bag with the current amount, Profile button witch will lead a user to the profile page once a user is registered, if not he will be able to easily get registred, and a contact button for the contact page.
- Products page will contain a preview of all the products/supplements that can be found in the database.
- Supplements should be displayed on the products page using bootstrap cards where each card will contain an image, name, price, rating, and category.
- Once clicked on the card user will be provided with a product image, name, price, rating, category, description, and product review, he will be able to increment decrement the quantity wanted to be added to the shopping bag and a button which will add the products to shopping bag.
- Registered users will be able to create reviews, update their existing reviews or delete them.
- Review will contain one input field and submit button.
- The profile page should contain delivery information that the user has provided when he signed up, update them when needed, and order history.
- Contact page will contain contact information and an email form.
- Contact information should contain the company phone and email address.
- Shopping bag page will contain product info, product name, ID, the number of products added, the price for single and subtotal products, bag total, delivery price, and a grand total.
- Once clicked on the checkout button user will need to provide delivery information and cart number.
- The checkout page will contain delivery information and an order summary with the total price.

### Skeleton plane

- Homepage
- products page
- Profile page
- Registration page
- Contact page
- Shopping bag page
- Checkout page
- Checkout success page

### Navigation

- User will be able to navigate the website using the websites' navigation.
- The profile page will only be made available to the user if he is logged in.
- The navbar will contain search input, Profile page, Contact page, Shopping bag with bag total underneath the icon.
- Navbar will contain the website logo.
- Nav menu on the phone will be activated by clicking on a burger icon.

## SQL Database Structure

![checkout app](/docs/images/database-diagram-01.png)

## Deployment

Before following any of these steps make sure that you have the latest dependencies installed in your application environment. All of the application dependencies are listed within the requrements.txt file found in project's root directory.

To install dependencies while in project's root dir. run the following command:
`pip3 install -r requirements.txt`

**Heroku Deployment:**

1. Go to project [repository](https://github.com/maxapn98/quality_supplements)
2. Fork the project by clicking on the _Fork_ button found in the top right corner of the viewport.
3. Go to [Heroku](https://www.heroku.com/) and log in. If you don't have an account, create one and then login.
4. In your dashboard click on "Create New App".
5. Give your application name and select region closest to your location.
6. Setup automatic deployment by clicking on "Github" icon inside of the "Deployment Method" section.
7. Click on "Connect GitHub" and connect your github acc. to Heroku.
8. Find the repo you have created when you followed the first two steps.
9. Once you find your repo, click the "connect" button.
10. Now you want to setup all of the environment variables that are required by the app in order for it to run. To do that find and click on "Reveal Config Var".

| Variable Name         | Variable Description                                                                                                                                                                                                                                                                                                                           |
| --------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| DEVELOPMENT           | Optional variable. If present in the os environ. then application will run in development mode. It can be set to anything as the code checks only for its existence.                                                                                                                                                                           |
| SECRET_KEY            | Mandatory variable. Must contain cryptographic key that is used for signing. It is used to generate tokens and hashes.                                                                                                                                                                                                                         |
| DATABASE_URL          | Optional variable. It should contain the database url. If not provided application code defaults to sqlite3. _Heroku creates this variable when you provision PostgreSQL service. Do not set it manually as on heroku it is a dynamic variable set and changed by Heroku service._                                                             |
| USE_AWS               | Optional variable. If present in the environ. variables the system will use code block for using AWS S3 bucket. Hence additional environ. variables will be required. _Note: Django needs additional service to serve static files. If you don't set USE_AWS see to implement some other service such as whitenoise to serve the static files_ |
| AWS_ACCESS_KEY_ID     | Identity token for AWS S3 bucket service.                                                                                                                                                                                                                                                                                                      |
| AWS_SECRET_ACCESS_KEY | Authorization key used to access S3 store.                                                                                                                                                                                                                                                                                                     |
| STRIPE_PUBLIC_KEY     | Required for Stripe API. Used in your client-side to tokenize payment information.                                                                                                                                                                                                                                                             |
| STRIPE_SECRET_KEY     | Required for Stripe API. Used on the backend to authenticate requests.                                                                                                                                                                                                                                                                         |
| STRIPE_WH_SECRET      | Required for Stripe API. Used by Stripe for webhooks WebHooks                                                                                                                                                                                                                                                                                  |

11. Once you have your environment variables setup click on "Enable Automatic Deployment".
12. Select your branch.
13. Heroku will now build the app. Once it is done click the button to view the deployed app.

**Local Deployment:**

1. Go to project [repository](https://github.com/maxapn98/quality_supplements)
2. Fork the project by clicking on the _Fork_ button found in the top right corner of the viewport.
3. Go to your forked repo and clone it to your local machine using git command.  
   `git clone <SSH>`
4. Go into your cloned project on your local machine using bash command.  
   `cd ~/quality_supplements`
5. Once inside init. python environment using the following terminal commands.
   - `python3 -m venv <virtual_env_name>` Creates virtual environment under the name you provide within the current active directory.
   - `source <virtual_env_name>/bin/activate` Activates the virtual environment that you have created.
6. Now you will need to setup env.py file within the root dir of your forked project. This will contain all of your environment variables that are used by this app. Refer to the table above in order to understand what variables you need to set.
7. Run `pip3 install -r requirements.txt` to install all of the dependencies within your active virtual environment.
8. Once you have set your environment variables migrate and load the json data from fixtures.
9. Run server on your local machine using `python3 manage.py runserver`

## Left To Implement

- Connect with social media
- Add edit/delete on reviews
- Testing for readme
- Wireframes
- Code validation

## Technologies & Languages

**Languages used in this project are:**

- Python
- JavaScript
- HTML (Markup Language)
- CSS

**Technologies used in this project are:**

- Django
  - Python based framework that follows MVC architectural pattern.
- JQuery
  - JavaScript based library used to provide abstract layer to JS for ease of use and faster development.
- BootStrap
  - CSS library with pre-defined classes allowing for faster development of responsive and styled webpages.
- Stripe
  - API service that offers payment processing for e-commerce websites.
- Font Awesome
  - Font and Icon toolkit.
- SQL
  - Domain-specific language designed for managing data held in relational database management system.
- Amazon S3 Bucket
  - Cloud object storage.
- dbdiagram.io
  - Used to create diagrams of database models during initial planing.

## Credits

### Content

### Media

- Photos used in this site development were obtained from [Unsplash.com](https://unsplash.com/)