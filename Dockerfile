FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy project files
COPY pyproject.toml ./
COPY README.md ./
COPY main.py ./
COPY inbox.py ./

# Install build dependencies
RUN pip install --no-cache-dir setuptools wheel

# Install project dependencies
RUN pip install --no-cache-dir .

# Environment variables will be provided at runtime
# Example: -e INBOX_TOKEN=your_token_here

# Use python main.py directly as the entrypoint
CMD ["python", "main.py"]