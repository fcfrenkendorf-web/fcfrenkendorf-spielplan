import urllib.request
import urllib.error

URL = (
    "https://matchcenter.fvnws.ch/"
    "default.aspx?v=494&oid=8&lng=1&a=vs"
)

try:
    request = urllib.request.Request(
        URL,
        headers={
            "User-Agent": "FCFrenkendorf-Spielplan/1.0"
        }
    )

    with urllib.request.urlopen(
        request, timeout=20
    ) as response:
        html = response.read().decode(
            "utf-8", errors="replace"
        )

    print("Verbindung erfolgreich")
    print("HTML-Zeichen:", len(html))
    print(
        "Spielplanstruktur gefunden:",
        "spTitel" in html
        and "row spiel" in html
    )

except (urllib.error.URLError, TimeoutError) as e:
    print("Verbindung fehlgeschlagen:", e)
    raise
