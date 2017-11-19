# IVLE Announcements

## IVLE: CG3002: CG3002: Procedure for Claims
`by: Sangit Sasidhar, 16-Nov-2017 01:55 PM`
Dear All,

You need to submit the claims form (RFP) for each group alongwith the list of expenses excel sheet and the receipts.  Please note the following points:  
You need to dismantle your dancing prototypes and return the components within a week of your final dance!! (23rd November for Thursday's Group and 24th November for Friday's Group)  
The receipts need to be pasted on A4 size paper. I have attached a sample on how to paste the receipts.  
The receipts need to be verified by the lab officers with the corresponding purchases when you return the components.  
Ensure that you fill up the List of expenses excel sheet with all the purchase details.  
Have an awesome dance-off!!!  

Cheers  
CG3002 Teaching Team  

## Final Test Schedule
`by: Peh Li Shiuan, 14-Nov-2017 10:25 AM`
Hi all,

 This is the time and order the final test will be carried out this Thursday/Friday. I generated it randomly in python :P. All members of the group must be present.

Nov 16 Thursday  
2:20pm Group 11  
2:40pm Group 6  
3pm Group 9  
3:20pm Group 1  
3:40pm Group 7  
4pm Group 2  
4:20pm Group 8  
4:40pm Group 4  
 
Nov 17 Friday  
2:20pm Group 12  
2:40pm Group 5  
3pm Group 10  
3:20pm Group 3  
3:40pm Group 13  

    See you all at the final dance off! :)

Cheers,  
Li Shiuan  
p/s For the final report submission due Sunday 2359, please also submit your final code (compressed .tar ideally, or github link)

## IVLE: CG3002: CG3002: Logout Move
`by: Sangit Sasidhar, 13-Nov-2017 11:16 PM`  
Dear All,

For the final evaluation the server will stop displaying after the 40th move. You can send the logout message to the server in one of two ways:

1. You can have an internal count to 40 and send the logout message to the server after the count reaches 40 or
2. Once you send the 40th move you can do your "logout" move and send the logout message to the server (Once the server receives the 40th move you can dance the logout move).

Regards,
CG3002 Teaching Team

## New Files in Module CG3002 
`by: Peh Li Shiuan, 08-Nov-2017 08:54 PM`  
New Files :

Folder Name : Handouts

Filename: final_eval_server.py
Description: final_eval_server.py: This is the script we will use for the final test next week. I slightly modified the earlier sample_eval_server.py: 1) Fair choice of 40 moves (out of all 10 actions) so each action will be tested 4 times, at random order. 2) Server will wait for "logout" message from you after 40 moves Please test your system with this and let us know if there are problems!

## Final evaluation details
`by: Peh Li Shiuan, 06-Nov-2017 05:01 PM`  
Hi all,

We will be doing the final evaluation next week during lab, November 16 or 17th, and your final report will be due that Sunday November 19th, 2359hrs. This final evaluation will take up 30% of your grade, and your final report will take up 10%, so together they take up the remaining 40% of your grade.

Final evaluation: We will randomly select one of your team members to be the dancer (all must be present), as well as one of the teaching staff to be the dancer. Each dancer will make 40 moves selected randomly out of all 10 moves. We will attach a USB power meter to your system for validating your power numbers. At the end of the sequence, the dancer should make a goodbye move and the system should detect that and send the "logout" message to the server to end the session.

 Happy dancing and training for the final evaluation! :)

Cheers,
Li Shiuan

## 5 moves evaluation tomorrow and Friday!
`by: Peh Li Shiuan, 01-Nov-2017 08:09 PM`  
Hi all,

Tomorrow is the big day for the Thursday lab groups, and Friday for the Friday lab groups! All team members must be there for the evaluation.

If you have not yet done the TEAMMATES peer survey, please do so!

See you,
Li Shiuan

## 1 more week to evaluation with 5 moves!
`by: Peh Li Shiuan, 25-Oct-2017 03:51 PM`  
Hi all,

   I hope your system is now integrated and you are busy dancing and improving it! :) Next week November 2nd and 3rd will be when you will be tested during your respective lab session. We will randomly pick one of your team members as the dancer. The sample_eval_server.py that is provided on IVLE will be run on our laptop, and we will let you know the WiFi hotspot and IP address of the server to connect to beforehand.

   Today, you will also be getting an email from TEAMMATES asking you to complete a peer survey. As CG3002 is a group project, it has been a tradition of the class to have such a peer survey to provide feedback on team dynamics and contribution. The survey will only take 5 minutes of your time, and I will give extra credit to all respondents.

Cheers,
Li Shiuan

## New evaluation server script
`by: Peh Li Shiuan, 12-Oct-2017 03:39 PM`  
Hi all,
 
   Here’s the evaluation server script we will use to test your system during week 11, for the first five moves. It is just slightly modified from the sample_auth_server.py that you were using to test the wireless comms.

  The semantics of the server is as follows:
 
python3 sample_eval_server IP address port groupID
 
   It will wait a minute before generating a random move (out of the 5 moves), to give everyone time to enter secret key, connect, and get ready to dance.
 
   The server will generate 20 moves, and for each move that it generates, it will wait for a detected action from your system. Once it receives any action, it will generate another move.
 
   There is now a larger display of the dance move to make it easier for you all to see while dancing :).
 
Cheers,
Li Shiuan

## IVLE: CG3002: Arrrangement with CG3002 software teaching duties between Oct 20 - 28, 2017
`by: Wang Ye, 01-Oct-2017 10:50 PM`  
Dear All,
 
Due to ISMIR2017 international conference (https://ismir2017.smcnus.org/), Boyd Anderson, Dania Murad and I will be in Suzhou as conference organizers between Oct 20-28, 2017. Because of this, we have the following arrangements regarding CG3002 teaching duties for the software part during that period.
 
Zhao Na will be attending all labs on Oct 20, 26 and 27. Dania Murad and I will be attending all labs on Oct 19, Nov 9 and 10. Please use the IVLE forum to ask questions as much as possible so that we can try to answer your questions remotely.
 
--WY

## IVLE: CG3002: Week 7 Software Testing Guideline
`by: Wang Ye, 01-Oct-2017 10:31 PM`  
Dear All,
 
The following are the software testing guidelines:
 
You are expected to run machine learning libraries with Raspberry Pi.
 
1. Collect data for all the activities with your own sensors.
2. Train a machine learning model with your data on the Raspberry Pi. Keep the name of your python code which trains the model as 'learning.py' for consistency.
3. We will be evaluating the following metrics as last time:
Classification accuracy
Confusion matrix
While evaluation, you will be asked to run your machine learning code 'learning.py' on the Raspberry Pi. The classification accuracy and confusion matrix should be written in a file, saved in Pi. We will require you to show us these files and evaluate your model accuracy accordingly.
 
Good luck!
 
CG3002 Teaching Team

## IVLE: CG3002: CG3002: Week 7 Hardware Testing Guidelines
`by: Sangit Sasidhar, 29-Sep-2017 04:15 PM`  
Dear All,

Hope you all are hard at work on your respective hardware, software and firmware sections.
The first prototype evaluation is three separate tests on software, hardware and firmware.

The following are the hardware testing guidelines:

1. All the hardware (including all the sensors) has to be integrated for testing
2. The hardware system should be able to do the following :
Measure the power consumed by your system. It should include both voltage and current measuremnt circuits.
All Sensors should be working and you should be able to mount them on yourself and do one/two dance steps and show a respective change in the values.
3. The user can provide the  results either through the hardware or by connecting a serial out to his/her laptop.

Good luck all :)

CG3002 Teaching Team

## Comms: New server_auth.py uploaded
`by: Peh Li Shiuan, 14-Sep-2017 05:45 PM`  
Hi all,

Thanks to Paul Tan who tried out our comms server and pointed out that the message format can be simplified! :) So an updated version of server_auth.py is now on IVLE -- please download this new version! It is much simpler and less confusing for you when coding up your wireless comms client. The other files sample_auth_server.py and performanceMetrics.py are unchanged.

Have fun! :)

Cheers,
Li Shiuan

## Comms evaluation guidelines uploaded; Feedback at this week's labs
`by: Peh Li Shiuan, 11-Sep-2017 11:02 AM`  
Hi all,

 I've just uploaded the Comms evaluation guidelines, and linked them to Week 7's lesson plan. Sangit will be uploading the hardware test guidelines. The individual subcomponent (Hw, Comms, Sw) tests are in Week 7, after the recess, during the labs.

 We will be giving you feedback on your design report at this week's labs. See you...

Cheers,
Li Shiuan

## IVLE: CG3002: Datasets for machine learning
`by: Wang Ye, 07-Sep-2017 10:56 PM`  
Dear all,

As requested by some of our students, here are two links to repository for machine learning.
 
1. http://archive.ics.uci.edu/ml/datasets.html
            You can find a proper pseudo dataset by filtering with different criteria (e.g. task; instance; attribute.) or searching with certain keywords (e.g. sensor; action recognition). 
            Example dataset: 
            Smartphone-Based Recognition of Human Activities and Postural Transitions Data Set (https://archive.ics.uci.edu/ml/datasets/Smartphone-Based+Recognition+of+Human+Activities+and+Postural+Transitions)
 
2. https://www.kaggle.com/datasets
            Example dataset:
            Run or walk [A dataset containing labeled sensor data from accelerometer and gyroscope] (https://www.kaggle.com/vmalyi/run-or-walk)

Such datasets will be useful before your sensor system can supply you with data.

​--WANG Ye

## Reminder: Design report due this Friday (tomorrow! Sep 8th) 11:59pm
`by: Peh Li Shiuan, 07-Sep-2017 02:26 PM`  
Hi all,

   Just a reminder that the design report is due tomorrow, Friday Sep 8th, at 11:59pm. Please submit it through IVLE. Note that this is an automated submission deadline, so please don't drag till the last minute :)

Cheers,
Li Shiuan

## Thursday labs start tomorrow, Aug 31st, 2-5pm @ DSA lab
`by: Peh Li Shiuan, 30-Aug-2017 09:18 AM`  
Just a reminder that Thursdays lab sessions will start tomorrow 2-5pm at DSA lab. You will be issued the components, and Sangit will be walking through the components at lab. See you!

## IVLE: CG3002: CG3002: Groupings
`by: Sangit Sasidhar, 29-Aug-2017 02:14 PM`  
Dear All,

All your groupings have been finalised. You can check them out in IVLE. 

CG3002 Teaching Team

## Friday labs start tomorrow 2pm (DSA lab)
`by: Peh Li Shiuan, 24-Aug-2017 05:14 PM`  
Just a reminder that Friday lab sessions will start tomorrow at DSA Lab. You will be receiving your box of components and Sangit will be giving a walk through of these components.

Cheers,  
Li Shiuan
