# CI Pipeline for Reference Architecture

This directory contains the CI pipeline configuration that implements a standardized build and deployment process based on application manifests.

## Manifest Usage

The `app-manifest.yml` file drives the entire CI/CD process:

### Build & Artifact Publishing
```yaml
app:
  name: <name>          # Used for artifact naming
  version: <version>    # Sets artifact version
  build:
    jdk: <version>     # Determines JDK version in CI
    framework: <type>  # Configures build tools
```
- CI reads JDK version to set up build environment
- Artifact is published using name/version from manifest
- Dependencies are installed based on manifest specs

### Container Build
```yaml
app:
  container:
    base: <image>      # Base container image
    ports:            # Container port configuration
      - port: <number>
    env:              # Runtime environment variables
      - name: <name>
        value: <value>
```
- Container build uses specified base image
- Ports from manifest are exposed in container
- Environment variables are configured in container

## Pipeline Workflows

1. **Build and Publish Artifact** (.github/workflows/build-artifact.yml)
   - Triggered on:
     - Push to main branch
     - Pull request to main
   - Actions:
     - Reads manifest for JDK version
     - Sets up build environment
     - Builds and tests application
     - Publishes to GitHub Packages

2. **Container Image Build** (.github/workflows/build-container.yml)
   - Triggered on:
     - New artifact publication
     - Monthly schedule (base image updates)
   - Actions:
     - Downloads artifact from GitHub Packages
     - Builds container with manifest configuration
     - Pushes to GitHub Container Registry

## Benefits

- Declarative application configuration
- Standardized build process
- Automated security updates
- Clear separation of concerns
- Infrastructure as Code

## Implementation

The pipeline is implemented using GitHub Actions workflows in:
- .github/workflows/build-artifact.yml
- .github/workflows/build-container.yml
