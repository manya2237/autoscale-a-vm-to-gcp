#!/bin/bash

# Threshold CPU usage percentage
THRESHOLD=75

# Interval for checking CPU usage (in seconds)
INTERVAL=10

# Function to check CPU usage
check_cpu_usage() {
    # Get the average CPU usage over 1 second
    CPU_USAGE=$(top -bn1 | grep "Cpu(s)" | awk '{print $2 + $4}')

    # Convert float to integer
    CPU_USAGE_INT=${CPU_USAGE%.*}

    echo "Current CPU Usage: $CPU_USAGE_INT%"

    if [ "$CPU_USAGE_INT" -gt "$THRESHOLD" ]; then
        echo "CPU usage exceeded threshold! Triggering auto-scaling..."
        trigger_auto_scaling
    fi
}

# Function to trigger auto-scaling
trigger_auto_scaling() {
    echo "Creating a new VM on GCP..."
    gcloud compute instances create auto-scaled-vm \
        --machine-type=e2-medium \
        --image-family=ubuntu-2004-lts \
        --image-project=ubuntu-os-cloud \
        --zone=us-central1-a

    echo "New VM instance created successfully!"
}

# Monitor CPU usage continuously
while true; do
    check_cpu_usage
    sleep $INTERVAL
done
