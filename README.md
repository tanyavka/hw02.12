# hw02.12

It is a simple FastAPI application for working with CVE data fetched from the **CISA Known Exploited Vulnerabilities Catalog**. The application allows you to view, filter, and search vulnerabilities using various endpoints.

---

## Features

- Retrieve general information about the application via **/info**.
- Fetch CVEs added in the last 10 days via **/get/all**.
- Get the 10 most recent CVEs via **/get/new**.
- List CVEs with `knownRansomwareCampaignUse = "Known"` (up to 10 entries) via **/get/known**.
- Search CVEs by a keyword in `cveID` or `description` via **/get?query=key**.

---

## Installation and Setup

### Steps to Install
1. **Clone the repository**
   ```bash
   git clone https://github.com/tanyavka/hw02.12.git
   cd hw02.12
2. **Install dependencies**
   ```bash
   pip install fastapi uvicorn requests
3. Run the server
   ```bash
   uvicorn main:app --reload --port 6980
The server will start, and Swagger UI will be available at http://127.0.0.1:6980/docs.

## Usage Instructions
1. **Access Swagger UI**
Open http://127.0.0.1:6980/docs in your browser. This interface lists all available endpoints and allows you to test them interactively.
2. **Endpoints Overview**
- **/info**: Displays general information about the application.  
<img width="1459" alt="info-ex" src="https://github.com/user-attachments/assets/615f1df0-a33e-4222-8c79-64ef6dd859ec">

- **/get/all**: Retrieves CVEs added in the last 10 days.  
<img width="1445" alt="all-ex" src="https://github.com/user-attachments/assets/e10fcce0-2d87-495b-bea5-44461ad75655">

- **/get/new**: Fetches the 10 most recent CVEs.  
<img width="1507" alt="new-ex" src="https://github.com/user-attachments/assets/6e4bc0f1-56b8-40ad-ad72-cc0d29fb0abb">

- **/get/known**: Lists CVEs with `knownRansomwareCampaignUse = "Known"` (up to 10).  
<img width="1455" alt="known-ex" src="https://github.com/user-attachments/assets/c7fcacb0-3797-4f8d-938b-49ecaeebf578">

- **/get?query=vmware**: Searches CVEs by the keyword, for example "Oracle".  
<img width="1494" alt="query-ex" src="https://github.com/user-attachments/assets/42724eac-ca18-4269-8256-06b0e056d1e0">
