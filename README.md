# HubSpot CRM Connector -README (OAuth 2.0)

This project provides a simple Python connector class to interact with the **HubSpot CRM API** using OAuth 2.0 credentials.  
It supports operations like fetching all leads, creating leads, updating leads, and exporting leads to CSV.

---

## 🔧 Installation

Clone your project and install the required dependencies:

```bash
pip install requests


---

## 🚀 Features
- Create new leads 
- Update leads by email  
- Fetch lead details by email  
- Fetch all leads List  
- Export all leads to **CSV**  


---

## 📂 Project Structure
```
hub_spot/
    │──hubspot
    │── __init__.py
    │── hubspot_connector.py       # Main connector file
│── README.md                   # Project documentation
│── requirements.txt            # Python dependencies
│── setup.py                    # Build & packaging file
│──script.sh                    # shell script to
```


```Python Virtual Environment Setup: Ubuntu,Linux,macOS/Windows```

```Creating a virtual environment helps you manage project-specific dependencies without affecting the global Python installation.```

```Use the commands below to create, activate, and deactivate a venv on both Ubuntu and Windows.```

```Platform	                Create venv	                Activate venv	            Deactivate```
   ------------------------------------------------------------------------------------------
    Ubuntu/Linux/macOS	    python3 -m venv venv	    source venv/bin/activate	deactivate
    Windows (CMD)	        python -m venv venv	        venv\Scripts\activate	    deactivate
    Windows (PowerShell)	python -m venv venv	        venv\Scripts\Activate.ps1	deactivate



### How to Use / Test This Class with `.env`

1. Create a `.env` file in the project root and add your hubspot credentials:
        and make sure you have fallow the (### 2️⃣ Install dependencies) step

    ```env
    CLIENT_ID=YOUR_CLIENT_ID
    CLIENT_SECRET=YOUR_CLIENT_SECRET
    ACCESS_TOKEN=YOUR_ACCESS_TOKEN
    REFRESH_TOKEN=YOUR_REFRESH_TOKEN
    ```

2. In your test file or script, import the class and create an object:

    ```python
    from hubspot import HubSpotConnector

    hubspot = HubSpotConnector(
     client_id = os.getenv("CLIENT_ID")
    client_secret = os.getenv("CLIENT_SECRET")
    refresh_token = os.getenv("REFRESH_TOKEN")
    access_token = os.getenv("ACCESS_TOKEN")
    )
    ```


## 🧩 Usage Examples

### ✅ Create a New Lead

hubspot.get_all_leads()

hubspot.create_lead(firstname,lastname,email)

hubspot.update_lead(email,updated_fields={})

hubspot.get_lead_by_email(email)

hubspot.export_leads_to_csv(file_name,path)