/*

Copyright 2016 kennytm

Licensed under the Apache License, Version 2.0 (the "License"); you may not use
this file except in compliance with the License. You may obtain a copy of the
License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software distributed
under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR
CONDITIONS OF ANY KIND, either express or implied. See the License for the
specific language governing permissions and limitations under the License.

*/

// Generate the image with: povray -W851 -H315 +A +AM2 cover.pov

#version 3.7;
#include "colors.inc"
#include "textures.inc"
#include "finish.inc"

global_settings {
    assumed_gamma 2.2
}

camera {
    location <0, 0, -13>
    look_at 0
    right x*851/315
}

light_source {
    <12, 0, -21> color White
    area_light 10*x, y, 5, 2
}

light_source {
    <-12, 3, 0> color White shadowless
}

sky_sphere {
    pigment { Clouds }
}

#declare CHARS_COUNT = 15;

#declare CHARS = array [CHARS_COUNT] {
    "H", "O", "N", "G", " ",
    "K", "O", "N", "G", " ",
    "A", "R", "R", "A", "Y"
};

#declare WT = 0.05; // wireframe thickness

#for (I, 0, CHARS_COUNT-1)
    object {
        union {
            text {
                internal 2 CHARS[I] 1, 0
                translate <-0.375, -0.375, -0.5>
                scale <2, 2, 0.25>
                texture {
                    pigment { Yellow }
                    finish { Phong_Glossy }
                }
            }
            text {
                internal 3 concat("a[", str(I, 1, 0), "]") 0.1, 0
                scale 0.5
                translate <-0.5, 1.1, -0.5>
                texture {
                    pigment { color Red }
                    finish { Phong_Glossy }
                }
            }
            difference {
                box { <-1, -1, -0.5>, <1, 1, 0.5> }
                box { <-1 + WT, -1 + WT, -0.5 - WT>, <1 - WT, 1 - WT, 0.5 + WT> }
                box { <-1 + WT, -1 - WT, -0.5 + WT>, <1 - WT, 1 + WT, 0.5 - WT> }
                box { <-1 - WT, -1 + WT, -0.5 + WT>, <1 + WT, 1 - WT, 0.5 - WT> }
                texture {
                    pigment { Gray }
                    finish { Dull }
                }
            }
        }
        translate (I - CHARS_COUNT/2)*2.5*x
        rotate -28*y
        translate 13*x
    }
#end


