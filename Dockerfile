FROM python:3
WORKDIR /mydata
COPY readCSVFile.py ./
RUN pip install pandas
RUN python readCSVFile.py
CMD ["python3","./readCSVFile.py"]