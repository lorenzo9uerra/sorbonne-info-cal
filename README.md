# sorbonne-info-cal

Simple python script to fetch the calendar of a course and save it as .ics file, so
it can be imported in various calendar clients.


### Usage
Just execute the script with:
```bash
python3 fetch_cal.py
```

It will ask to input the code of the course as seen in the website https://cal.ufr-info-p6.jussieu.fr/master/.\
To find the code of your course look at the side bar with the name of the
courses, a correct code should be something like `BIM/M1_BIM`, so take the name
of the master and, separated with a slash, append the name of the course.

That's it, the script will fetch the events and save them in an .ics file with
the name of the master and course you wanted.
