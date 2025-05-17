# Heart Disease Predictor

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![Django](https://img.shields.io/badge/Django-4.2.6-green.svg)
![Vercel](https://img.shields.io/badge/Vercel-Deployed-black.svg)

A modern web application built with Django and scikit-learn to predict heart disease risk based on user-provided health metrics. Featuring a responsive Bootstrap 5 interface, it offers instant predictions, heart health facts, and lifestyle tips. Deployable on Vercel, this project is ideal for health-focused applications and machine learning enthusiasts.

## Features

- **Heart Disease Prediction**: Uses a RandomForestClassifier trained on the UCI Heart Disease dataset to predict risk.
- **User-Friendly Form**: Input 13 health metrics (e.g., age, cholesterol, blood pressure) with clear guidance.
- **Responsive Design**: Built with Bootstrap 5 and custom CSS for seamless mobile and desktop experiences.
- **Health Insights**: Includes facts, tips, and habits to promote heart health.
- **Vercel Deployment**: Ready-to-deploy with `vercel.json` and `build_files.sh` for static file handling.
- **Secure Configuration**: Environment variables for `SECRET_KEY` and `DEBUG` ensure production safety.


## Prerequisites

- Python 3.9+
- Git
- Vercel CLI (`npm install -g vercel`)
- GitHub account
- Vercel account

## Instructions
1. Clone it
2. pip install -r requirements.txt
3. Also install dotenv. I m deploying in vercel so didn't do it. 
3. create .env(only for local) with the following content without any spaces
    SECRET_KEY=your-secret-key-here
    DEBUG=True
4. in CMD run: 
    python manage.py collectstatic
    python manage.py migrate
    python manage.py runserver
    http://127.0.0.1:8000/

