# Use Python 3.10 on Debian (slim is Debian-based)
# Explicitly set platform to linux/amd64 as requested
FROM --platform=linux/amd64 python:3.10-slim

# Set working directory
WORKDIR /app

# Copy the static site
COPY site /app/site

# Expose port 8080 as requested
EXPOSE 8080

# Run the server on port 8080
CMD ["python", "-m", "http.server", "8080", "--directory", "site", "--bind", "0.0.0.0"]
