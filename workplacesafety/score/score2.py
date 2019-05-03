from azureml.contrib.services.aml_request import AMLRequest, rawhttp

def init():
    pass

@rawhttp
def run(request):
    output = {}

    output['detection_boxes'] = [
        [0.632853319644928,
        0.8427513837814331,
        0.6888669610023499,
        0.8872339725494385],
        [0.6196154856681824,
        0.8764234185218811,
        0.6814213275909424,
        0.9090630412101746],
        [0.6299444842338562,
        0.9056463837623596,
        0.6937898278236389,
        0.9416812062263489]]
    output['detection_classes'] = [1, 1, 16]
    output['detection_scores'] = [0.98, 0.98, 0.98]

    return output