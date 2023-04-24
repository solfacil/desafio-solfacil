FROM mysql:latest

ENV MYSQL_DATABASE solfacil
ENV MYSQL_USER admin
ENV MYSQL_PASSWORD root
ENV MYSQL_ROOT_PASSWORD root

COPY ./sql-scripts/ /docker-entrypoint-initdb.d/