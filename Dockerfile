# Start with a Python base image
FROM python:3.11-slim

# Install system dependencies and Chrome
RUN apt-get update && apt-get install -y \
    wget \
    curl \
    unzip \
    ca-certificates \
    fonts-liberation \
    libappindicator3-1 \
    libasound2 \
    libgbm1 \
    libnspr4 \
    libnss3 \
    libx11-xcb1 \
    libxtst6 \
    xdg-utils \
    && apt-get clean

# Install Google Chrome (Headless)
RUN curl -sS https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb -o google-chrome.deb
RUN dpkg -i google-chrome.deb; apt-get -fy install

# Install Python dependencies
COPY requirements.txt /app/
WORKDIR /app
RUN pip install -r requirements.txt

# Install selenium and webdriver_manager to manage ChromeDriver
RUN pip install selenium webdriver_manager

# Copy your application code
COPY . /app/

# Set environment variable to use headless mode
ENV DISPLAY=:99

# Run your Python application
# CMD ["gunicorn", "app:app"]
CMD ["gunicorn", "--timeout", "120", "app:app"]