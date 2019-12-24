FROM python:3
WORKDIR /mydata
COPY readCSVFile.py ./
RUN pip install pandas
CMD ["python3","./readCSVFile.py"]