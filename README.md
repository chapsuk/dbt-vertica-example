# Bro app dbt example

`Bro` application - allows users to register by email in app, 
invite bro by `ref` link likes `http://bro.app?bro=<user_id>` 
and sed `Hey bro!` to bro.

This repo contains dbt-vertica example of bro app

## Requirements

- `python3`
- `docker`
- `dbt 0.18.1`
- `dbt-vertica`

## Run dev env

```
$ docker-compose up -d
```

## Init deps

```
$ dbt deps
```

## Generate datasets

Run `python ./scripts/generate_data.py` to generate events datasets:

1. `reg.csv` - user_id,email,country,ref,created_at
1. `login.csv` - user_id,created_at
1. `bro.csv` - from,to,craeted_at

## Load data to Stage

[This tooks ~10min](https://github.com/mpcarter/dbt-vertica/issues/2)

```
$ dbt seed
```

## Run, test

```
$ dbt run && dbt test
```
