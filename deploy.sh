#!/bin/bash

# Deployment script for Sistem Manajemen Data
# Usage: ./deploy.sh [production|staging]

set -e

ENVIRONMENT=${1:-production}
echo "🚀 Deploying to $ENVIRONMENT environment..."

# Check if Docker is installed
if ! command -v docker &> /dev/null; then
    echo "❌ Docker is not installed. Please install Docker first."
    exit 1
fi

# Check if docker-compose is installed
if ! command -v docker-compose &> /dev/null; then
    echo "❌ Docker Compose is not installed. Please install Docker Compose first."
    exit 1
fi

# Create necessary directories
mkdir -p data ssl logs

# Set environment variables
export FLASK_ENV=$ENVIRONMENT
export SECRET_KEY=$(openssl rand -hex 32)

echo "📦 Building Docker images..."
docker-compose build

echo "🔄 Stopping existing containers..."
docker-compose down

echo "🚀 Starting services..."
docker-compose up -d

echo "⏳ Waiting for services to be ready..."
sleep 10

# Health check
echo "🏥 Performing health check..."
if curl -f http://localhost:5000/ > /dev/null 2>&1; then
    echo "✅ Deployment successful!"
    echo "🌐 Application is running at: http://localhost:5000"
    echo "🔑 Admin credentials: admin / admin123"
else
    echo "❌ Health check failed. Check logs with: docker-compose logs"
    exit 1
fi

echo "📊 Deployment completed successfully!"
echo ""
echo "Useful commands:"
echo "  View logs: docker-compose logs -f"
echo "  Stop services: docker-compose down"
echo "  Restart services: docker-compose restart"
echo "  Update application: git pull && ./deploy.sh"
