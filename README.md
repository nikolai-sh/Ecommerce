# Ecommerce

This is the test task:

1. Create a new public project on GitHub or any Mercurial hosting and periodically
   to record the progress of work there. Register exceptions in .gitignore (or .hgignore):
   only the source code should be included in the project version control system,
   no backups, compiled modules and database.

   Create a new Django project.
   - create a virtual environment for the project,
   - create a requirements.txt file in the root of the project, add the dependencies there:

     Django> = 3.2, <3.3
     django-annoying

   - install the required libraries using pip install -r requirements.txt
     in a virtual environment in which the work will be carried out;
     
    Further in the Django project:
    - describe the models "product", "seller" and "sales". Sale model
      should record purchases made, that is, contain information about
      what product, in what quantity, at what price, when and by what seller
      was sold.
    - create a database with a superuser with a username and password admin.
    - Unload the superuser into the initial_data.json file using the command:

      python manage.py dumpdata auth.User> initial_data.json

      and place it in the fixtures folder of your application. 
      
1. In a django project, on the start (root) page, display a list of products
   and their prices. Implement in the following sequence:

   - create a test in the django project that checks if it returns
     page '/' and that the HTTP return code is 200;

   - run the test, make sure that it fails;

   - commit changes to SCM, push to the server;

   - create Employee, Item, Sale models (they will match
     tables in the database);

   - create a view for page '/' and connect it to urls.py.
     Create a basic template and a root page template;

   - use the annoying.render_to decorator,

   - get the test to pass;

   - commit changes to SCM;

   - [optional] rewrite the view for the root page and use the class-based view,
     check the test and commit the changes to the SCM

   - create fixture for models and connect them to the test;

   - add a test that checks the presence of text on the page
     with the name of the goods;

   - commit changes to SCM;

   - display a list of products on the page (modify the view and template);

   - make sure that the test completes successfully;

   - commit changes to SCM.
   
1. Create css and images folders and add static file handlers to urls.py.
    Connect basic css to the page (you can take, for example, from here:
    http://html5boilerplate.com/ or from here:
    http://twitter.github.com/bootstrap/

1. Add page title and title, title and color
    (indents, fonts, lines) list of goods.

1. Bring the look of all lists to one neat look.


1. Add a "Buy" button in the product line by which to translate
    user to a page with a description of the product, a field for entering its quantity,
    a drop-down list of sellers and a "Pay" button. At the push of a button
    add a record to the Sale table. Register quantity, cost,
    the seller and the date of purchase. After successfully saving the data, redirect
    to the root page. Remember to create tests before implementing the page.
    Commit created tests with commits.
    
1. Connect authorization. Add "Login" link at the top of the page.
    After logging in, show the username and the "Log out" link.
    
1. Add a page for viewing shopping information. Allow viewing
    only for authorized users. Display date, product name,
    seller's name and purchase amount. Sort in reverse chronological order.

1. Add a paginated shopping list. It is possible according to the django documentation,
    django-pagination can be used. Output 5 lines per page.
    
1. Install the coverage module via pip and get test coverage of the project:

      coverage run --include =. / ./manage.py test
      coverage report
      coverage html
      coverage erase
      rm -rf htmlcov

## TODO

1. Add a context processor adding the date and time the page was generated
     to the context of all application templates. Output it to footer.
     
1. Create a model that will store product price changes.
     Add a post_save signal handler that stores the date in it
     and time of change, reference to the "product" model and the new price. Add to
     a page where you can view a summary of the change history
     product prices. Allow viewing only for authorized users.
     
1. Write a test that verifies that price changes are saved correctly. 

## Quick Start

To get this project up and running locally on your computer:
   Recommended using a Python virtual environment.
1. Assuming you have Python setup, run the following commands (if you're on Windows you may use `py` or `py -3` instead of `python` to start Python):
   ```
   pip3 install -r requirements.txt
   python3 manage.py createsuperuser # Create a superuser
   python3 manage.py runserver
   ```
1. Open a browser to `http://127.0.0.1:8000/admin/` to open the admin site
1. Create a few test objects of each type.
1. Open tab to `http://127.0.0.1:8000` to see the main site, with your new objects.
