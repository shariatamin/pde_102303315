# Data Engineering Project

This repository contains the solution for the "Data Engineering" portfolio project. The project focuses on designing and implementing a robust, scalable, and maintainable data architecture for data-intensive applications.

## Project Overview

This project explores main task in data engineering:

**Task 1: Batch-Processing-Based Data Architecture:** Design and implement a data infrastructure capable of ingesting, storing, pre-processing, and aggregating massive amounts of data for a machine learning application that runs quarterly. [cite_start]The focus is on scheduled batch processing. [cite: 13, 14, 15]

The project adheres to modern data engineering principles such as Infrastructure as Code (IaC) and Microservices (MS), utilizing Docker for containerization to ensure security, isolation, and failover recovery. [cite: 9, 28, 96]

## Project Phases & Deliverables

The project was structured into three main phases, reflecting the typical lifecycle of a data engineering solution:

* **Conception Phase:** Focused on architectural design, technology selection (e.g., Apache Kafka, Hadoop, Spark), ensuring reliability, scalability, maintainability, data security, governance, and protection. [cite_start]This phase also included sample data source selection and a visual architectural draft. [cite: 19, 23, 24, 28, 32, 45, 90, 92, 93, 96, 100, 115]
* **Development/Reflection Phase:** Involved the practical implementation of the designed data processing system locally using Docker containers. [cite_start]Data ingestion, pre-processing, and aggregation were implemented and verified. [cite: 56, 57, 58, 59, 60, 61, 62, 63, 64, 126, 127, 128, 129, 130, 131, 132, 133]
* **Finalization Phase:** Included fine-tuning the code, assessing system performance against requirements, and reflecting on challenges, improvements, and learned skills. [cite_start]A key part of this phase was discussing strategies for introducing a second data pipeline (real-time for batch project, batch for real-time project). [cite: 71, 72, 73, 74, 75, 76, 77, 78, 140, 141, 142, 143, 144, 145, 146, 147]

## Project Structure

The repository is organized as follows:
.

├── src/                                              # Contains the source code for microservices (e.g., Python scripts)

│   ├── ingestion_service/

│   │   └── ingest_data.py

│   ├── processing_service/

│   │   └── process_data.py

│   └── aggregation_service/

│       └── aggregate_data.py

├── docker-compose.yml                                # Defines and links all Docker services

├── Dockerfile.

## Technologies Used

* **Docker & Docker Compose:** For containerization and orchestrating microservices. [cite: 29, 59, 97, 129]
* **Apache Kafka (or similar):** For data ingestion/streaming (depending on task). [cite: 21, 90]
* **Apache Spark (or similar):** For data processing and aggregation. [cite: 21, 90]
* **[Database Technology, e.g., PostgreSQL, MongoDB, Cassandra]:** For data storage. 
* **Python:** For scripting data processing logic.
* **Git & GitHub:** For version control and project hosting. [cite: 26, 57, 66, 95, 127, 135]

## Getting Started

To run this project locally, you need to have **Docker** and **Docker Compose** installed on your machine.

### Prerequisites

* [Docker Desktop](https://www.docker.com/products/docker-desktop/) (includes Docker Engine and Docker Compose) installed.

### Setup Instructions

Follow these steps to set up and run the data pipeline:

1.  **Clone the Repository:**
    ```bash
    git clone [https://github.com/shariatamin/pde_102303315.git](https://github.com/shariatamin/pde_102303315.git)
    cd pde_102303315
    ```

2.  **Prepare Data (if applicable):**
    * **For Batch Processing (Task 1):** The project expects a data file in the `data/` directory. A small `sample_data.csv` is included for initial testing. For larger datasets (as per project requirements, at least 1,000,000 data points ), place your chosen data file (e.g., from Kaggle [cite: 33, 101]) into the `data/` directory. Ensure it's time-referenced with a timestamp for each data point[cite: 34, 102].
        ```bash
        # Example: Placing your large dataset
        cp /path/to/your/large_dataset.csv data/your_large_dataset.csv
        ```
        *If your ingestion service expects a specific filename, you might need to rename your file or adjust the ingestion script.*

    * **For Real-Time Processing (Task 2):** If your project simulates real-time data or connects to an external stream, ensure any necessary setup (e.g., API keys, environment variables) is configured, or follow the instructions in your `src/ingestion_service` if a local data generation script is provided. If using a static source to simulate real-time features, ensure `sample_data.csv` is appropriately structured. [cite: 103, 104]

3.  **Build and Run Docker Containers:**
    Navigate to the root directory of the cloned repository (where `docker-compose.yml` is located) and run the following command:
    ```bash
    docker compose up --build -d
    ```
    * `--build`: This flag ensures that Docker builds fresh images for your services based on your `Dockerfile`s.
    * `-d`: This flag runs the containers in detached mode (in the background).

    This command will:
    * Build Docker images for your custom services (if defined).
    * Download any required public Docker images (e.g., Kafka, Spark).
    * Create and start all services defined in your `docker-compose.yml` (e.g., ingestion, processing, aggregation, database).

4.  **Verify Service Status:**
    You can check the status of your running containers with:
    ```bash
    docker compose ps
    ```
    All services should show a `healthy` or `running` status.

5.  **Accessing Services (Optional - for debugging/monitoring):**
    * **Logs:** To view the logs of a specific service (e.g., `ingestion_service`):
        ```bash
        docker compose logs -f ingestion_service
        ```
    * **Execute commands inside a container:** To open a shell inside a running container (e.g., `processing_service`):
        ```bash
        docker compose exec processing_service /bin/bash
        ```
    * **Exposed Ports:** If you have exposed ports in your `docker-compose.yml` (e.g., for a database UI or a monitoring tool), you can access them via `localhost:<port>`.

### Stopping and Cleaning Up

To stop and remove all services and networks created by Docker Compose:

```bash
docker compose down
```

To remove all volumes (persisted data for databases, etc.) as well:

```bash
docker compose down --volumes
```

## How It Works (Conceptual Flow)
(This section assumes a general data flow based on the project description. Adapt it to your specific implementation details for each task.)

**For Batch Processing (Task 1):**
1. **Data Ingestion:** The ingestion_service reads data from the data/ directory (or a simulated source) in batches. This data is then typically pushed to a storage layer. 


2. **Data Storage:** Raw ingested data is stored effectively in a chosen database (e.g., a data lake or data warehouse component). 


3. **Pre-processing & Aggregation:** The processing_service and aggregation_service (or combined components) retrieve data from storage, perform necessary cleaning, transformations, and aggregations according to the defined logic. 


4. **Data Delivery:** The aggregated data is then made available for the downstream machine learning application. 


**Important Considerations**

* **Reproducibility:** The entire setup is designed to be reproducible using Docker and Docker Compose. 





* **Scalability & Maintainability:** The microservices architecture and chosen technologies are intended to promote scalability and maintainability. 






* **Data Security & Governance:** Measures for data security, governance, and protection were considered during the design and implementation phases. 





* **Local Deployment:** For development purposes, the system is deployed locally using Docker. Cloud deployment is not part of this project. 


## Contact
For any questions regarding this project, please feel free to open an issue on this GitHub repository.
