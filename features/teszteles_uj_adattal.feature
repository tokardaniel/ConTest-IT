#language: hu

Jellemző: Létrehozunk egy új partnert, hozzá egy telephelyet és egy eszközt

    Forgatókönyv: Adatok begyűjtése
        * "2" db új adat betöltése API-n keresztül

    Forgatókönyv: Parnerek rögzítése
        * Megjelent az oldal
        * Navigálás a bal menüben a következő menüpontra: "Partnerek"
        # Explicit wait
        * Megvárjuk, hogy eltűnjön a táblázatból a következő szöveget tartalmazó element: "No records to display"
        * Megjelent az ügyfelek grid
        * Letöltött partnerek rögzítése

    Forgatókönyv: Telephelyek rögzítése
        * Navigálás a bal menüben a következő menüpontra: "Telephelyek"
        * Megvárjuk, hogy eltűnjön a táblázatból a következő szöveget tartalmazó element: "No records to display"
        * Telephelyek rögzítése

    Forgatókönyv: Eszközök rögzítése
        * Navigálás a bal menüben a következő menüpontra: "Eszközök"
        * Megvárjuk, hogy eltűnjön a táblázatból a következő szöveget tartalmazó element: "No records to display"
        * Eszközök rögzítése

    Forgatókönyv: Telephely oldalon megjelenő eszköz adatok összevetése az excellel
        * Navigálás a bal menüben a következő menüpontra: "Telephelyek"
        * Megvárjuk, hogy eltűnjön a táblázatból a következő szöveget tartalmazó element: "No records to display"
        * Eszköz adatok összehasolítása az excelben lévő adatokkal

    Forgatókönyv: Szervíz státusz beállítása
        * Navigálás a bal menüben a következő menüpontra: "Eszközök"
        * Megvárjuk, hogy eltűnjön a táblázatból a következő szöveget tartalmazó element: "No records to display"
        * Egy eszköz szervízstátuszának módosítása

    Forgatókönyv: Telephelyek oldalon vizsgáljuk, hogy nem jelenik e meg a szervízben lévő eszköz
        * Navigálás a bal menüben a következő menüpontra: "Telephelyek"
        * Megvárjuk, hogy eltűnjön a táblázatból a következő szöveget tartalmazó element: "No records to display"
        * Egy telephely esetén nem jelennek meg a szervízben lévő eszközök
