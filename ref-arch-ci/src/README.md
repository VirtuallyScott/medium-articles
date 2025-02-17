# Reference Architecture CI Example

This directory contains a sample Java application that demonstrates using a manifest-driven CI approach.

## Manifest Format (app-manifest.yml)

The manifest file defines key application metadata and build requirements:

```yaml
app:
  name: string            # Application name
  version: string        # Application version
  type: string          # Application type (java)
  build:
    jdk: string         # JDK version
    framework: string   # Spring Boot, etc
    dependencies:       # Additional build dependencies
      - name: string
        version: string
  
  artifact:
    group: string       # Maven group ID
    name: string       # Artifact name
    type: string       # jar, war, etc
    
  container:
    base: string       # Base image for container
    ports:            # Exposed ports
      - port: number
    env:              # Environment variables
      - name: string
        value: string
```

The CI pipeline will read this manifest to:
1. Build the Java application using specified JDK/framework
2. Package as defined artifact type
3. Build container image with specified base image
4. Push to artifact/container registries

This approach allows teams to define their application requirements declaratively while leveraging standardized CI pipelines.
