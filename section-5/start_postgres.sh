docker run -d \
	--name postgresdb \
	-e POSTGRES_PASSWORD=$1 \
	-e PGDATA=/var/lib/postgresql/data/pgdata \
	-v posgres-data:/var/lib/postgresql/data \
    -p 5432:5432 \
    --rm \
	postgres