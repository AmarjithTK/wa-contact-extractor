import re
import csv


def extract(workdir):
    with open(f'{workdir}/blobs/file.html', 'r') as file:
        html = file.read()

    # Regex pattern to match a specific pattern in the HTML
    pattern = r"\+\d{1,4}\s\d{5}\s\d{5}"

    # Find all matches of the pattern in the HTML
    matches = re.findall(pattern, html, re.DOTALL)
    stripped = strip_and_filter(matches)
    
    with open(f'{workdir}/blobs/numbers.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        matches = list(set(stripped))
        for match in matches:
            writer.writerow([match])    
    # print(matches)
    check_duplicates(list(set(stripped)))


    return stripped


def check_duplicates(arr):
    unique_strings = []
    for s in arr:
        if s in unique_strings:
            print("found")
        else:
            unique_strings.append(s)


def strip_and_filter(arr):
    new_arr = []
    for s in arr:
        stripped = s.replace(" ", "")
        if stripped not in new_arr:
            new_arr.append(stripped)
            
    return new_arr
