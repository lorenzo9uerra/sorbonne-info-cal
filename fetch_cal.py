import requests
from xml.etree import cElementTree as ET

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
    data = "<?xml version=\"1.0\" encoding=\"UTF-8\"?><L:calendar-query xmlns:L=\"urn:ietf:params:xml:ns:caldav\"><D:prop xmlns:D=\"DAV:\"><D:getcontenttype/><D:getetag/><L:calendar-data/></D:prop><L:filter><L:comp-filter name=\"VCALENDAR\"><L:comp-filter name=\"VEVENT\"><L:time-range start=\"20220725T000000Z\" end=\"20230315T000000Z\"/></L:comp-filter></L:comp-filter></L:filter></L:calendar-query>"

    return requests.request(method="REPORT",url=url,headers=headers, data=data)

def save_ics_from_response(response, filename):
    root = ET.fromstring(response.text)

    icsfile = open(filename, "wt")
    for el in root.iter('{urn:ietf:params:xml:ns:caldav}calendar-data'):
        if el.text:
            icsfile.write(el.text)
    icsfile.close()

course_code = input("Code of the course to be fetched [RES/M2_RES]: ")
filename = input("Calendar filename [calendar.ics]: ")
if not course_code:
    course_code = "RES/M2_RES"
if not filename:
    filename = "calendar.ics"

response = fetch_cal(course_code)
save_ics_from_response(response, filename)
