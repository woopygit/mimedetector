# MIMEDetector

MIMEDetector è una libreria Python che permette di rilevare facilmente il tipo MIME di file locali e URL remoti.

[English Documentation (Documentazione in Inglese)](README.md)

## Installazione

```bash
pip install mimedetector
```

## Utilizzo

```python
from mimedetector import MIMEDetector

# Messaggi di debug in inglese (predefinito)
detector = MIMEDetector()

# Messaggi di debug in italiano
detector_it = MIMEDetector(language="it")

# Controlla un file locale
mime_type = detector.get_MIME("path/to/local/file.pdf")
print(f"Tipo MIME del file locale: {mime_type}")

# Controlla un URL remoto
mime_type = detector.get_MIME("https://example.com/file.pdf")
print(f"Tipo MIME dell'URL: {mime_type}")
```

## Caratteristiche

- Rilevamento automatico tra file locali e URL remoti
- Supporto per percorsi Path e stringhe
- Gestione degli errori robusta
- Debug opzionale per le richieste URL
- Supporto multilingua (Inglese e Italiano)

## Requisiti

- Python 3.7+
- requests

## Licenza

Questo progetto è distribuito sotto licenza MIT.

# Content of docs/en/usage.md
# Detailed Usage Guide

## Basic Usage

The MIMEDetector class provides a simple interface to detect MIME types:

```python
from mimedetector import MIMEDetector

detector = MIMEDetector()
mime_type = detector.get_MIME("file.pdf")
```

## Language Selection

You can choose between English and Italian debug messages:

```python
# English messages
detector_en = MIMEDetector(language="en")

# Italian messages
detector_it = MIMEDetector(language="it")
```

## Error Handling

The library includes robust error handling:

```python
# Enable debug messages
mime_type = detector.get_MIME("https://example.com/nonexistent", ShowDebug=True)
```

# Content of docs/it/usage.md
# Guida all'Utilizzo Dettagliata

## Utilizzo Base

La classe MIMEDetector fornisce un'interfaccia semplice per rilevare i tipi MIME:

```python
from mimedetector import MIMEDetector

detector = MIMEDetector()
mime_type = detector.get_MIME("file.pdf")
```

## Selezione della Lingua

Puoi scegliere tra messaggi di debug in inglese e italiano:

```python
# Messaggi in inglese
detector_en = MIMEDetector(language="en")

# Messaggi in italiano
detector_it = MIMEDetector(language="it")
```

## Gestione degli Errori

La libreria include una gestione degli errori robusta:

```python
# Abilita i messaggi di debug
mime_type = detector.get_MIME("https://example.com/nonexistent", ShowDebug=True)
```