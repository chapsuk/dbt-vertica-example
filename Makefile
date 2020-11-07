PYTHON_BIN=python3	

.PHONY: generate_data
generate_data:
	$(PYTHON_BIN) ./scripts/generate_datasets.py

.PHONY: create_schema
create_schema:
	docker exec -it bro_vertica /opt/vertica/bin/vsql -U dbadmin -c 'CREATE SCHEMA IF NOT EXISTS "docker"."broapp";'
