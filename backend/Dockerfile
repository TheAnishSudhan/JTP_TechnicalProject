FROM python:3.10
WORKDIR /app
COPY reqs.txt ./
RUN pip3 install -r reqs.txt
COPY . ./
EXPOSE 5001
ENTRYPOINT [ "python3" ]
CMD [ "app.py"]