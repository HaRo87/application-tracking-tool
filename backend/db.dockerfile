FROM postgres:17.4-bookworm

ARG PG_DATA=/var/lib/psql/data
ENV PGDATA=$PG_DATA
