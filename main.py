import requests
import time

url = "https://price.jup.ag/v4/dlmm/reference-fees"

try:
    r = requests.get(url, timeout=10)
    print(f"✅ STATUS: {r.status_code}")
    print(r.text[:500])
except Exception as e:
    print(f"❌ ERROR: {e}")

# Не дать Railway сразу завершиться:
while True:
    time.sleep(60)
