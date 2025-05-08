# README

This README would normally document whatever steps are necessary to get the application up and running.

## Login Page

![Screenshot 2025-05-08 at 9 17 12 PM](https://github.com/user-attachments/assets/67f28ea2-3b3f-4d41-8877-e12fb3b2cce4)

## Country List Page

![Screenshot 2025-05-08 at 9 18 06 PM](https://github.com/user-attachments/assets/c4e9d9cc-1a9c-4e26-a69b-d8675317e01a)


## Country Details Page

![Screenshot 2025-05-08 at 9 18 31 PM](https://github.com/user-attachments/assets/4a71131c-e17d-404b-b69a-cf8a0d475f9b)


### Prerequisites
The setup steps expect following tools installed on the system.

- Python >= [3.9.6](javascript:void(0);)
- Django [1.11.29](javascript:void(0);)
- Postgresql [14.15](javascript:void(0);)

##### Dependencies
| Package                       | Version   |
|-------------------------------|-----------|
| certifi                       | 2021.10.8 |
| charset-normalizer            | 2.0.12    |
| djangorestframework           | Data      |
| djangorestframework-simplejwt | 4.1.4     |
| idna                          | 2.10      |
| psycopg2                      | 2.8.6     |
| PyJWT                         | 1.7.1     |
| python-decouple               | 3.8       |
| pytz                          | 2025.2    |
| requests                      | 2.27.1    |
| urllib3                       | 1.26.20   |


## Installation

### Create a new environment

```
python3 -m venv countryAPI
```

### Activate the environment

```
source countryAPI/bin/activate
```

### Clone the project repo

```
https://github.com/hmtanbir/countryInfo.git
```

### Enter into the project repo

```
cd countryInfo
```

## Setup .env file and configure

```
cp -r .env.txt .env
```
Now, open .env file and configure the database configuration

## Install the dependencies

```
pip install -r requirement.txt
```


# Database setup and configuration

You can create using DB Client like DBeaver or you can use shell command

### Enter into postgresql shell:
```
psql -U postgres
```

### Now create the database from the shell:

```
CREATE DATABASE countryinfo;
```
### Now add permission to the database from the shell:
```
GRANT ALL PRIVILEGES ON DATABASE countryinfo TO postgres;
```

### exit database from the shell:

```
\q
```


#### Now migrate the db:

```
python manage.py migrate
```

#### Now create superuser the db:

```
python manage.py createsuperuser
```

### Now Import countries data into the db:

```
python manage.py import_countries
```

### Now run the server:

```
python manage.py runserver
```

### Open browser and click:

Now visit [localhost:8000](http://localhost:8000)



# API Documentation
Please visit this [API Documentation](https://documenter.getpostman.com/view/33611649/2sB2j968eL).


## Author
[HM Tanbir](https://linkedin.com/in/hmtanbir)
