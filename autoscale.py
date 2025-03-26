from google.cloud import compute_v1
import psutil
import subprocess

PROJECT_ID = "gcp-vm-452509"
ZONE = "us-central1-c"
INSTANCE_NAME = "autoscale-instance"

def create_vm():
    instance_client = compute_v1.InstancesClient()
    instance = compute_v1.Instance()
    instance.name = INSTANCE_NAME
    instance.zone = ZONE
    instance.machine_type = f"zones/{ZONE}/machineTypes/n1-standard-1"
    operation = instance_client.insert(project=PROJECT_ID, zone=ZONE, instance_resource=instance)
    print("VM created successfully.")

def monitor_and_scale():
    cpu_usage = psutil.cpu_percent(interval=1)
    print(f"Current CPU Usage: {cpu_usage}%")
    if cpu_usage > 75:
        print("CPU usage is high! Creating a new VM...")
        create_vm()

monitor_and_scale()