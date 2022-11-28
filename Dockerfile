FROM nginx:1.18-alpine

## Step 1:
# Create a working directory
WORKDIR /app

RUN rm /usr/share/nginx/html/*

# Copy source code to working directory
COPY . /usr/share/nginx/html