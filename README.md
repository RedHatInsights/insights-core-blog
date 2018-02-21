# Insights Core Blog


This is the Insights Core Blog Space.

## Set up the environment  

##### Clone the Blog Repository Project<br/>
prompt> git clone git@github.com:RedHatInsights/insights-core-blog.git

##### Change to the insights-core-blog project directory  
Create a virtual environmant<br/>
prompt>virtualenv ./env

##### Source the virtual environment
prompt>source ./env/bin/activate


## Writing Blog Content

#### Header Information:

Title: Insights Core Blog
Date: <Date the blog entry was added> Example: 2018-02-01 00:00 <br/>
Tags: <Tags can be used to create links to defined Catagories> 
      Example: insights-core<br/>
Category: Definies the Category this blog entry falls under<br/>
+ If not defined Category will defined by the directory it the markdown
          is under


Slug: Must be unique across all blog entries. Example: insights-core-blog-1<br/>
Authors: -Authors name-

Summary: -Short Summary about the post-

Body:<br/>
My post ...

For more information on writing content:
[Pelican Docs "Writing Content"](http://docs.getpelican.com/en/3.6.3/content.html)

##### Adding Jupyter Notebook to Blog

Place the notebook .ipynb in the directory for the Category you are posting to.

For summary information about the notebook you can add a markup cell the beginning of
the notebook.   
Example:
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Summary:\n",
    "\n",
    "This is the \"debug_stats_report_template.ipynb\""
   ]
  },
  
Create a meta file that contains the proper header information for the blog 
entry.

The name of the file should be formated as follows

    "name of notebook file"-meta 

##### Publishing Content
Building and pushing content to the ph-pages branch of the blog repo is easy.
Simply run


## Publish the New Content

##### Run script to publish content
prompt>./push-gh-pages.sh

This will build, commit and push the html content, generated by Pelican, 
to the gh-pages branch in the insights-core-docs project
