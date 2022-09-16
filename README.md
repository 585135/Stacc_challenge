# Stacc Code Challenge 2022

## Introduksjon
Jeg har valgt å gjøre oppgave **b)**, utvikle et API for sjekking av PEP. 

I dette APIet ligger funksjonalitet for å  hente ut alle politisk eksponerte personer som ligger i databsen ved å bruke */api/all*. Man kan også søke etter navn ved å bruke */api/name/< et navn >*. Det er også mulig å søke etter individer som tilhører diverse dataset som f.eks **"Every Politician"**. For å søke i andre dataset gå til */api/dataset/< dataset du vil søke på >*.

Jeg har ikke mye erfaring med APIer så tenkte at en god måte å lære det på var å lage ett. Jeg har brukt Flask biblioteket i Python og databasen MongoDB Atlas for å oppnå dette. Jeg har også lastet opp appen i Heroku så den kan nås overalt.

## Teknologier
* Python
* Flask (API routing)
* MongoDB (Database / lagring)
* Heroku (Cloud Hosting)

## Hvordan bruke prosjektet
For å kjøre prosjektet lokalt må man:
* Hente prosjektet fra github
* Starte et virtual environment
* Installere requirements.txt ved bruk av *pip3 install -r requirements.txt*
* Så kan man kjøre kyc.py og bruke f.eks Postman til å sende requests til http://127.0.0.1:47046/


*PS.* Om man skulle få certification error [SSL: CERTIFICATE_VERIFY_FAILED] må man oppdatere sitt certificate. Dette har jeg lagt i mappen certificate, filen må lastes ned og endres fra *.pem* til *.cer*

Prosjektet er også lastet opp på Heroku og kan nås på [Heroku API baseURL](https://heroku-kyc.herokuapp.com/). Jeg har opprettet en collection i [Postman](https://www.postman.com/navigation-pilot-26434475/workspace/d9c10c8f-5d43-44ea-88dc-6a5fde217198/collection/19260773-c1c7f942-31f3-4de8-9e19-075d357cbaf9?action=share&creator=19260773) for testing av requests og dokumentasjon på de forskjellige kallene. 

## Kommentarer 
Jeg har aldri brukt hverken Python, Flask, MongoDB eller Heroku så mye av tiden gikk på å lære seg ny tech. Jeg hadde originalt planlagt å lage en Java applikasjon som brukte de APIene som var laget fra før men tenkte at jeg kunne prøve noe nytt.

Per nå bruker ikke dette APIet noen autentisering så den er åpen for hvem som helst. Tilgang til databasen ligger også i koden slik at den er ganske utsatt. Jeg har ikke tatt hensyn til dette siden jeg har fokusert på å først å fremst få til et fungerende API på litt begrenset tid.