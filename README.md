# Python3 Client for overfitted.io's API

This is a small Python3 client which permits fast interaction with services hosted on overfitted.io (e.g., OCR, document parsing, etc.).
It implements all the REST-based communication via the `requests` package and employs parallel connections via `ThreadPoolExecutor`.

The module automatically queries overfitted.io for a list of services and their specifications (parameters, endpoint, etc.); this leaves space for modifications or additions of new services on the server's end without requiring changes in the python client.


## Installation

The fastest installation method is through **pip3** as follows:
```
pip3 install git+https://github.com/overfitted-io/python-api-client.git
```

To **uninstall**:
```
pip3 uninstall overfitted-io-client
```

## Usage

1. Define the environment variable `OVERFITTED_IO_API_KEY` and add your **API key**; if you don't have one, see the [Get Started](https://overfitted.io/get-started/) section.
```
# TODO: replace this
export OVERFITTED_IO_API_KEY=123456789abcdef
``` 

2. Import the module and test the connection
```python
import overfitted_io_client as oc

# should display your account information and API key
print(oc.get_account_info([{ 'api_key' : oc.config.get_api_key() }]))
```


3. If previous command succeeded, you can use the available services.
E.g., for performing OCR on a given image:

```python
import overfitted_io_client as oc

img = open('my_img.jpg', 'rb')

result = oc.query_service('glyph', inputs = [{ 'img' : img, 'lang' : 'en-ma', 'api_key' : oc.config.get_api_key()}])

# [({ "text": "Some random text found within the image", ...}, 200)]
print(result)
```

**Explanation:** the `query_service()` method is used to access all hosted services; in this example, OCR is desired, therefore the OCR service (named *glyph*) is called; the `inputs` parameter takes a list of 1 element (1 task) in this scenario: to run OCR on the image provided as `img` using the language code `en-ma` (English Modern Antiqua) and as `api_key` the key you supplied in the environment variable at the previous step. the `result` is also a list which matches the order of the `inputs` and, in this case, contains 1 element (1 tuple) with the format `(json_response, response_status_code)`.

For a list of parameters names (inside the `inputs` variable), check each service's documentation on [overfitted.io](https://overfitted.io)


**Note:** providing a list of input images to the `query_service()` function enables the use of multiple parallel connections which facilitates better throughput.


## Problems / Bugs

Please open a GitHub issue if there are any problems with this module.
Also, take into account that the services on overfitted.io are in active development; implementing feedback from collaborators can introduce new parameters or modifications in the response's format.
