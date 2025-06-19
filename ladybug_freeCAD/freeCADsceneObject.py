
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
import Part
import FreeCAD as App

class LadyBugScene(BaseObjectClass):
	def __init__(self, obj):
		super().__init__(obj, "LadyBugScene")
		self.initLadyBugScene()
				
	def initLadyBugScene(self):
		print(f"Init LadyBugScene")

	def addLadyBugSceneObject(self, parent):
        # Add new FC object to parent
        print(f"Add LadyBug Scene Object")
        self.obj = parent.newObject("Part::PythonFeature","LadyBugScene")

	def execute(self, fp):
        self.createGeometry(fp)
        
    def createGeometry(self, fp):
        currPlacement = fp.Placement
        #fp.Shape = Part.Shape()
        # Just show a Box for Now
        fp.Shape = Part.makeBox(10, 10, 10)

    def onChanged(self, fp, prop):
        # print(fp.Label+" State : "+str(fp.State)+" prop : "+prop)
        if "Restore" in fp.State:
            return
            
class baseObjectClass:
    def __init__(self, obj, objType):
        """Init"""
        self.Type = objType
        obj.Proxy = self
        obj.Proxy.Type = objType
    
    def __getstate__(self):
        """
        When saving the document this object gets stored using Python's
		json module.
		Since we have some un-serializable parts here -- the Coin stuff --
		we must define this method
		to return a tuple of all serializable objects or None.
        """
        if hasattr(self, "Type"):  # If not saved just return
            return {"type": self.Type}
        else:
            	pass

    def dumps(self):               # Post python 3.11
        """
        When saving the document this object gets stored using Python's
		json module.
		Since we have some un-serializable parts here -- the Coin stuff --
		we must define this method
		to return a tuple of all serializable objects or None.
        """
        if hasattr(self, "Type"):  # If not saved just return
            return {"type": self.Type}
        else:
            	pass

    def __setstate__(self, arg):
        """
        When restoring the serialized object from document we have the
		chance to set some internals here.
		Since no data were serialized nothing needs to be done here.
        """
		# Handle bug in FreeCAD 0.21.2 handling of json
		#print(f"setstate : arg {arg} type {type(arg)}")
        if arg is not None and arg != {}:
            if 'type' in arg:
                self.Type = arg["type"]
            else: #elif 'Type' in arg:
                self.Type = arg["Type"]
            #print(self.Type)

    def loads(self, arg):       # Post python 3.11
        """
        When restoring the serialized object from document we have the
		chance to set some internals here.
		Since no data were serialized nothing needs to be done here.
        """
		# Handle bug in FreeCAD 0.21.2 handling of json
		#print(f"setstate : arg {arg} type {type(arg)}")
        if arg is not None and arg != {}:
            if 'type' in arg:
                self.Type = arg["type"]
            else: #elif 'Type' in arg:
                self.Type = arg["Type"]
            #print(self.Type)

# use general ViewProvider if poss
class ViewProvider():
    def __init__(self, obj):
        #super().__init__(obj)
        """Set this object to the proxy object of the actual view provider"""
        obj.Proxy = self

    def updateData(self, fp, prop):
        """If a property of the handled feature has changed we have the chance to handle this here"""
        # print("updateData")
        pass

    def setTransparency(self, obj, value):
        obj.ViewObject.Transparency = value

    def getDisplayModes(self, obj):
        """Return a list of display modes."""
        # print("getDisplayModes")
        modes = []
        modes.append("Shaded")
        modes.append("Wireframe")
        modes.append("Points")
        return modes

    def getDefaultDisplayMode(self):
        """Return the name of the default display mode. It must be defined in getDisplayModes."""
        return "Shaded"

    def setDisplayMode(self, mode):
        """Map the display mode defined in attach with those defined in getDisplayModes.\
               Since they have the same names nothing needs to be done. This method is optional"""
        return mode

    def onChanged(self, vp, prop):
        """Here we can do something when a single property got changed"""
        # if hasattr(vp,'Name') :
        #   print("View Provider : "+vp.Name+" State : "+str(vp.State)+" prop : "+prop)
        # else :
        #   print("View Provider : prop : "+prop)
        # GDMLShared.trace("Change property: " + str(prop) + "\n")
        # if prop == "Color":
        #    c = vp.getPropertyByName("Color")
        #    self.color.rgb.setValue(c[0],c[1],c[2])

    def getIcon(self):
        """Return the icon in XPM format which will appear in the tree view. This method is\
               optional and if not defined a default icon is shown."""
        return """
            /* XPM */
            static const char * ViewProviderBox_xpm[] = {
            "16 16 6 1",
            "   c None",
            ".  c #141010",
            "+  c #615BD2",
            "@  c #C39D55",
            "#  c #000000",
            "$  c #57C355",
            "        ........",
            "   ......++..+..",
            "   .@@@@.++..++.",
            "   .@@@@.++..++.",
            "   .@@  .++++++.",
            "  ..@@  .++..++.",
            "###@@@@ .++..++.",
            "##$.@@$#.++++++.",
            "#$#$.$$$........",
            "#$$#######      ",
            "#$$#$$$$$#      ",
            "#$$#$$$$$#      ",
            "#$$#$$$$$#      ",
            " #$#$$$$$#      ",
            "  ##$$$$$#      ",
            "   #######      "};
            """

    # In ViewProvidor ????
    #def __getstate__(self):
    #    """When saving the document this object gets stored using Python's json module.\
    #           Since we have some un-serializable parts here -- the Coin stuff -- we must define this method\
    #           to return a tuple of all serializable objects or None."""
    #    return None

    #def __setstate__(self, state):
    #    """When restoring the serialized object from document we have the chance to set some internals here.\
    #           Since no data were serialized nothing needs to be done here."""
    #    return None
