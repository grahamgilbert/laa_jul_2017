FROM python:2
# COPY requirements.txt /requirements.txt
# RUN pip install -r /requirements.txt
RUN pip install django djangorestframework
COPY . /app
COPY run.sh /run.sh
RUN chmod +x /run.sh
CMD ["/run.sh"]
