# Project Log Analysis
I've been hired onto a team working on a newspaper site. The user-facing newspaper site frontend itself, and the database behind it, were already built and running. I've been asked to build an internal reporting tool that will use information from the database to discover what kind of articles the site's readers like.

The database contains newspaper articles, as well as the web server log for the site. The log has a database row for each time a reader loaded a web page. Using that information, my code will answer questions about the site's user activity.

The program I write in this project will run from the command line. It won't take any input from the user. Instead, it will connect to that database, use SQL queries to analyze the log data, and print out the answers to some questions.

## Why This Project?

In this project, I will stretch my SQL database skills. I will get practice interacting with a live database both from the command line and from my code. I will explore a large database with over a million rows. And I will build and refine complex queries and use them to draw business conclusions from data.

## Report Generation

Building an informative summary from logs is a real task that comes up very often in software engineering. For instance, at Udacity they collect logs to help measure student progress and the success of their courses. The reporting tools they use to analyze those logs involve hundreds of lines of SQL.

## Database as shared resource

In this project, you'll work with data that could have come from a real-world web application, with fields representing information that a web server would record, such as HTTP status codes and URL paths. The web server and the reporting tool both connect to the same database, allowing information to flow from the web server into the report.

## Requirements

[Python 3](https://www.python.org/download/releases/3.0/) - The code uses ver 3.6.4\
[Vagrant](https://www.vagrantup.com/) - A virtual environment builder and manager\
[VirtualBox](https://www.virtualbox.org/) - An open source virtualiztion product.\
[Git](https://git-scm.com/) - An open source version control system


##  How to access the project?

Follow the steps below to access the code of this project:

 1. If you don't already have the latest version of python download it from the link in requirements.
 2. Download and install Vagrant and VirtualBox.
 4. Clone this repository.
 5. Download the [newsdata zip file](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip) database.
 6. Navigate to into the vagrant folder.
 7. Launch the virtual machine with`vagrant up`
 8. Once Vagrant installs necessary files use `vagrant ssh` to continue.
 9. The command line will now start with vagrant. Then cd into the /vagrant folder.
 10.  To load the database type `psql -d news -f newsdata.sql`
 12. To run the database type `psql -d news`
 13. Use command `python news_db.py.py` to run the python program that fetches query results.
