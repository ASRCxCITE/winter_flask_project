# winter_flask_project

Project Description:
Part One:
You are going to create a very simple and straightforward webpage that will be phase one of projects to come next semester. It will involve running a backend server using flask (instructions below), creating a mongoDB database with any WRF data that we have given you access to (recall https://github.com/ASRCxCITE/mongo_tutorial), creating any kind of plots and serving them on the front end (recall workshop https://github.com/ASRCxCITE/Tutorials). You can be creative and make it look nice or do the minimal and just show a single plot. Once you are done you will push your project to github. The readme must contain the URL so Kara and myself can access the front end and see the work you have done (example URL will look like http://coeml.asrc.albany.edu:<input your notebook port>/)
Part Two:
In part two, you are to make at least 1 interactive plot and make several pages with a navigation. EX: create multiple pages that are linked from your main page leading to separate plots per page. 


Running flask server:
We have created a starting point to run a backend flask server. You can build off this original or make your own. This file should eventually be moved into your project folder.
Open up terminal in jupyter lab and write ls, should see app.py.
$ python app.py
Server should start
Access webpage from http://169.226.181.104:<input your flask port>/ or http://coeml.asrc.albany.edu:<input your flask port>/
Should see ‘Flask working in Docker container!’
Go to app.py change something in “Flask working in Docker container!” and save

@app.route(“/”) specifies the starting point, to add more routes you can add to the file like so:
@app.route("/test")
def salvador():
    return "Hello, this is a new route"

Save the file and now you can access that new route with:
http://coeml.asrc.albany.edu:<input your flask port>/test

Once everything is working up to this point, create a project folder, move app.py into it and follow this tutorial from HTML, CSS, and Virtual Environments to but not including Moving Forward with Flask and virtualenv
https://www.freecodecamp.org/news/how-to-build-a-web-application-using-flask-and-deploy-it-to-the-cloud-3551c985e492/

It will show you how to add css, multiple pages and link everything.

Once you have completed part 1 show Kara and/or Arnold for feedback before proceeding to part two.

Do not be intimidated, this seems like a lot but we have done all of these parts already. This is a very small project that could be done in a few hours if you put your mind to it. We expect you to forget steps and run into problems. Don't forget to reference the work we have on github and if you start getting errors, google is your best friend :) Happy Holidays!
