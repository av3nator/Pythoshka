FROM python:3-onbuild
COPY . .
CMD ["python", "main.py"]