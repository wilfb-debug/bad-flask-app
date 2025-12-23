## Architecture Overview
- This project demonstrates the transformation of an intentionally insecure cloud-native application into a secure, observable, and scalable architecture using Google Cloud managed services.
- The initial version of the application intentionally demonstrated common cloud anti-patterns, including hardcoded secrets, exposed credentials via HTTP responses, and lack of observability. These issues were then systematically identified and remediated using cloud-native best practices.

## High-Level Architecture
- The application is deployed on Google Cloud Run, a fully managed serverless compute platform. Deployment is automated through a CI/CD pipeline using Cloud Build, with source code hosted in GitHub.
- At runtime, the application retrieves sensitive configuration values from Google Secret Manager rather than storing them in source code. Access to secrets is tightly controlled using a least-privilege IAM service account assigned to the Cloud Run service.

## Core Components

### Cloud Run (Serverless Runtime)
- Hosts the Flask application
- Automatically scales based on incoming traffic
- Scales to zero when idle to reduce cost
- Reads the application port from the PORT environment variable as required by Cloud Run

### Cloud Build (CI/CD)
- Builds and deploys the container image automatically
- Triggered from source control (GitHub)
- Ensures consistent, repeatable deployments

### Secret Manager
- Stores sensitive values such as database hostnames and passwords
- Secrets are accessed at runtime only
- No secrets are hardcoded or exposed in application responses

### Identity and Access Management (IAM)
- Cloud Run uses a dedicated service account
- Granted only secretmanager.versions.access
- Follows the principle of least privilege

### Logging and Monitoring
- Cloud Logging captures application and request logs
- Cloud Monitoring provides metrics and visibility into runtime behavior
- Enables faster debugging and operational awareness

## Security Improvements
- The secure architecture addresses the following risks:
- Secret exposure → Mitigated using Secret Manager and IAM
- Misconfigured container ports → Resolved using environment-based configuration
- Lack of observability → Resolved using built-in logging and monitoring
- Over-privileged access → Resolved using least-privilege service accounts

## Architectural Outcomes
- Secrets are never exposed to end users
- The application follows cloud-native security best practices
- The system is scalable, observable, and cost-efficient
- The architecture is production-aligned and interview-ready
