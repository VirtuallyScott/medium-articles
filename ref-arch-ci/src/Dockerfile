# This is a multi-stage Dockerfile that separates the build environment from the runtime environment
# Stage 1: Build stage
FROM eclipse-temurin:17-jdk AS builder
WORKDIR /build
COPY . .
RUN ./mvnw clean package -DskipTests

# Stage 2: Runtime stage
FROM eclipse-temurin:17-jre-alpine
WORKDIR /app
COPY --from=builder /build/target/*.jar app.jar
EXPOSE 8080
ENTRYPOINT ["java", "-jar", "app.jar"]
