#!/usr/bin/env python3
#
#===============================================================================
#
# Copyright 2016 kennytm
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may not
# use this file except in compliance with the License. You may obtain a copy of
# the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations under
# the License.
#
#===============================================================================
#
# See http://gph.is/1r3jV2y for the result :)

'''requirements.txt

numpy==1.11.0
Pillow==3.2.0

'''

from PIL import Image, ImageDraw, ImageFont, ImageSequence
import os
import numpy
import sys

一日最衰都係 = {
    '佔中': 9.28,
    '拉布': 9,
    '港獨': 8,

    '三跑': 0.3,
    '中共': 0.1,
    '之鋒': 0.1,
    '公安': 0.1,
    '六八九': 0.689,
    '共產黨': 0.2,
    '包容': 0.1,
    '北京': 0.1,
    '十年': 1.0,
    '和理非': 0.4,
    '地產商': 0.1,
    '基本法': 0.1,
    '大陸': 0.1,
    '左膠': 0.5,
    '廢青': 0.1,
    '廿三條': 0.23,
    '掟磚': 0.2,
    '支那': 0.1,
    '政府': 0.2,
    '日本': 0.1,
    '暴亂': 2.8,
    '暴徒': 0.2,
    '有線': 0.1,
    '本土': 0.5,
    '樹根': 0.1,
    '毓民': 0.1,
    '民主黨': 0.2,
    '民建聯': 0.2,
    '法西斯': 0.1,
    '泛民': 0.5,
    '港豬': 0.5,
    '無綫': 0.1,
    '熱狗': 0.2,
    '美國': 0.1,
    '美帝': 0.1,
    '自由行': 0.1,
    '英國': 0.1,
    '菲律賓': 0.1,
    '蝗蟲': 0.1,
    '踢篋': 0.1,
    '長毛': 0.1,
    '陳雲': 0.1,
    '雙非': 0.2,
    '驅蝗': 1.0,
    '高鐵': 0.3,
    '鳩嗚': 0.1,
    '黑警': 0.4,
}

FRAMES_COUNT = 500
MEMORY_ITERATIONS = 5
IMAGE_SIZE = (256, 256)
TITLE_FONT = ('/Library/Fonts/Hanzipen.ttc', 1)
MESSAGE_FONT = ('/Library/Fonts/WeibeiTC-Bold.otf', 0)

reasons, weights = zip(*一日最衰都係.items())
weights = numpy.array(weights) / sum(weights)

last_chosen_reasons = set()
image = Image.new('RGB', IMAGE_SIZE, '#ffffff')
canvas = ImageDraw.Draw(image)

if False:
    # test to ensure every character exists in the selected font.
    repotoire = sorted(set(''.join(reasons)))
    repotoire = '\n'.join(''.join(repotoire[i:i+12]) for i in range(0, len(repotoire), 12))
    message_font = ImageFont.truetype(font=MESSAGE_FONT[0], size=21, index=MESSAGE_FONT[1])
    canvas.text((0, 0), repotoire, fill='#000000', font=message_font)
    image.show()
    sys.exit(0)

title_font = ImageFont.truetype(font=TITLE_FONT[0], size=36, index=TITLE_FONT[1])
canvas.text((20, 47), '一日最衰都係', fill='#000000', font=title_font)

message_font = ImageFont.truetype(font=MESSAGE_FONT[0], size=80, index=MESSAGE_FONT[1])
for i in range(FRAMES_COUNT):
    # randomly choose a reason, but don't make the same phrase repeat too often.
    for reason in numpy.random.choice(reasons, FRAMES_COUNT, p=weights):
        if reason not in last_chosen_reasons:
            if len(last_chosen_reasons) > MEMORY_ITERATIONS:
                last_chosen_reasons.pop()
            last_chosen_reasons.add(reason)
            break

    # reason is chosen, generate image.
    canvas.rectangle((0, 97, 256, 256), fill='#ffffff')
    x = 130 - 40*len(reason)
    canvas.text((x, 97), reason , fill='#ff0000', font=message_font)

    # save image
    image.save('out/frame{:03d}.png'.format(i))

# Run:
#
# convert -delay 2 -loop 0 out/frame*.png output.gif
#
# to construct the gif.
