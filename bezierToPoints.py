from svgpathtools import svg2paths

def main():
    x =  bezierToPoints('Andy.svg')
    print(len(x))

'''
load the SVG file and extract the paths
note extra paths will be added but,
line connects the end of one path to the start of the next

NOTE: While I did take this code from Chat GPT,
I modified it so that it will output all of the curves
Increase the quality by increaseing the interpolation points
and translating the image so that it fits on the canvas
'''
def bezierToPoints(filePath, quality=1, translate = (400,300)):
    output = []
    paths, _ = svg2paths(filePath)
    # paths are the bezier curves
    for path in paths:
        # this interpolates baised on the quality parameter
        samples = quality * len(path) 
        for i in range(samples):
            t = i / (samples + 1) 
            point = path.point(t) 
            x = int(point.real- translate[0])
            y = int(point.imag - translate[1])
            output.append((x,y))
    return output
if __name__ == "__main__":
    main()
