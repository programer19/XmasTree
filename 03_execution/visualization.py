# Based on code from https://github.com/standupmaths/xmastree2020

import time
import sys

from animationFileReaders.CsvAnimationFileReader import CsvAnimationFileReader
from ledsAdapters.VisualLedsAdapter import VisualLedsAdapter
from ledsMapReaders.CsvLedsMapReader import CsvLedsMapReader
from ledsMapReaders.TxtLedsMapReader import TxtLedsMapReader


class Tree():
    def __init__(self, ledsAdapter):
        self._ledsAdapter = ledsAdapter

    def runRepeatedAnimation(self, animationFileReader, repeats = 0, frameRate = 60):
        repeatCounter = 0;
        while (repeatCounter < repeats) or (repeats == 0):
            animationFileReader.resetAnimation()
            self.runAnimation(animationFileReader, frameRate)
            repeatCounter += 1
        self.flushLeds()

    def runAnimation(self, animationFileReader, frameRate = 60):
        while True:
            frame = animationFileReader.getFrame()
            self._ledsAdapter.showFrame(frame)
            time.sleep(1/frameRate)
            if (not animationFileReader.nextFrame()): break

    def flushLeds(self):
        self._ledsAdapter.flush()


mapFileName = sys.argv[2]
mapFileNameExtension = mapFileName.split(".")[-1]
if (mapFileNameExtension == 'txt'):
    mapReader = TxtLedsMapReader(mapFileName)
elif (mapFileNameExtension == 'csv'):
    mapReader = CsvLedsMapReader(mapFileName)
else:
    print('Unknown LED map type')
    quit()

mapReader.normalize()

ledsAdapter = VisualLedsAdapter(500, mapReader, 800, 800)
tree = Tree(ledsAdapter)
tree.runRepeatedAnimation(CsvAnimationFileReader(sys.argv[1]), 0, 60)
