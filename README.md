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
courses:\
![image](https://user-images.githubusercontent.com/43646324/204301365-0907426b-c7cc-4c24-bc8a-b2d54819d472.png)\
a correct code should be something like `BIM/M1_BIM`, so take the name
of the master and, separated with a slash, append the name of the course.

That's it, the script will fetch the events and save them in an .ics file with
the name you wanted.
