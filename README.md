# SC2021
Codice per il calcolo dello spazio cognitivo nei testi letterari

Indicazioni per il corretto funzionamento del programma(da Linux):

necessario un file txt fatto a simil-tabella, per ogni riga il luogo, il numero di occorrenze, la latitudine e la longitudine. Questi devono essere divisi da spazi bianchi.
Si veda l'esempio nel repository "table.txt".
Importante che le stringhe che rappresentano il luogo non presentino spazi bianchi e/o caratteri speciali (no caratteri accentati).
es. "San Francisco" NO - "SanFrancisco" SI

da riga di comando
entrare nel path in cui si trova il programma e il file txt
invocare l'interprete python3 e passargli come argomenti il programma e il file txt:
python3 spaziocognitivo.py table.txt

eseguire

l'output nel terminale corrisponde a
1. riga: latitudine e longitudine del centro di percezione in gradi
2. riga: raggio di percezione in chilometri
