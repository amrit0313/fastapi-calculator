# FastAPI Calculator Microservice (dockerized)

A simple and clean calculator microservice built using FastAPI that supports basic arithmetic operations via API endpoints.

---

## What This Project Does

This app allows users to perform basic calculations like:

- Addition: `/add?a=10&b=5`
- Subtraction: `/subtract?a=10&b=5`
- Multiplication: `/multiply?a=10&b=5`
- Division: `/divide?a=10&b=5`

The app follows good development practices including:

- `.env`-based configuration
- Clear project structure
- Easy local development with FastAPI

---

to get the code:
git clone https://github.com/amrit0313/fastapi-calculator
cd fastapi-calculator

to run with docker:
docker build -t calculator .  
docker run -p 7000:7000 calculator
