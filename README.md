# Team2-Projekt4
Dette er et repositorie omhandlende EH4/EEH4-PRO4, beskriver hvordan en solcelle teststand skal benyttes for at kunne udføre et fysik forsøg på Elektronik/Elektrisk Energiteknologi på 1. semester. Repositoriet inderholder alle program filer der skal til for at køre testanden.  
Nedenfor ses en guide til hvordan man indstiller teststanden fra serversiden. Derudover er der nogle forskellige dukumenter der kan anvendes i forbindelse med opgaven.

* [Skabelon](https://github.com/au634825/Team2-Projekt4/blob/main/Fysik%20opgave/Fysik%20-%20%C3%B8velse%201%20-%20SKABALON.xlsx)
* [Fysik opgaven](https://github.com/au634825/Team2-Projekt4/blob/main/Fysik%20opgave/Fysik%20solpanel%20opgave.pdf)

## Guide
### Opretter navn:
Her bedes du indtaste dit navn eller jeres team navn/nummer.

### Solpanel vinkel:
Vinklen på solpanelet kan ændres til følgende værdier: [0°, 15°, 30°, 45°, 60°, 75°, 90°]. Når vinklen står til 0° vil panelet stå vinkelret på lyskilden. På 90° vil den stå med siden til. Værdien vælges fra drop-down menuen.

### Lysstyrke:
Lysintensiteten kan ændres til følgende værdier: [0%, 25%, 50%, 75%, 100%]. Når lysstyrken er på 0% vil lyskilden være slukket. På 100% vil der være maks. Lysstyrke, 100% svare ca. til at lyskilden lyser med 100W. Værdien vælges fra drop-down menuen.

### Load modstand:
Modstandsværdien kan ændres fra 0Ω til maks. 924Ω. Modstandsværdien skal indtastes af brugeren som et positivt heltal.

### Data tabel:
Datatabellen udfyldes med data fra sensorer kort efter knappen ”opdater data” trykkes. Herefter skal du kopiere værdierne over i et værktøj til databehandling. Vi anbefaler værktøjet ”Excel”. For hver gang du ændrer på nogle af parametrene og trykker ”opdater data” vil dataene i tabellen erstattes af de nye. Husk derfor at gemme dem før du foretager næste måling.

### Knap ”opdater data”:
Når du har valgt solpanelets vinkel, lysstyrken og load modstanden skal du trykke på knappen ”opdater data” for at tage målingen. Når du trykker på knappen, vil lyskilden i teststanden tændes og sensorerne vil herefter måle det de skal og sende dataene til serveren som du kigger på her. Denne proces tager ca. 5 sec.

