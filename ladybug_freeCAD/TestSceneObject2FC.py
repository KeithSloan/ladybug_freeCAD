# ***************************************************************************
# *                                                                         *
# *   Copyright (c) 2025 Keith Sloan <ipad2@sloan-home.co.uk>               *
# *                                                                         *
# *                                                                         *
# *   This program is free software; you can redistribute it and/or modify  *
# *   it under the terms of the GNU Lesser General Public License (LGPL)    *
# *   as published by the Free Software Foundation; either version 2 of     *
# *   the License, or (at your option) any later version.                   *
# *   for detail see the LICENCE text file.                                 *
# *                                                                         *
# *   This program is distributed in the hope that it will be useful,       *
# *   but WITHOUT ANY WARRANTY; without even the implied warranty of        *
# *   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the         *
# *   GNU Library General Public License for more details.                  *
# *                                                                         *
# *   You should have received a copy of the GNU Library General Public     *
# *   License along with this program; if not, write to the Free Software   *
# *   Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  *
# *   USA                                                                   *
# *                                                                         *
# *   Acknowledgements :                                                    *
# *                                                                         *
# *                                                                         *
# *                                                                         *
# *                                                                         *
# *                                                                         *
############################################################################*


## Test function

from freeCADsceneObject import LadyBugScene

scene = LadyBugScene()
scene.add2DocLadyBugSceneObject()

### ??
vector = (10,10)

from bakedisplay import bake_display_vector2d
from bakegeometry import bake_vector2d


bake_display_vector2d(vector, z=0, layer_name=None, attributes=None)
bake_vector2d(vector, z=0, layer_name=None, attributes=None)


