# Dane projektu

## Cel

Ocena ryzyka niewypłacalności posiadaczy kart kredytowych z kalibracją prawdopodobieństw.

## Źródło danych

Źródło: UCI Machine Learning Repository — Default of Credit Card Clients.

- Dane: https://archive.ics.uci.edu/dataset/350/default+of+credit+card+clients 
- Liczba obserwacji: około 30 000.
- Dane dotyczą klientów kart kredytowych na Tajwanie.
- Dane historyczne dotyczą 2005 roku.
- Zmienna docelowa: `default.payment.next.month` — do potwierdzenia po pobraniu i sprawdzeniu danych.

## Organizacja plików

- `raw/` — oryginalne, niezmodyfikowane dane.
- `processed/` — dane przygotowane do analizy i modelowania.

Pliki danych nie są przechowywane w repozytorium Git. Dokumentacja opisuje ich źródło i sposób organizacji.

## Planowane kontrole

Po pobraniu zbioru zostaną sprawdzone:

- liczba wierszy i kolumn,
- nazwy i typy zmiennych,
- braki danych,
- duplikaty,
- rozkład zmiennej docelowej,
- zgodność danych ze źródłem.

## Uwaga

Opis i parametry zbioru zostaną zweryfikowane na podstawie pobranych danych oraz dokumentacji źródłowej.
