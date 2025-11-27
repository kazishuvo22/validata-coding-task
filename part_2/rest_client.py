import requests

# Base URL of Flask API
BASE_URL = "http://127.0.0.1:5000/api/banks"

# GET all banks
def get_all_banks():
    response = requests.get(BASE_URL)
    if response.status_code == 200:
        banks = response.json()
        print("All Banks:")
        for b in banks:
            print(f"{b['id']}: {b['name']} ({b['location']})")
        return banks
    else:
        print(f"Error fetching banks: {response.status_code}")
        return []

# GET a single bank by ID
def get_bank(bank_id):
    response = requests.get(f"{BASE_URL}/{bank_id}")
    if response.status_code == 200:
        bank = response.json()
        print(f"Bank {bank_id}: {bank['name']} ({bank['location']})")
        return bank
    else:
        print(f"Error fetching bank {bank_id}: {response.status_code}")
        return None

# CREATE a new bank
def create_bank(name, location):
    payload = {"name": name, "location": location}
    response = requests.post(BASE_URL, json=payload)
    if response.status_code in (200, 201):
        bank = response.json()
        print(f"Created Bank: {bank['id']} - {bank['name']} ({bank['location']})")
        return bank
    else:
        print(f"Error creating bank: {response.status_code} - {response.text}")
        return None

# UPDATE an existing bank
def update_bank(bank_id, name, location):
    payload = {"name": name, "location": location}
    response = requests.put(f"{BASE_URL}/{bank_id}", json=payload)
    if response.status_code == 200:
        bank = response.json()
        print(f"Updated Bank {bank_id}: {bank['name']} ({bank['location']})")
        return bank
    else:
        print(f"Error updating bank {bank_id}: {response.status_code} - {response.text}")
        return None

# DELETE a bank
def delete_bank(bank_id):
    response = requests.delete(f"{BASE_URL}/{bank_id}")
    if response.status_code in (200, 204):
        print(f"Deleted Bank {bank_id}")
        return True
    else:
        print(f"Error deleting bank {bank_id}: {response.status_code} - {response.text}")
        return False


if __name__ == "__main__":
    # Create new bank
    new_bank = create_bank("First Bank", "Dhaka")

    # Get all banks
    get_all_banks()

    # Get a single bank
    if new_bank:
        get_bank(new_bank["id"])

    # Update the bank
    if new_bank:
        update_bank(new_bank["id"], "First Bank Updated", "Chittagong")

    # Delete the bank
    if new_bank:
        delete_bank(new_bank["id"])
