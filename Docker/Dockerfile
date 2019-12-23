FROM nginx:latest
COPY app.conf /etc/nginx/conf.d/
COPY entry-point.sh /usr/bin
RUN chmod +x /usr/bin/entry-point.sh
RUN apt-get update
RUN apt-get install -y apt-utils
RUN apt-get install -y git python3 python3-pip libpq-dev
RUN pip3 install Flask Flask-SQLAlchemy SQLAlchemy Flask-Script Flask-Migrate gpiozero psycopg2
RUN git clone https://github.com/taurus-silver-17/Devops-ing4.git /usr/share/nginx/html/Devops
CMD ./usr/bin/entry-point.sh
