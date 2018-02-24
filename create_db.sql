CREATE DATABASE prima;
CREATE USER usagistudio WITH PASSWORD 'pplc7';
ALTER ROLE usagistudio SET client_encoding TO 'utf8';
ALTER ROLE usagistudio SET default_transaction_isolation TO 'read committed';
ALTER ROLE usagistudio SET timezone TO 'UTC';
ALTER USER usagistudio createdb;
GRANT ALL PRIVILEGES ON DATABASE prima TO usagistudio;