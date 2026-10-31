# Use a lightweight Python runtime
FROM python:3.13-slim

# Set the working directory inside the container
WORKDIR /app

# Copy dependency definitions first
COPY app/requirements.txt ./requirements.txt

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Remove pip's bundled SBOM file that is confusing the image scan
RUN rm -f /usr/local/lib/python3.13/site-packages/pip/_vendor/bom.cdx.json

# Create a non-root application user
RUN useradd --create-home --uid 10001 appuser

# Copy application source code
COPY --chown=appuser:appuser app/ ./app/

# Run the application as a non-root user
USER appuser

# Document the application port
EXPOSE 8000

# Start the API server
CMD ["uvicorn", "main:app", "--app-dir", "app", "--host", "0.0.0.0", "--port", "8000"]