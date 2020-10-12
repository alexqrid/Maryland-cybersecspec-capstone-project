# Simple messaging system
This is a simple project for Maryland University's Cybersecurity specialization at [Coursera](https://coursera.org).  
# Requirements  
Requirements
All the functionality outlined in the interface details must be accessible over an http connection with HTML-based web pages. You cannot embed an applet, servlet, flash, or other application in a web page to serve as this project.

## Access
If you implement this on your own server, you should provide the URL of the home page.  

If you provide a local repository, it must meet the following requirements.

• An evaluator can download an archive that contains all the necessary libraries and code.

• An automated system will invoke make in the build directory of your submission.

• make must function without internet connectivity and it must return within ten minutes.

• Evaluators should not require any libraries or installation on their own machines. All necessary libraries must be included in your archive.

• Your software must be actually built, through initiation of make, from source (not including libraries you might use). Submitting binaries (only) is not acceptable.

make should produce an executable file that can be launched to run the server. Your server must be accessible through any web browser on the machine where the server is running at http://localhost:5813

## Functionality
### Interface
The user interface is the way users and evaluators will interact with your messaging system. You should think carefully about the usability of the interface, particularly with respect to the security elements.

It must include the following pages:

• index.html, the default home page, which should have links to “Register” or “Log in”

• Registration page where users register for the system. You can design your own process. For example, you may have users provide all their information, including a username and password, up front or you can create a multi-step registration process with email verification, etc. You can use whatever type of password / authentication system you like. After successfully registering, users should be taken to the login page.

• Login page, where users authenticate. If a user does not remember their login information, there should be some way to reset it (use whatever you like – email, text, security questions, etc.) After successfully authenticating, they should be taken to their inbox.

• Inbox, where users can see messages sent to them. You can display this however you like – clickable with previews like email, a long running list of messages similar to the Twitter newsfeed, or anything else you like. The requirements are simply that the user can see new messages sent to them. You can decide how you want to manage message storage after they have been read the first time.

• Send message page allows users to send messages to other users. One user should be able to address a message to another by username.

You are free to create other pages as you see fit.

### Message Storage
You may store your message data anyway you like. Use flat files, databases, etc. However, you must encrypt the data before you store it. You can use whatever encryption mechanism you like.

Evaluators should be able to dump your database and view the contents. This should be accessible at http://example.com/YOUR HOME DIRECTORY/dbdump if you are running on your own server or http://localhost:5813/dbdump if you are providing a local server. Dump the data as plain text files using whatever formatting you like. If the data is encrypted, you can dump it as encrypted. If there are binaries, use whatever plain-text export functionality your database has. The goal here is for people to see how your data is stored, not to review every entry in the database.

Rules
• Do not obfuscate your code

• Teams must do their own work and not share solutions with others.

### Scoring
See the evaluation rubric for scoring awarded for each element of the core functionality and for usability analysis.

A bug is defined as incorrect behavior by a program. In this case, a bug must be a behavior that violates one of the functionality or access requirements described above. A vulnerability is defined as a security exploit in a program. Again, these should be security exploits related to the functionality outlined above; it could be allowing inappropriate access to messages or accounts. A vulnerability in, say, a javascript library you use would not count against you in this capstone. A crash is defined as unexpected program termination. We are adopting a strict definition of a crash for the purposes of the capstone. It must be one that causes the app to abort or otherwise completely stop working (requiring either a manual or automatic restart).

For every unique bug found against your submission during the Break-it phase, you will lose 5 points. For every unique bug found against your submission that leads to a crash, you will lose 10 points. For every unique vulnerability found during the Break-it phase, you will lose 15 points.

Usability will be scored as the sum of the ratings your evaluators provide on their analysis of your authentication system. See the rubric for the exact elements they will look for. Each team will rate the usability (not the security) of your user-facing authentication system on the following scales:

|  worse  | points | better |  
| ---- | ---- | ----|  
| difficult |	1 2 3 4 5 6 7 8 9	| easy |  
| frustrating	| 1 2 3 4 5 6 7 8 9 |	satisfying |  
| terrible |	1 2 3 4 5 6 7 8 9 |	wonderful |  
| confusing |	1 2 3 4 5 6 7 8 9 |	very clear |  
| slow |	1 2 3 4 5 6 7 8 9 |	fast |  


## Basic Functionality
Scoring awards the project’s team 10 points for every Yes and 0 points for every No. 150 points total

* Code repository is downloadable ?
* Database dump from /dbdump is successful ?
* Are messages in the database encrypted?
* Can you access the website ?
* Interface elements

__To test this, please create two accounts and send a message from each account to the other. Answer Yes/No to each prompt.__

* Is there an index.html page that includes options (or links to pages) to register and to login
* Registration page present
* Registration page functional
* Login page present
* Login works after registration
* Page to see messages sent to the user is present
* Messages to the user are actually shown on the messages page
* Page to send messages is present
* Messages are successfully sent to the recipient
## Security Usability Analysis

Score for the project team is 2 X the sum of ratings on the final question’s scale. 50 points total. Also answer the following descriptive questions.

* What are the password requirements?
* Could a user who just wants to access the system as quickly / easily as possible circumvent the security measures with insecure behavior (e.g. a “12345” password, etc.)?  

If there is password-based authentication…
* How easy is it for a person to memorize this password? Is it easier or harder than a standard 8-character password that requires upper case, lower case, numbers, and punctuation? Justify your answer with principles of memory such as the 7+/-2 rule, chunking, etc.
* Please indicate More Usable, Equally Usable, Less Usable and provide a reason.  

If there is no username-password authentication, but something else in its place…
* How usable is this alternative to a standard 8-character password? Justify with principles of usability: speed, efficiency, memorability, learnability, user preference. Please indicate More Usable, Equally Usable, Less Usable and provide a reason.
  
If there are authentication measures beyond the initial authentication step…

* What are the additional steps?
* How long to the additional steps take to complete (time it)?
* How usable are the additional steps? Justify with principles of usability: speed, efficiency, memorability, learnability, user preference.
## Rate the user experience with the authentication mechanism on this site on the following scale. Note that you are not rating how secure it is, only the experience for the user:

|  worse  | points | better |  
| ---- | ---- | ----|  
|very difficult	| 1 2 3 4 5	|very easy|
|very frustrating	| 1 2 3 4 5|	very satisfying|
|really terrible |	1 2 3 4 5|	really wonderful|
|very confusing |	1 2 3 4 5	|very clear|
|very slow	| 1 2 3 4 5	| very fast|


## Break It
Scoring for the project’s team: For every unique bug found against your submission during the Break-it phase, you will lose 5 points. For every unique bug found against your submission that leads to a crash, you will lose 10 points. For every unique vulnerability found during the Break-it phase, you will lose 15 points.

Recall the following definitions:  

A bug is defined as incorrect behavior by a program, while a vulnerability is defined as a security exploit in a program. A crash is defined as unexpected program termination due to violations of memory safety.  

For each bug you find that other teams can verify, you earn 5 points.  

For each bug that leads to a crash that you find that other teams can verify, you earn 10 points.  

For each security vulnerability you find that other teams can verify, you earn 15 points.  

Document each unique way you break the system. Provide clear step-by-step instructions on how to detect the bug, cause the crash, or exploit the vulnerability. You will not receive any points if other teams cannot replicate your results.  
  
A bug or vulnerability is unique if it uses a different problem in the system. For example, if an SQL injection attack can let you change a message and also read a message or delete a message, that counts only as one vulnerability: the system is not robust against SQL injection attacks. It would not count as three vulnerabilities (one for changing, one for deleting, one for reading).  

Number each problem, beginning with 1. Label each as “bug”, “crash”, or “vulnerability”. Thoroughly document how another team could replicate your finding.  
