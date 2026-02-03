#!/bin/bash
echo "--- RIAKOINE EMPIRE STATUS ---"
docker compose ps
echo "--- LATEST INTELLIGENCE ---"
docker compose logs --tail=5 riakoine_cortex
