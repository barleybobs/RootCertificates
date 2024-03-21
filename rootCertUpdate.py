import requests, json

response = requests.get("https://ccadb.my.salesforce-sites.com/ccadb/AllIncludedRootCertsCSV")

if response.status_code == 200:
    results = []

    rows = response.text.split("\n")
    rows.pop(0)

    for row in rows:
        row = row[1:-1]
        cells = row.split("\",\"")

        results.append({
            "owner": cells[0],
            "certificate_name": cells[1],
            "sha256": cells[9],
            "web": {
                "apple": cells[2] == "Included" and "TLS Server" in cells[3],
                "chrome": cells[4] == "Included",
                "microsoft": cells[5] == "Included" and "Server Authentication" in cells[6],
                "mozilla": cells[7] == "Included" and "Websites" in cells[8],
            },
            "email": {
                "apple": cells[2] == "Included" and "Email" in cells[3],
                "microsoft": cells[5] == "Included" and "Secure Email" in cells[6],
                "mozilla": cells[7] == "Included" and "Email" in cells[8],
            }
        })

        with open("certificates.json", "w") as outfile:
            json.dump(results, outfile, indent=4)

