# Arxiv.org Computational Physics Paper Autodownloader
This app automates the tedious downloading process from the ArXiv.org.



## Background 
As it is a common practice for all physicists to read most up-to-date papers on ArXiv, I find it tedious to go through different pages and to download the papers and then to rename the paper (just in case later I totally forgot what this pdf is about), and to organize the file folders. Therefore I come up with this idea to automate the above 4 steps using Selenium and Python. 



## The Flow
(1)The app will first create a folder with the name specified as today's date.
(2)Then it will go through the first page of computational physics section and get all the download links
(3)At the same time, it will also get all the paper names associated with each link.
(4)use chromewebdriver to download given the links, and then change the name of each file to the title of the paper. The default directory is set in the chrome options.
(5)once everything is done, I move the whole folder to my document under physics papers.
and voila!

## Note
This is a good practice for me with Selenium, and definitely there are lots of other options to explore (for example, to upload the files to the cloud, to gather papers from more than one source, such as PRL, PRB, SCIENCE, or Nature). I will definitely think about future revisions.

