#F:\Documents\pycharm projects\lab11
from mindmap_leaf import MindMapLeaf
from mindmap_composite import MindMapComposite

def main():
    if __name__ == "__main__":
        # Root of the mindmap
        root = MindMapComposite( "The Phoberon System ", "oval" )

        characters = MindMapComposite( "Astronomical Objects", "oval" )
        characters.add( MindMapLeaf( "Phoberon 'Banba' - Yellow Star", "circle" ) )
        characters.add( MindMapLeaf("Morpheus 'Fódla' - Brown Dwarf", "circle" ) )
        characters.add( MindMapLeaf( "Phantasos 'Ériu' - Terrestrial Moon", "circle" ) )
        characters.add( MindMapLeaf( "Morrigan 'Badb' - Terrestrial Planet", "circle" ) )
        characters.add( MindMapLeaf( "Macha - Terrestrial Planet", "circle" ) )
        root.add( characters )

        plot_points = MindMapComposite( "Ériuan Continents", "square" )
        plot_points.add( MindMapLeaf( "Aithria - Northern Continent", "plain" ) )
        plot_points.add( MindMapLeaf( "Ignara - Southern Continent", "plain" ) )
        plot_points.add( MindMapLeaf( "Vóganar - Western Continent", "plain" ) )
        plot_points.add( MindMapLeaf( "Eryndor - Eastern Continent", "plain" ) )
        root.add( plot_points )

        themes = MindMapComposite( "Ériuan Times of Day", "cloud" )
        themes.add( MindMapLeaf( "Brightnight - Sky is lit by the general light of the distant Brown Dwarf with no Yellow Star in the sky 'slightly more light than the brightest full moon on Earth'", "plain" ) )
        themes.add( MindMapLeaf( "Highnoon - Sky shines brilliantly with the light of the Yellow Star mixing with that of the distant Brown Dwarf", "plain" ) )
        themes.add( MindMapLeaf( "Highday - The sky burns hot with the light of the nearby Brown Dwarf in the same sky as the Yellow Star", "plain" ) )
        themes.add( MindMapLeaf( "Lowday - The warmth of the nearby Brown Dwarf with no Yellow Star permeates the sky", "plain" ) )
        themes.add( MindMapLeaf( "Twilight - soft glowing light fills the sky from the Brown Dwarf and Yellow Star below the horizon to the north and south", "plain" ) )
        themes.add( MindMapLeaf( "Dimnight - faint glowing on the southern horizon from the Brown Dwarf and Yellow Star below the southern horizon", "plain" ) )
        themes.add(MindMapLeaf(
            "Day - Just the Yellow Sun in the sky",
            "plain"))
        themes.add(MindMapLeaf(
            "Night - Neither Yellow Sun or Brown Dwarf is in the sky",
            "plain"))
        root.add( themes )

        setting = MindMapComposite( "Day Cycles for The Continents from global time 00:00:00-32:00:00'32 hour day cycle'", "hexagon" )
        setting.add( MindMapLeaf( "Aithria - 8 hours night, 8 hours brightnight, 8 hours day, 8 hours highnoon, then back to 8 hours night", "plain" ) )
        setting.add( MindMapLeaf( "Ignara - 8 hours highday, 8 hours day, 8 hours lowday, 8 hours night, then back to 8 hours highday", "plain" ) )
        setting.add( MindMapLeaf( "Vóganar - 8 hours dimnight, 8 hours day, 8 hours twilight, 8 hours of night, then back to 8 hours dimnight", "plain" ) )
        setting.add( MindMapLeaf( "Eryndor - 8 hours dimnight, 8 hours brightnight, 8 hours twilight, 8 hours of highnoon, then back to 8 hours dimnight", "plain" ) )
        root.add( setting )

        conflicts = MindMapComposite( "Major differences between Ériu and Earth orbits", "bang" )
        conflicts.add( MindMapLeaf( "Ériu is tidally locked during the closer half of it's orbit around the Brown Dwarf", "plain" ) )
        conflicts.add( MindMapLeaf( "Ériu has time to fully rotate exactly once during the further half of it's orbit around the Brown Dwarf before resuming tidal locking", "plain" ) )
        conflicts.add( MindMapLeaf( "Ériu has 32 hour day cycles", "plain" ) )
        root.add( conflicts )

        dialogue = MindMapComposite( "Continental Climates and Topographies", "circle" )
        dialogue.add( MindMapLeaf( "Aithria - Snow covered , cold and Dark compared to a lot of the planet", "plain" ) )
        dialogue.add( MindMapLeaf( "Ignara - Hottest continent and lava pools can be found", "plain" ) )
        dialogue.add( MindMapLeaf( "Vóganar - cooler weather with a massive crator bay ", "plain" ) )
        dialogue.add(MindMapLeaf("Eryndor - Hotter weather in the valleys but cold windy mountains ranges and many canyons and rivers", "plain"))
        root.add( dialogue )

        stage_directions = MindMapComposite( "Places of interest", "square" )
        stage_directions.add( MindMapLeaf( "Crator Bay", "plain" ) )
        stage_directions.add( MindMapLeaf( "Duck island", "plain" ) )
        stage_directions.add( MindMapLeaf( "The southern Lava pools", "plain" ) )
        stage_directions.add( MindMapLeaf( "The Lost North", "plain" ) )
        root.add( stage_directions )

        print(root.display())


if __name__ == "__main__":
    main()