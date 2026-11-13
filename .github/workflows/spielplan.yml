name: FC Frenkendorf Spielplan

on:
  workflow_dispatch:

permissions:
  contents: read

jobs:
  spielplan-test:
    runs-on: ubuntu-latest

    steps:
      - name: Projekt laden
        uses: actions/checkout@v4

      - name: Python einrichten
        uses: actions/setup-python@v5
        with:
          python-version: '3.12'

      - name: FVNWS-Verbindung testen
        run: python spielplan.py
