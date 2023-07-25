import re
import csv


def extract(workdir):
    with open(f'{workdir}/blobs/file.html', 'r') as file:
        html = file.read()

    # Regex pattern to match a specific pattern in the HTML
    pattern = r"\+\d{1,4}\s\d{5}\s\d{5}"

    # Find all matches of the pattern in the HTML
    matches = re.findall(pattern, html, re.DOTALL)
    matches = list(set(matches))
    # print(matches)

    return matches


    with open(f'{workdir}/blobs/numbers.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        matches = list(set(matches))
        for match in matches:
            writer.writerow([match])