# Django Package Template
Template for creating packages. 


# Instructions
1. Click `Use this Template` on GitHub
2. Fill out your project name accordingly
3. Clone your repository
4. Run `initalize.py`

# Important: Celery
If working with Celery, you need to do three things. 
1. Uncomment line 1 in `test/app/__init__.py`
2. Uncomment line 4 in `test/app/settings.py`
3. `cp test/app/celery.py.example test/app/celery.py`

# Additional Recommendations
1. Rewrite this `README.md`
2. Generate a documentation folder `sphinx quickstart`
3. Enable Travis on Github and `mv .travis.yml.example .travis.yml` (don't forget to change `django_package_template`)
4. Travis will test your application, given that you have proper Django tests
5. Add required packages in `setup.py`

# Clean Up
1. Delete `initailize.py`
