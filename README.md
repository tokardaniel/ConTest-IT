# ConTest-IT

## Tesztek futtatása

```shell
    behave path/to/featurefile
```

### Tesztek futtatása dockerben

#### Image elkészítése

```shell
    ./docker-build.ps1
```

#### Teszt futtatása docker konténerben

```shell
    ./run-test.ps1 path/to/featurefile
```

### Dashbord

A tesztek futáskor allure kompatibilis json reportot állítanak elő. Ezek a fájlok egy un. docker volume-ba kerülnek, amiket fel tud olvasni egy másik konténer, ami egy weboldalt tud megjeleníteni, rajta a teszt futások eredményével.

#### Dashboard image készítés

```shell
    ./build-report-server.ps1
```

#### Dashboard indítása

```shell
    ./start-report-server.ps1
```
Ha sikeresen elindult, akkor a következő URL-en érhető el a böngészőből: http://localhost:9999