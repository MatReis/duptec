FROM mysql

ENV MYSQL_ROOT_PASSWORD=password

COPY db_file.sql /docker-entrypoint-initdb.d/

EXPOSE 3306
