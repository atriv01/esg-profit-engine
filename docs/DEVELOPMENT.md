# Local Development Guide - ESG Profit Engine

## 1. Prerequisites
- Docker & Docker Compose
- Python 3.10+
- Node.js 18+ (for frontend development)

## 2. Start Infrastructure (PostgreSQL & Redis)
Run Docker Compose from the root directory to spin up the local database and cache:
```bash
docker-compose up -d
