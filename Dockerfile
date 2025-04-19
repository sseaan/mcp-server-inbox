FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy project files
COPY pyproject.toml ./
COPY README.md ./
COPY main.py ./
COPY inbox.py ./

# Install dependencies directly
RUN pip install --no-cache-dir requests>=2.28.0 mcp[cli]>=1.4.1

# Environment variables will be provided at runtime
# Example: -e INBOX_TOKEN=your_token_here

# Use python main.py directly as the entrypoint
CMD ["python", "main.py"]