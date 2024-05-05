# checkcif_api
Webscraping Api for using IUCr checkcif tool (https://checkcif.iucr.org/).

You will need the 'requests' package to process HTTP requests. Install in your environment:
'conda install requests'
or:
'pip install requests'

Use checkcif_api.py for a single checkcif, use mul_checkcif.py for processing an entire directory (but both scripts have to be in the same place)

WARNING:
This script ignores SSL encryption keys, as IUCr checkcif doesn't provide them
