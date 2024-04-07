import inapppy
import google.auth
from google.oauth2 import service_account
from google.auth.transport.requests import AuthorizedSession
from google.auth.exceptions import DefaultCredentialsError

class InAppManager:
    def __init__(self, credentials_file_path):
        self.credentials_file_path = credentials_file_path
        try:
            self.creds, _ = google.auth.default(scopes=['https://www.googleapis.com/auth/androidpublisher'])
        except DefaultCredentialsError as e:
            print(f"Error loading credentials: {e}")
    
    def make_purchase_and_verify(self, package_name, subscription_id, developer_payload):
        # Initialize the InAppPy object
        inapp = inapppy.InAppPy()

        # Purchase the product
        purchase = inapp.purchase(package_name)

        # Check if the purchase was successful
        if purchase.success:
            # The purchase was successful
            print("Purchase successful!")
            
            # Get necessary purchase details
            token = purchase.purchase_token
            
            # Acknowledge the subscription purchase
            self.acknowledge_subscription_purchase(package_name, subscription_id, token, developer_payload)
        else:
            # The purchase failed
            print("Purchase failed.")

    def acknowledge_subscription_purchase(self, package_name, subscription_id, token, developer_payload):
        session = AuthorizedSession(self.creds)

        url = f'https://androidpublisher.googleapis.com/androidpublisher/v3/applications/{package_name}/purchases/subscriptions/{subscription_id}/tokens/{token}:acknowledge'

        request_body = {
            'developerPayload': developer_payload
        }

        response = session.post(url, json=request_body)

        # Check if the request was successful (status code in the range 200 to 299)
        if 200 <= response.status_code < 300:
            print('Subscription purchase acknowledged successfully.')
        else:
            print(f'Error acknowledging subscription purchase: {response.status_code} - {response.text}')

    def cancel_subscription_purchase(self, package_name, subscription_id, token):
        session = AuthorizedSession(self.creds)

        url = f'https://androidpublisher.googleapis.com/androidpublisher/v3/applications/{package_name}/purchases/subscriptions/{subscription_id}/tokens/{token}:cancel'

        response = session.post(url)

        # Check if the request was successful (status code in the range 200 to 299)
        if 200 <= response.status_code < 300:
            print('Subscription purchase canceled successfully.')
        else:
            print(f'Error canceling subscription purchase: {response.status_code} - {response.text}')

def prompt_action():
    print("Choose an action:")
    print("1. Make a new subscription purchase")
    print("2. Verify a subscription purchase")
    print("3. Cancel a subscription purchase")
    return input("Enter your choice (1/2/3): ")

def get_subscription_details():
    package_name = input("Enter the package name: ")
    subscription_id = input("Enter the subscription ID: ")
    return package_name, subscription_id

# Example usage
credentials_file_path = '/path/to/your/credentials.json'
inapp_manager = InAppManager(credentials_file_path)

action = prompt_action()

if action == '1':
    package_name, subscription_id = get_subscription_details()
    developer_payload = input("Enter the developer payload: ")
    inapp_manager.make_purchase_and_verify(package_name, subscription_id, developer_payload)
elif action == '2':
    # Implement verification logic
    package_name, subscription_id = get_subscription_details()
    developer_payload = input("Enter the developer payload: ")
    token = input("Enter the purchase token: ")
    inapp_manager.acknowledge_subscription_purchase(package_name, subscription_id,token, developer_payload)
    pass
elif action == '3':
    # Implement cancellation logic
    package_name, subscription_id = get_subscription_details()
    token = input("Enter the purchase token: ")
    inapp_manager.cancel_subscription_purchase(package_name, subscription_id, token)
    pass
else:
    print("Invalid choice. Please choose 1, 2, or 3.")
