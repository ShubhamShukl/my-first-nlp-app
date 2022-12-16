import paralleldots
# Setting your API key
paralleldots.set_api_key('bPFImC7ClpuuQhiNxLiqDCxTTqYHXKS3vraNnpEbnMc')

def ner(text):
    ner = paralleldots.ner(text)
    return ner
