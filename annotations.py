# python3
#
# Copyright 2019 The TensorFlow Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from PIL import Image
from PIL import ImageDraw


def _round_up(value, n):

  return n * ((value + (n - 1)) // n)


def _round_buffer_dims(dims):
  
  width, height = dims
  return _round_up(width, 32), _round_up(height, 16)


class Annotator:
  """Utility for managing annotations on the camera preview."""

  def __init__(self, camera, default_color=None):
    """Initializes Annotator parameters.
    Args:
      camera: picamera.PiCamera camera object to overlay on top of.
      default_color: PIL.ImageColor (with alpha) default for the drawn content.
    """
    self._camera = camera
    self._dims = camera.resolution
    self._buffer_dims = _round_buffer_dims(self._dims)
    self._buffer = Image.new('RGBA', self._buffer_dims)
    self._overlay = None
    self._draw = ImageDraw.Draw(self._buffer)
    self._default_color = default_color or (0xFF, 0, 0, 0xFF)

  def update(self):
    """Draws any changes to the image buffer onto the overlay."""
    temp_overlay = self._camera.add_overlay(
        self._buffer.tobytes(), format='rgba', layer=3, size=self._buffer_dims)
    if self._overlay is not None:
      self._camera.remove_overlay(self._overlay)
    self._overlay = temp_overlay
    self._overlay.update(self._buffer.tobytes())

  def clear(self):
    """Clears the contents of the overlay, leaving only the plain background."""
    self._draw.rectangle((0, 0) + self._dims, fill=(0, 0, 0, 0x00))

  def bounding_box(self, rect, outline=None, fill=None):
    outline = outline or self._default_color
    self._draw.rectangle(rect, fill=fill, outline=outline)

  def text(self, location, text, color=None):
    color = color or self._default_color
    self._draw.text(location, text, fill=color)
