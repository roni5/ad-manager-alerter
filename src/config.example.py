# Copyright 2023 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Config file for the ad manager anomaly detection module"""

import os

# Copy this file to config.py and update the fields below to match your project
# settings

# Step 1, download report to GCS
SERVICE_ACCOUNT = "default"

NETWORK_CODE = "[YOUR_NETWORK_CODE]"

BUCKET = "[YOUR_GCS_BUCKET]"
REPORT_FILE = "report.csv.gz"
COLUMNS_TO_REPORT = ["AD_SERVER_IMPRESSIONS"]
DAYS_IN_REPORT = 60


# Step 2, upload report to bigquery and build model
DATASET = "[YOUR_DATASET]"
TABLE = "historical_report"
ML_MODEL_NAME = "historical_report_model"

COLUMNS_TO_REPORT = ["AD_SERVER_IMPRESSIONS"]
DAYS_IN_REPORT = 60

COLUMN_TO_MONITOR = "Column_AD_SERVER_IMPRESSIONS"

# Step 3, send alerts
DAYS_IN_CHART = 7
# Config on many consecutive anomalies are required for alert to trigger
CONSECUTIVE_ANOMALIES_REQ = 3

SENDER_GMAIL_ADDRESS  = "...@gmail.com"
# Recommended that you define the password as an environment variable
SENDER_GMAIL_PASSWORD = os.environ["SENDER_GMAIL_PASSWORD"]

ALERT_RECEIVERS = ["receiver@example.com"]
