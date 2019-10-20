#!/usr/bin/env python

from __future__ import print_function
import argparse

try:
	from cv2 import imwrite
	from ar_markers.marker import HammingMarker
	from ar_markers import __version__
except ImportError:
	raise Exception('Error: OpenCv is not installed')


def gen(mid):
	path = './marker_{}.png'
	marker = HammingMarker(mid)
	imwrite(path.format(marker.id), marker.generate_image())
	print("Generated Marker with ID {}".format(marker.id))
	print('Done!')
