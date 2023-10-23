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


