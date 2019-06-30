import os
import sys
import json
import io

here = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(here, "vendored"))
# now it is allowed to add a non-std package
from pycatj import pycatj


def pycatjify(request):
    # default data value
    data = json.loads(
        '{"data":"test_value","somenumber":123,"a_dict":{"asd":"123","qwe":[1,2,3],"nested_dict":{"das":31,"qwe":"asd"}}}'
    )
    # default root value
    root = "my_dict"
    # if request object exists and the keys `data` and `root` are inside of it
    # rewrite the default values for `data` and `root`
    print("Incoming request body: ", request.get_data())
    rj = request.get_json()
    if rj:
        data = rj
        if "pycatj_data" in rj:
            print("pycatj_data key is found in the request body")
            data = rj["pycatj_data"]
        if "root" in rj:
            print("root key is found in the request body")
            root = rj["root"]

    result = io.StringIO()
    pycatj.process_dict(data, root, result)
    return json.dumps({"data": result.getvalue()})


if __name__ == "__main__":
    print(pycatjify(None))
