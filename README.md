# ocr-python

## Get started

Install teseract MacOs

```shell script
brew install tesseract
``` 

Create a new python environment & install requirements

```shell script
python -m venv en
source env/bin/activate
pip install -r requirements.txt
```

## Execute example with test image 01

```shell script
python ocr.py --image img/example_01.png
```