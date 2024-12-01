import json
from fastapi import FastAPI, Query
from datetime import datetime, timedelta
from typing import List

app = FastAPI()

cve_data = []

def load_cve_data():
    global cve_data
    try:
        with open("cve_data.json", "r") as f:
            cve_data = json.load(f)["vulnerabilities"]
    except Exception as e:
        print(f"Error loading CVE data: {e}")
        cve_data = []

load_cve_data()

@app.get("/info")
def get_info():
    return {
        "app_name": "CVE Explorer",
        "author": "tanyavka",
        "description": "FastAPI додаток для роботи з CVE",
        "version": "1.0.0"
    }

@app.get("/get/all")
def get_all_cves():
    ten_days_ago = datetime.now() - timedelta(days=10)
    recent_cves = [
        cve for cve in cve_data
        if datetime.strptime(cve["dateAdded"], "%Y-%m-%d") >= ten_days_ago
    ]
    return recent_cves[:40]

@app.get("/get/new")
def get_new_cves():
    sorted_cves = sorted(
        cve_data, key=lambda x: datetime.strptime(x["dateAdded"], "%Y-%m-%d"), reverse=True
    )
    return sorted_cves[:10]

@app.get("/get/known")
def get_known_ransomware():
    known_cves = [
        cve for cve in cve_data if cve.get("knownRansomwareCampaignUse") == "Known"
    ]
    return known_cves[:10]

@app.get("/get")
def search_cves(query: str = Query(...)):
    filtered_cves = [
        cve for cve in cve_data if query.lower() in cve["cveID"].lower()
        or query.lower() in cve.get("shortDescription", "").lower()
    ]
    return filtered_cves

@app.post("/reload")
def reload_data():
    load_cve_data()
    return {"status": "Data reloaded successfully"}
