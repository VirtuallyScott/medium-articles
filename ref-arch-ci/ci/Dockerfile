# Multi-stage build for Java applications
# Stage 1: Download artifact from GitHub Packages
FROM alpine:3.18 as downloader
ARG GITHUB_TOKEN
ARG VERSION
ARG ARTIFACT_NAME
WORKDIR /download
RUN apk add --no-cache curl
RUN curl -H "Authorization: Bearer ${GITHUB_TOKEN}" \
    -L -o app.jar \
    "https://maven.pkg.github.com/owner/repo/com/example/${ARTIFACT_NAME}/${VERSION}/${ARTIFACT_NAME}-${VERSION}.jar"

# Stage 2: Runtime
FROM eclipse-temurin:17-jre-alpine
WORKDIR /app
COPY --from=downloader /download/app.jar app.jar
EXPOSE 8080
ENTRYPOINT ["java", "-jar", "app.jar"]
