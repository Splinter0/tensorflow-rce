import json
import re
import argparse
import base64

def detect(path):
    print("Checking model", path)

    with open(path, "rb") as f:
        content = f.read().decode("latin-1")
    
    body = re.search("{(.*)}", content).group()
    model = json.loads(body)
    found = 0
    for layer in model["config"]["layers"]:
        if layer['class_name'] != "Lambda":
            continue
        
        print("\nFound Lambda layer with name \"" + layer["config"]["name"] + "\"")
        
        func = layer["config"]["function"]
        print("With body function:")
        print("Raw base64:")
        print(func[0])
        decoded = base64.b64decode(func[0]).decode("latin-1")
        print("Decoded:")
        print(decoded)
        found += 1
    
    print("\nFound {} Lambda functions".format(found))
        
        
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Detect malicious Tensorflow model")
    parser.add_argument("path", type=str, help="Path of the Tensorflow model")
    
    args = parser.parse_args()
    try:
        detect(args.path)
    
    except Exception as e:
        print("Failed to analyse for Lambda layers, don't give up!")
        print(e)