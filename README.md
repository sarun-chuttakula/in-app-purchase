# In-App Purchase Integration Guide

This guide provides instructions on how to integrate in-app purchase functionality into your application using the Google Play Billing API and the inapppy Python library.

## Prerequisites

Before integrating in-app purchases into your application, ensure you have the following:

- A Google Play Developer account.
- A published application on the Google Play Store.
- A service account key file (.json) with appropriate permissions for accessing the Google Play Developer API.

## Installation

To use the `inapppy` library for in-app purchases, you can install it via pip:

```bash
pip install inapppy
```

Configuration
Google Play Developer Console:
Navigate to the Google Play Developer Console and create a service account with appropriate permissions for managing in-app purchases.
Download the service account key file (.json) and securely store it.
Credentials Setup:
Specify the path to your service account key file in the credentials_file_path variable within the script.

Usage
Making a New Subscription Purchase
To make a new subscription purchase:

Choose action 1 from the prompt.
Enter the package name and subscription ID when prompted.
Input the developer payload.
Follow the on-screen instructions.
Verifying a Subscription Purchase
To verify a subscription purchase:

Choose action 2 from the prompt.
Enter the package name, subscription ID, and purchase token when prompted.
Input the developer payload.
Follow the on-screen instructions.
Canceling a Subscription Purchase
To cancel a subscription purchase:

Choose action 3 from the prompt.
Enter the package name, subscription ID, and purchase token when prompted.
Follow the on-screen instructions.
