#language: hu

Jellemző: Létrehozunk egy új partnert, hozzá egy telephelyet és egy eszközt a partner id-val azonosítjuk

    Forgatókönyv: Adatok begyűjtése
        * Legyen egy partner a következő id-val "1234", akinek van egy random eszköze

    Forgatókönyv: Parnerrögzítése
        * Megjelent az oldal
        * Navigálás a bal menüben a következő menüpontra: "Partnerek"
        # Explicit wait
        * Megvárjuk, hogy eltűnjön a táblázatból a következő szöveget tartalmazó element: "No records to display"
        * Megjelent az ügyfelek grid
        * Letöltött partnerek rögzítése

    Forgatókönyv: Telephely rögzítése
        * Navigálás a bal menüben a következő menüpontra: "Telephelyek"
        * Megvárjuk, hogy eltűnjön a táblázatból a következő szöveget tartalmazó element: "No records to display"
        * Telephelyek rögzítése a következő azonosítóval rendelkező pernerhez: "1234"

    Forgatókönyv: Eszköz rögzítése
        * Navigálás a bal menüben a következő menüpontra: "Eszközök"
        * Megvárjuk, hogy eltűnjön a táblázatból a következő szöveget tartalmazó element: "No records to display"
        * Eszközök rögzítése a következő id-val rendelkező partnerhez: "1234"

    Forgatókönyv: Excel letöltése
        * Rögzített eszközök exportálása excelben

    Forgatókönyv: Telephely oldalon megjelenő eszköz adatok összevetése az excellel
        * Navigálás a bal menüben a következő menüpontra: "Telephelyek"
        * Megvárjuk, hogy eltűnjön a táblázatból a következő szöveget tartalmazó element: "No records to display"
        * A következő id-val rendelkező partner: "1234" eszköz adatinak összehasolítása az excelben lévő adatokkal

    Forgatókönyv: Szervíz státusz beállítása
        * Navigálás a bal menüben a következő menüpontra: "Eszközök"
        * Megvárjuk, hogy eltűnjön a táblázatból a következő szöveget tartalmazó element: "No records to display"
        * Egy eszköz szervízstátuszának módosítása

    Forgatókönyv: Telephelyek oldalon vizsgáljuk, hogy nem jelenik e meg a szervízben lévő eszköz
        * Navigálás a bal menüben a következő menüpontra: "Telephelyek"
        * Megvárjuk, hogy eltűnjön a táblázatból a következő szöveget tartalmazó element: "No records to display"
        * Egy telephely esetén nem jelennek meg a szervízben lévő eszközök
