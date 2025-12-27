# Agentic AI Resort Management System (Multi-Agent Framework)

**Author:** Revanth Prasad Yedla  
**Affiliation:** Indian Institute of Technology Kharagpur (IITKGP)  
**Department:** Medical Imaging and Informatics  
**Technology Stack:** Python 3.12 | Google Gemini 2.0 Flash | SQLAlchemy | SQLite | Pandas

---

## 📌 Project Overview
This project implements a sophisticated **Multi-Agent System (MAS)** designed to automate the operations of a large-scale resort. Utilizing an **Agentic AI** framework, the system uses the Google Gemini 2.0 Flash model as a central orchestrator to bridge natural language guest queries with a structured SQL backend.

The system manages a 90-room inventory and a 90-item multi-cuisine menu, ensuring data integrity, security, and real-time billing updates.

## 🛠 Core Features
- **Intelligent Routing:** A central "Resort Manager" analyzes guest intent and delegates tasks to specialized sub-agents.
- **Deterministic Tool Use:** Agents utilize Python-based tools (functions) to interact with the database, eliminating AI "hallucinations".
- **Security Handshake:** Mandatory guest verification via Room Number and Guest ID before any transactional or personal data access.
- **Orderly Billing Model:** Real-time calculation of meal totals for dining orders, updated directly in the guest's digital ledger.
- **Service Request Tracking:** Housekeeping and amenity requests (e.g., towels, laundry) are logged with status tracking in the database.



## 🏗 System Architecture
The architecture follows a **Manager-Worker Pattern**:
1. **Resort Manager (Supervisor):** Performs semantic analysis of user input to determine the required service domain.
2. **Reception Agent:** Handles room availability lookups, pricing for multi-night stays, and resort facility information.
3. **Restaurant Agent:** Manages the 9-category menu and executes the `place_restaurant_order` transaction.
4. **Room Service Agent:** Logs non-billing guest requests to the `service_requests` table.

## 🚀 Installation & Setup

### 1. Prerequisites
- Python 3.10+ installed.
- A Google Gemini API Key.

### 2. Environment Configuration
Create a `.env` file in the root directory:
```text
GEMINI_API_KEY=your_api_key_here

### 3. Technical Stack
The system is built using a modern Python-based informatics stack designed for scalability and data integrity:
Language: Python 3.12+
Generative AI: Google Gemini 2.0 Flash (leveraging advanced reasoning for tool selection)
Database Engine: SQLite (Local persistent storage)
ORM: SQLAlchemy (for systematic relational mapping of rooms and guests)
Data Ingestion: Pandas (used for automated synchronization of the 90-item menu from Excel)
Security: python-dotenv for local environment variable protection

###4. Installation and Setup Instructions
Follow these steps to deploy the Resort AI system on your local machine:
Clone the Repository:

"git clone https://github.com/RevanthPY/Resort_AIsystem_AGENTIC_AI.git"
"cd Resort_AIsystem_AGENTIC_AI"

Install Dependencies:

"pip install -r requirements.txt"

###5. Initialize Database: Run the sync scripts to populate the 90-room inventory and 9-category menu:

"python database.py"
"python sync_rooms.py"
"python create_guests.py"
"python import_menu.py"

###6. Run Application 
"python run_resort.py"
