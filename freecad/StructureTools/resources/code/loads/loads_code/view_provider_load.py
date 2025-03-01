class ViewProviderDistLoad:
    def __init__(self, obj):
        obj.Proxy = self
    
    def getIcon(self):
        return """
               /* XPM */
static char * load_distributed_xpm[] = {
"32 32 8 1",
" 	c None",
".	c #1966FF",
"+	c #1866FF",
"@	c #1A66FF",
"#	c #1A67FF",
"$	c #1965FF",
"%	c #1A65FF",
"&	c #1967FF",
"                                ",
"                                ",
"                                ",
"  ...........................+  ",
"  ............................  ",
"  ............................  ",
"  ...@        #..@        @...  ",
"  ...$         ...        $...  ",
"  ...$         ...        $...  ",
"  ...$         ...        $...  ",
"  ...$         ...        $...  ",
"  ...$         ...        $...  ",
"  ...$         ...        $...  ",
"  ...$         ...        $...  ",
"  ...$         ...        $...  ",
"  ...$         ...        $...  ",
"  ...$         ...        $...  ",
"  ...$         ...        $...  ",
"  ...$         ...        $...  ",
"  ...$         ...        $...  ",
"  ...$         ...        $...  ",
"  %...        &..&        %..@  ",
"$......$    #.......    $......#",
" ......      ......$     ...... ",
" +.....      &.....      ...... ",
"  ....$       ....$      $....  ",
"  @...        ....        ....  ",
"  $..+        #..@        ...#  ",
"   ..          ...         ..   ",
"   ..          ..          ..   ",
"   $$           +          $.   ",
"                                "};
"""

class ViewProviderPontualLoad:
    def __init__(self, obj):
        obj.Proxy = self
    
    def getIcon(self):
        return """
               /* XPM */
static char * load_nodal_xpm[] = {
"32 32 4 1",
" 	c None",
".	c #FF1919",
"+	c #FF1A1A",
"@	c #FF1818",
"              ....              ",
"              ....              ",
"              ....              ",
"              ....              ",
"              ....              ",
"              ....              ",
"              ....              ",
"              ....              ",
"              ....              ",
"              ....              ",
"              ....              ",
"              ....              ",
"              ....              ",
"              ....              ",
"              ....              ",
"              ....              ",
"              ....              ",
"              ....              ",
"              ....              ",
"              ....              ",
"             .....              ",
"          ...........+          ",
"           ..........           ",
"           ..........           ",
"            ........            ",
"             ......             ",
"             .....+             ",
"              ....              ",
"              @...              ",
"               ..               ",
"               .@               ",
"                                "};
"""

#TODO corrigir com icone correto
class ViewProviderMomentumLoad:
    def __init__(self, obj):
        obj.Proxy = self
    
    def getIcon(self):
        return """
               /* XPM */
static char * load_nodal_xpm[] = {
"32 32 4 1",
" 	c None",
".	c #FF1919",
"+	c #FF1A1A",
"@	c #FF1818",
"              ....              ",
"              ....              ",
"              ....              ",
"              ....              ",
"              ....              ",
"              ....              ",
"              ....              ",
"              ....              ",
"              ....              ",
"              ....              ",
"              ....              ",
"              ....              ",
"              ....              ",
"              ....              ",
"              ....              ",
"              ....              ",
"              ....              ",
"              ....              ",
"              ....              ",
"              ....              ",
"             .....              ",
"          ...........+          ",
"           ..........           ",
"           ..........           ",
"            ........            ",
"             ......             ",
"             .....+             ",
"              ....              ",
"              @...              ",
"               ..               ",
"               .@               ",
"                                "};
"""
