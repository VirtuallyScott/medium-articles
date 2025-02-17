# CI Pipeline for Reference Architecture

This directory contains the CI pipeline configuration that implements a standardized build and deployment process based on application manifests.

## Pipeline Overview

The pipeline consists of two main workflows:

1. **Build and Publish Artifact**
   - Reads app-manifest.yml to determine build requirements
   - Sets up specified JDK version
   - Builds application using Maven/Gradle
   - Runs tests
   - Publishes artifact to GitHub Packages

2. **Container Image Build**
   - Triggered either by:
     - New artifact publication
     - Monthly schedule for base image updates
   - Pulls latest artifact from GitHub Packages
   - Builds container image using multi-stage Dockerfile
   - Tags and pushes to GitHub Container Registry

## Benefits

- Developers only need to maintain app-manifest.yml
- Standardized build and deployment process
- Regular security updates through scheduled rebuilds
- Clear separation of build and runtime environments
- Automated artifact and container publishing

## Implementation

The pipeline is implemented using GitHub Actions workflows in:
- .github/workflows/build-artifact.yml
- .github/workflows/build-container.yml
