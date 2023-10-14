import requests
from xml.etree import cElementTree as ET

course_list = [
    'ANDROIDE/M1_ANDROIDE',
    'ANDROIDE/M2_ANDROIDE',
    'BIM/M1_BIM',
    'BIM/M2_BIM',
    'DAC/M1_DAC',
    'DAC/M2_DAC',
    'IMA/M1_IMA',
    'IMA/M2_IMA',
    'IQ/M1_IQ',
    'IQ/M2_IQ',
    'MasterInfo/calendar', 'MasterInfo/M1',
    'MasterInfo/M2',
    'RES/M1_RES',
    'RES/M1_RES-EIT-Digital',
    'RES/M1_RES-ITECIA',
    'RES/M1_RES-ITESCIA',
    'RES/M2_RES',
    'RES/M2_RES-EIT-Digital',
    'RES/M2_RES-INSTA',
    'RES/M2_RES-ITECIA',
    'RES/M2_RES-ITESCIA',
    'SAR/M1_SAR',
    'SAR/M2_SAR',
    'SESI/M1_SESI',
    'SESI/M2_SESI',
    'SFPN/M1_SFPN',
    'SFPN/M1_SFPN-AFTI',
    'SFPN/M2_SFPN',
    'SFPN/M2_SFPN-AFTI',
    'STL/M1_STL',
    'STL/M2_STL',
    'STL/M2_STL-INSTA'
    ]

def ask_cc():
    i = 1
    print("Code of the course to be fetched: ")
    for code in course_list:
        print(f"{i}: {code}")
        i+=1
    nlist = int(input("Choose the number of the calendar to be fetched: "))
    if nlist >= 1 and nlist <= len(course_list):
        return course_list[nlist]
    else:
        print("The calendar specified is not present in the list")
        return ""

def fetch_cal(course_code):
    headers = {
            "Content-Type": "text/xml; charset=utf-8",
            "Authorization": "Basic c3R1ZGVudC5tYXN0ZXI6Z3Vlc3Q=",
            "X-client": "CalDavZAP 0.13.1 (Inf-IT CalDAV Web Client)",
            "Depth": "2",
            "X-Requested-With": "XMLHttpRequest",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin"
            }
    url = f"https://cal.ufr-info-p6.jussieu.fr/caldav.php/{course_code}/"
    data = "<?xml version=\"1.0\" encoding=\"UTF-8\"?><L:calendar-query xmlns:L=\"urn:ietf:params:xml:ns:caldav\"><D:prop xmlns:D=\"DAV:\"><D:getcontenttype/><D:getetag/><L:calendar-data/></D:prop><L:filter><L:comp-filter name=\"VCALENDAR\"><L:comp-filter name=\"VEVENT\"><L:time-range start=\"20230624T000000Z\" end=\"20240215T000000Z\"/></L:comp-filter></L:comp-filter></L:filter></L:calendar-query>"

    return requests.request(method="REPORT",url=url,headers=headers, data=data)

def save_ics_from_response(response, filename):
    root = ET.fromstring(response.text)

    icsfile = open(filename, "wt")
    for el in root.iter('{urn:ietf:params:xml:ns:caldav}calendar-data'):
        if el.text:
            icsfile.write(el.text)
    icsfile.close()
    icsfile = open(filename, "rt")

    # purge the file: remove from BEGIN:VCALENDAR to BEGIN:VEVENT included and the END:VCALENDAR referred except the first time
    # Split the input data into separate VCALENDAR sections
    old_cal = icsfile.read().strip().split("\n")
    icsfile.close()
    
    # remove "" from the list
    old_cal = [x for x in old_cal if x]

    # first section is the header, keep it
    header= []
    for x in old_cal:
        if x=="BEGIN:VEVENT":
            break
        else:
            header.append(x)

    # remove everything until the first BEGIN:VEVENT
    events=[]
    for x in old_cal:
        if not x in header and x != "END:VCALENDAR":
            events.append(x)
        else:
            continue

    new_cal = header + events + ["END:VCALENDAR"]

    # Write the combined content to a new .ics file
    with open(filename, "w") as old_cal:
        old_cal.write("\n".join(new_cal))
        old_cal.close()

course_code = ask_cc()
response = fetch_cal(course_code)

if response.ok:
    save_ics_from_response(response, course_code.replace("/", "-")+".ics")
    print("DONE :)")
else:
    print("The specified code of the course is not valid, check again")