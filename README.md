Stacc code challenge 2022
Oppgavebeskrivelse
Jeg har valgt å gjøre oppgave b), utvikle mitt eget API.

Prosjektet mitt har gått ut på å lage et API. Jeg har ikke gjort spesielt mye med APIer så tenkte at en god måte å lære det på var å lage ett. Jeg har brukt flask i python og databasen MongoDB Atlas for å oppnå dette. Jeg har også lastet opp appen i Heroku så den kan brukes på mobil etc.

I dette APIet kan man hente ut alt innholdet i databasen ved å bruke /api/all. Man kan også søke etter navn ved å bruke /api/name/< din input >. Videre så er det også mulig å søke etter individer som tilhører diverse dataset som f.eks "Every Politician" Denne brukes ved å gå til /api/dataset/< dataset du vil søke på >.

Hvis man vil administrere databasen er det også mulighet til å legge til personer på samme route som å søke: /api/name/ < name > ved å sende en POST request isteden for en GET.


Prosjektet er lastet opp på Heroku og kan nås på https://heroku-kyc.herokuapp.com/ bare legg til routes bak så får du ut innholdet.
Jeg har også opprettet en collection i Postman for kjapp testing av requests. Denne finner man her:https://www.postman.com/navigation-pilot-26434475/workspace/d9c10c8f-5d43-44ea-88dc-6a5fde217198/collection/19260773-c1c7f942-31f3-4de8-9e19-075d357cbaf9?action=share&creator=19260773


Kommentarer
Jeg har aldri brukt hverken python, flask, mongodb eller heroku slik at det gikk mye tid til å lære seg ny tech. Jeg kunne laget en java app som brukte de APIene som var laget fra før men tenkte at jeg kunne prøve noe nytt.

Per nå sjekker ikke dette API noen authorisasjon slik at den er åpen for hvem som helst. Tilgang til databasen ligger også i koden slik at den er ganske utsatt. Jeg har ikke tatt hensyn til dette siden jeg har fokusert på å først å fremst få til et fungerende API på litt begrenset tid.


