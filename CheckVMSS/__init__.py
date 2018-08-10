import logging
import os
import json

import azure.functions as func
from azure.mgmt.compute import ComputeManagementClient
from azure.common.credentials import ServicePrincipalCredentials

credentials = ServicePrincipalCredentials(
        client_id=os.environ['AZURE_CLIENT_ID'],
        secret=os.environ['AZURE_CLIENT_SECRET'],
        tenant=os.environ['AZURE_TENANT_ID']
    )
compute_client = ComputeManagementClient(credentials, os.environ['AZURE_SUBSCRIPTION_ID'])

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    req_body = req.get_json()
    resourceGroup = req_body.get('resourceGroup')
    scaleSetName = req_body.get('scaleSetName')

    vmss_vms = compute_client.virtual_machine_scale_set_vms.list(resourceGroup, scaleSetName)

    vms = 0
    for vm in iter(vmss_vms):
        vms += 1

    return func.HttpResponse(str(vms))
