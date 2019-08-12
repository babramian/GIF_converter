import imageio
import os

video = os.path.abspath(input())

def gifConverter(inputPath, targetFormat):
    outputPath = os.path.splitext(inputPath)[0] + targetFormat

    print(f'converting {inputPath}\n to {outputPath}')

    reader = imageio.get_reader(inputPath)
    fps = 15

    writer = imageio.get_writer(outputPath, fps=fps)

    for frames in reader:
        writer.append_data(frames)
    
    print('Finished.')
    writer.close()

gifConverter(video, '.gif')