#language: hu

Jellemző: Létrehozunk öt új partnert, hozzájuk egy-egy telephelyet és egy-egy eszközt

    Forgatókönyv: Adatok begyűjtése
        * "1" db új adat betöltése API-n keresztül

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

    Forgatókönyv: Szervíz státusz beállítása
        * Navigálás a bal menüben a következő menüpontra: "Telephelyek"
        * Megvárjuk, hogy eltűnjön a táblázatból a következő szöveget tartalmazó element: "No records to display"

    Forgatókönyv: Telephely oldalon megjelenő eszköz adatok összevetése az excellel
        * Eszköz adatok összehasolítása az excelben lévő adatokkal
