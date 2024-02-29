# Team Randomizer

Church Team Randomizer

### Installation Command

```
make setup
make install
```

### Run Server

```
uvicorn src.main:app --reload
```

### PostgreSQL Setup

#### Download PostgreSQL

```
brew install postgresql
```

Connect PostgreSQL instance with a user that has administrative privileges using the psql command line client

#### Check user privileges

```
\du
```

#### Create a new database

```
# Create database
CREATE DATABASE db_name;

# Create database with UTF8 character encoding
CREATE DATABASE school ENCODING 'UTF8';
```

#### List existing databases

```
# List database name
SELECT datname FROM pg_database;

# List database name and other metadata
\l
```

#### Change to a database

```
\c school
```

#### Create a table

```

```
