FROM python:2
RUN pip install Flask requests
COPY . /app
COPY run.sh /run.sh
RUN chmod +x /run.sh
CMD ["/run.sh"]
