# hw02.12

It is a simple FastAPI application for working with CVE data fetched from the **CISA Known Exploited Vulnerabilities Catalog**. The application allows you to view, filter, and search vulnerabilities using various endpoints.

---

## Features

- Retrieve general information about the application via **/info**.
- Fetch CVEs added in the last 5 days (up to 40 entries) via **/get/all**.
- Get the 10 most recent CVEs via **/get/new**.
- List CVEs with `knownRansomwareCampaignUse = "Known"` (up to 10 entries) via **/get/known**.
- Search CVEs by a keyword in `cveID` or `description` via **/get?query=key**.

---

## Installation and Setup

### Steps to Install
1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/cve-explorer.git
   cd cve-explorer
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
  *Attach a screenshot of the `/info` endpoint response.*

- **/get/all**: Retrieves CVEs added in the last 5 days (up to 40).  
  *Attach a screenshot of `/get/all` results.*

- **/get/new**: Fetches the 10 most recent CVEs.  
  *Attach a screenshot of `/get/new` results.*

- **/get/known**: Lists CVEs with `knownRansomwareCampaignUse = "Known"` (up to 10).  
  *Attach a screenshot of `/get/known` results.*

- **/get?query=vmware**: Searches CVEs by the keyword "vmware".  
  *Attach a screenshot showing search results for the keyword.*

5. **Testing the API**
Use Swagger UI to execute requests and verify the results.
<img width="1507" alt="example" src="https://github.com/user-attachments/assets/6e4bc0f1-56b8-40ad-ad72-cc0d29fb0abb">




