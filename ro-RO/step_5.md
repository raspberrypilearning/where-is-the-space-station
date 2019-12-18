## Unde este SSI?

Stația Spațială Internațională este pe orbită în jurul Pământului. Face o rotație completă a pământului aproximativ la fiecare oră și jumătate și călătorește cu o viteză medie de 7,66 km pe secundă. E rapidă!

Să folosim un alt serviciu web pentru a afla unde se află Stația Spațială Internațională.

+ Mai întâi, deschide adresa URL pentru serviciul web într-o nouă filă din browser: <a href="http://api.open-notify.org/iss-now.json" target="_blank"> http://api.open-notify.org/iss-now.json </a>

Ar trebui să vezi ceva ca mai jos:

    {
    "iss_position": {
      "latitude": 8.54938193505081, 
      "longitude": 73.16560793639105
    }, 
    "message": "success", 
    "timestamp": 1461931913
    }
    

Rezultatul conține coordonatele punctului de pe Pământ pe care SSI se află în prezent.

[generic-theory-lat-long]

+ Acum trebuie să apelezi același serviciu web din Python. Adăugă următorul cod la sfârșitul scriptului pentru a obține locația curentă a SSI:

![captură de ecran](images/iss-location.png)

+ Să creăm variabile pentru a stoca latitudinea și longitudinea, apoi să le tipărim:

![captură de ecran](images/iss-coordinates.png)