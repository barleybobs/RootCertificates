# Root Certificate Database

This repository contains a json file containing an array of root certificates and whether they are trusted by various root stores. It also contains the owner, certificate, and the SHA-256 hash of the root certificate.

All of this information is gathered from the [Common CA Database](https://www.ccadb.org/resources).

It splits trust into whether they are trusted for websites and email.

> [!NOTE]
> This repository is automatically updated by a GitHub Action daily at midnight ([UTC](https://time.is/UTC)).

## Currently supported Root Stores
 - Apple
 - Google (Chrome)
 - Microsoft
 - Mozilla

## Certificate format

```json
{
    "owner": "A-Trust",
    "certificate_name": "A-Trust-Root-07",
    "sha256": "8AC552AD577E37AD2C6808D72AA331D6A96B4B3FEBFF34CE9BC0578E08055EC3",
    "web": {
        "apple": false,
        "chrome": false,
        "microsoft": true,
        "mozilla": false
    },
    "email": {
        "apple": false,
        "microsoft": false,
        "mozilla": false
    }
},
```