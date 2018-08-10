# Python example for Azure SDK

This simple example has a single python function - CheckVMSS - that will check the number of instances currently provisioned in a Virtual Machine Scale Set, and save that value to a CosmosDB table.

## Setup

1. Clone this repo
1. Make sure format matches [the virtual environment described here](https://github.com/Azure/azure-functions-python-worker/wiki/Create-Function-(CLI))
1. Run `pip install -r requirements.txt` when in the `functions-python-azure-sdk` folder
1. Run `func extensions sync` when in the `functions-python-azure-sdk` folder
1. Rename `local.settings.json.example` to `local.settings.json` and replace the placeholder values with real connection strings and service principal credentials
1. `func start` in the `functions-python-azure-sdk` directory and send an HTTPS request to the endpoint with the following format

```json
{
	"resourceGroup": "<resource group name>",
	"scaleSetName": "<VMSS name>"
}
```
