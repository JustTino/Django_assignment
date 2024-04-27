# Shopping with Django
A shopping site done in Django to show the basics of an ecommerce site. This is a remake of an older application, which tried to do too much. This one focuses on the shopping part, with support for testing.

After you clone or download the repository use these commands to set things up:

    pyenv local 3.10.7 # this sets the local version of python to 3.10.7
    python3 -m venv .venv # this creates the virtual environment for you
    source .venv/bin/activate # this activates the virtual environment
    pip install --upgrade pip [ this is optional]  # this installs pip, and upgrades it if required.
    pip install django
    pip install faker
    python3 manage.py migrate

This app uses Faker to generate customer and product details in the 'shop/management/commands/populate_tables.py' file. Go to https://faker.readthedocs.io/en/stable/providers.html and look through the options for Standard Providers to see if you want to change any details in values used.

You should now be able to populate the tables with the command:

        python3 manage.py populate_tables

Then you can start the server to see it running. 

You will need to create a superuser as well if you want to work with the admin features. You can do that with the command:

        python3 manage.py createsuperuser

Otherwise each customer created is also a user with a default password set in the management/commands/populate_tables.py file. 

You can launch django with the usual command:

        python3 manage.py runserver

With the server running, you can navigate around both parts of the application:
1. Go around the genearl website and notice what's working, what's bare-bones, and other issues. This is not finished, but a work in progress to illustrate how you might build a shopping application. 
2. Go to localhost:8000/admin and login with your superuser credentials. There you'll see the Django admin interface. From here you can also add products, and customers. The models listed here are specified in the shop/admin.py file.

### The Payment System 
This uses sessions to put items into a basket, which can be seen via 'Basket' link, and then shifted to 'Purchase' with the user details. This is based in part on the example at https://github.com/PacktPublishing/Django-3-by-Example/tree/master/Chapter08 from a book of the same name.

A key for the basket is set in settings.py, which will be unique for each shopper.
A person needs an account before they can see the payment page.


### There is still more to do with this
This still needs more work. There is currently no way to set up admin users, other than using the admin system to change users to 'staff', who could then see a dashboard of orders, and customers. The current dashboard is a placeholder, which only 'is_staff' can see. You can look at this other repo for ideas of how to add visuals to it https://github.com/scharlau/polar_bears_django_visuals based on what you find interesting.

A better version would improve a range of things in this application. There are many places that need improvement.
For example, you could only allow staff to remove and edit the products too. Only staff should be able to view customers and orders too, plus there are a number of authentication issues to put in place for view methods.
Ideally, there should be more tests too. It would've made developing these extra parts easier if tests showed where the pages 'broke' as parts were added.
Oh, and the stuff from faker sometimes adds extra characters. Those need to be cleaned up.

##  Doing the Work
Work through the three rounds with a partner, or on your own, depending upon your circumstances. Each round should be twelve minutes, followed by a discussion of where you are and what has been working, as well as, what you're working on next.

You may want to refer to the shop/models.py file to understand the database schema before you get started. Some of you might even want to diagram the schema. 

You might also want to spend a few minutes at the start of each round planning what you might want to do.

You'll see that this version works with the objects in the shop/models.py file to manipulate the data we display on the page. This means we've mostly abstracted away the SQL, and are working with objects for our queries and the dislay of results.

There are some forms here for the products. These add the basic CRUD methods (create, read, update and delete). You could add similar ones for other objects.

### Testing 
There are basic tests to confirm the site works for Products, but more should be added to confirm all models, and that the basket and purchase work correctly.

## The Exercises

1. Round one should be fixing the order_detail.html page to show names of items and customers, who placed the order. If you have time, then you can also fix the customer_details.html page to show the customer's orders, and let them click through to the order_details.html page, which also needs more details added so customers/staff can see items.
2. Round two should be implementing the 'dashboard' page to show the total value of orders placed by customers.
3. Round three is adding it so that customers can see their own orders.

