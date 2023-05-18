from svgpathtools import svg2paths

def main():
    x =  bezierToPoints('Andy.svg')
    print(len(x))

def bezierToPoints(filePath):
    # Convert SVG file to paths
    output = []
    paths, _ = svg2paths(filePath)

    path = paths[0]
    samples = len(path)
    # Extract coordinates from paths
    for i in range(samples):
        t = i / (samples + 1) 
        point = path.point(t) 
        x = int(point.real)
        y = int(point.imag)
        output.append((x,y))
    return output

if __name__ == "__main__":
    main()
