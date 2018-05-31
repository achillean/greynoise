# Greynoise for Python

The **greynoise** Python package provides a library and command-line interface for interacting with the [Greynoise API](https://www.greynoise.io)

## Getting Started

The library is fairly barebones at the moment but this is how to use it from Python:

```python
from greynoise import Greynoise

# Connect to the API
api = Greynoise('API Key')

# Get a list of background noise IPs
noise_ips = api.noise_bulk()
```

Or you can access the list of IPs via the command-line tool called **greynoise**:

```
$ greynoise init API_Key
Successfully initialized
$ greynoise noise bulk
57.51.98.42
```
