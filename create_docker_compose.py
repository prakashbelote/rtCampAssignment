def create_docker_compose():
    compose_file = """
version: '3.8'

services:
  httpd:
    image: httpd:latest
    ports:
      - 80:80
    volumes:
      - ./httpd/conf.d:/etc/httpd/conf.d
      - ./httpd/html:/usr/share/httpd/html
    depends_on:
      - php

  php:
    image: php:latest
    volumes:
      - ./php:/var/www/html
    depends_on:
      - mysql

  mysql:
    image: mysql:latest
    environment:
      MYSQL_ROOT_PASSWORD: Password@123
      MYSQL_DATABASE: database
      MYSQL_USER: admin
      MYSQL_PASSWORD: Password
    volumes:
      - ./mysql:/var/lib/mysql
"""

    with open('docker-compose.yml', 'w') as file:
        file.write(compose_file)

    print("Docker Compose file 'docker-compose.yml' has been created successfully!")

create_docker_compose()
