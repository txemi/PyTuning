# -*- coding: utf-8 -*-
"""
Created on Tue May 26 11:15:40 2015

@author: mark
"""
from __future__ import print_function, division
import sympy as sp

all = [ "cent", "perfect_fifth", "perfect_fourth", "octave", "perfect_major_third", \
       "quarter_comma", "five_limit_constructors", "edo12_constructors", \
       "lucy_construtors", "all_constructors", "interval_catalog"]

# Ratio Constants

cent                  = sp.Integer(2)**sp.Rational(1,1200)
perfect_fifth         = sp.Integer(3)/sp.Integer(2)
perfect_fourth        = sp.Integer(4)/sp.Integer(3)
octave                = sp.Integer(2)
perfect_major_third   = sp.Integer(5)/sp.Integer(4)
syntonic_comma        = sp.Rational(81,80)
quarter_comma         = sp.sqrt(sp.sqrt(syntonic_comma))

# Scale definition constants

five_limit_constructors = [
    (sp.Rational(16,15), "s"),
    (sp.Rational(10,9),  "t"),
    (sp.Rational(9,8),   "T"),
]

edo12_constructors = [
    (sp.core.power.Pow(2,sp.Rational(2,12)), "T"),
    (sp.core.power.Pow(2,sp.Rational(1,12)), "s"),
]

lucy_L = sp.root(2,2*sp.pi)
lucy_s = sp.sqrt(2/lucy_L**5)

lucy_construtors = [
    (lucy_L,               "L"  ),
    (lucy_s,               "s"  ),
    (sp.Integer(1)/lucy_L, "1/L"),
    (sp.Integer(1)/lucy_s, "1/s"),
    
]

interval_catalog = [
    ("Unison" , sp.Integer(1)),
    ("Ragisma" , sp.Rational(4375, 4374)),
    ("Breedsma", sp.Rational(2401, 2400)),
    ("Cent", sp.Integer(2) ** sp.Rational(1,1200)),
    ("Millioctave", sp.Integer(2) ** sp.Rational(1,1000)),
    ("Schisma", sp.Rational(32805, 32768)),
    ("Savart",  sp.Integer(10) ** sp.Rational(1,1000)),
    ("Septimal Kleisma", sp.Rational(225, 224)),
    ("Kleisma", sp.Rational(15625, 15552)),
    ("Semicomma", sp.Rational(2109375, 2097152)),
    ("Sixteenth Tone",  sp.Integer(2) ** sp.Rational(1,96)),
    ("Orwell Comma", sp.Rational(1728, 1715)),
    ("Hundred-twenty-ninth Harmonic", sp.Rational(129, 128)),
    ("Small Septimal Semicomma", sp.Rational(126, 125)),
    ("Unidecimal Seconds Comma", sp.Rational(121, 120)),
    ("Diaschisma", sp.Rational(2048, 2025)),
    ("Syntonic Comma", sp.Rational(81, 80)),
    ("Holdrian Comma",  sp.Integer(2) ** sp.Rational(1,53)),
    ("Pythagorean Comma", sp.Rational(531441, 524288)),
    ("Eighth Tone",  sp.Integer(2) ** sp.Rational(1,48)),
    ("Sixty-fifth Harmonic", sp.Rational(65, 64)),
    ("Septimal Comma", sp.Rational(64, 63)),
    ("Ptolemy's Enharmonic", sp.Rational(56, 55)),
    ("Sixth Tone",  sp.Integer(2) ** sp.Rational(1,36)),
    ("Septimal Sixth Tone",  sp.Rational(50, 49)),
    ("Inferior Quarter Tone",  sp.Rational(46, 45)),
    ("Undecimal Diesis",  sp.Rational(45, 44)),
    ("Fifth Tone",  sp.Integer(2) ** sp.Rational(1,30)),
    ("Enharmonic Diesis",  sp.Rational(128, 125)),
    ("Lesser 41-limit Fifth Tone",  sp.Rational(42, 41)),
    ("Greater 41-limit Fifth Tone",  sp.Rational(41, 40)),
    ("Septimal Quarter Tone",  sp.Rational(36, 35)),
    ("Just Quarter Tone",  sp.Rational(246, 239)),
    ("Equal-tempered Quarter Tone",  sp.Integer(2) ** sp.Rational(1,24)),
    ("Lesser 17-limit Quarter Tone",  sp.Rational(35, 34)),
    ("Harrison's Comma",  sp.Rational(59049, 57344)),
    ("Greater 17-limit Quarter Tone",  sp.Rational(34, 33)),
    ("Thrty-third Harmonic",  sp.Rational(33, 32)),
    ("Inferior Quarter Tone",  sp.Rational(32, 31)),
    ("Five-hundred-twenty-ninth harmonic",  sp.Rational(529, 512)),
    ("Greater Quarter Tone",  sp.Rational(31, 30)),
    ("Lesser 29-limit Quarter Tone",  sp.Rational(30, 29)),
    ("Greater 29-limit Quarter Tone",  sp.Rational(29, 28)),
    ("Septimal Minor Second",  sp.Rational(28, 27)),
    ("Beta Scale Step",  sp.Rational(3, 2) ** sp.Rational(1, 11)),
    ("Chromatic Diesis",  sp.Rational(27, 26)),
    ("One-hundred-thirty-third Harmonic",  sp.Rational(133, 128)),
    ("Third Tone",  sp.Integer(2) ** sp.Rational(1,18)),
    ("Tridecimal Third Tone",  sp.Rational(26, 25)),
    ("Just Chromatic Semitone",  sp.Rational(25, 24)),
    ("Lesser 23-limit Semitone",  sp.Rational(24, 23)),
    ("Greater 23-limit Semitone",  sp.Rational(23, 22)),
    ("Alpha Scale Step",  sp.Rational(3, 2) ** sp.Rational(1, 9)),
    ("Sixty-seventh Harmonic",  sp.Rational(67, 64)),
    ("Hard Semitone",  sp.Rational(22, 21)),
    ("Septimal Chromatic Semitone",  sp.Rational(21, 20)),
    ("Novendecimal Augmented Unison",  sp.Rational(20, 19)),
    ("Pythagorean Minor Second",  sp.Rational(256, 243)),
    ("Greater Chromatic Semitone",  sp.Rational(135, 128)),
    ("Novendecimal Minor Second",  sp.Rational(19, 18)),
    ("121st Subharmonic",  sp.Rational(128, 121)),
    ("Just Minor Semitone",  sp.Rational(18, 17)),
    ("Equal-tempered Minor Second",  sp.Integer(2) ** sp.Rational(1,12)),
    ("Minor Diatonic Semitone",  sp.Rational(17, 16)),
    ("Just Minor Second",  sp.Rational(16, 15)),
    ("Pythagorean Major Semitone",  sp.Rational(2187, 2048)),
    ("Secor",  sp.Rational(18, 5) ** sp.Rational(1, 19)),
    ("Septimal Diatonic Semitone",  sp.Rational(15, 14)),
    ("Lesser Tridecimal 2/3-tone",  sp.Rational(14, 13)),
    ("Sixty-ninth Harmonic",  sp.Rational(69, 64)),
    ("Semitone maximus",  sp.Rational(27, 25)),
    ("Two-third Tone",  sp.Integer(2) ** sp.Rational(1,19)),
    ("Greater Tridecimal 2/3-tone",  sp.Rational(13, 12)),
    ("Equal-tempered Neutral Second",  sp.Integer(2) ** sp.Rational(3,24)),
    ("3/4-tone",  sp.Rational(12,11)),
    ("Thirty-fifth Harmonic",  sp.Rational(35, 32)),
    ("Grave Whole Tone",  sp.Rational(800, 729)),
    ("Ptolemy's second",  sp.Rational(11, 10)),
    ("Seventy-first Harmonic",  sp.Rational(71, 64)),
    ("Pythagorean Diminished Third",  sp.Rational(65536, 9049)),
    ("Small Just Whole Tone",  sp.Rational(10, 9)),
    ("Equal-tempered Major Second",  sp.Integer(2) ** sp.Rational(2,12)),
    ("Pythagorean Major Second",  sp.Rational(9, 8)),
    ("Hundred-forty-fifth Harmonic",  sp.Rational(145, 128)),
    ("Just Diminished Third",  sp.Rational(256, 225)),
    ("Seventy-third Harmonic",  sp.Rational(73, 64)),
    ("Septimal Major Second",  sp.Rational(8, 7)),
    ("Thirty-seventh Harmonic",  sp.Rational(37, 32)),
    ("Semi-augmented Whole Tone",  sp.Rational(125, 108)),
    ("55th Subharmonic",  sp.Rational(64, 55)),
    ("Two-hundred-ninety-ninth Harmonic",  sp.Rational(299, 256)),
    ("Septimal Minor Third",  sp.Rational(7, 6)),
    ("Just Augmented Second",  sp.Rational(75, 64)),
    ("Pythagorean Minor Third",  sp.Rational(32, 27)),
    ("19th Harmonic",  sp.Rational(19, 16)),
    ("Equal-tempered Minor Third",  sp.Integer(2) ** sp.Rational(3,12)),
    ("Quasi-equal-tempered Minor Third",  sp.Rational(25, 21)),
    ("Quarter-comma Meantone Minor Third",  sp.Rational(8,5)/(sp.Rational(81, 80)**sp.Rational(1,4))),
    ("Alpha Scale Minor Third",  sp.Rational(3, 2) ** sp.Rational(4, 9)),
    ("Just Minor Third",  sp.Rational(6, 5)),
    ("Pythagorean Augmented Second",  sp.Rational(19683, 16384)),
    ("Seventy-seventh Harmonic",  sp.Rational(77, 64)),
    ("Superminor Third",  sp.Rational(17, 14)),
    ("Acute Minor Third",  sp.Rational(243, 200)),
    ("Thirty-ninth Harmonic",  sp.Rational(39, 32)),
    ("105th Subharmonic",  sp.Rational(128, 105)),
    ("Undecimal Neutral Third",  sp.Rational(11, 9)),
    ("Equal-tempered Neutral Third",  sp.Integer(2) ** sp.Rational(7, 24)),
    ("Zalzal's Wosta",  sp.Rational(27, 22)),
    ("Tridecimal Neutral Third",  sp.Rational(16, 13)),
    ("Seventy-ninth Harmonic",  sp.Rational(79, 64)),
    ("Grave Major Third",  sp.Rational(100, 81)),
    ("Pythagorean Diminished Fourth",  sp.Rational(8192, 6561)),
    ("Just Major Third",  sp.Rational(5, 4)),
    ("One-hundred-sixty-first Harmonic",  sp.Rational(161, 128)),
    ("Equal-tempered Major Third",  sp.Integer(2) ** sp.Rational(4, 12)),
    ("Three-hundred-twenty-third Harmonic",  sp.Rational(323, 256)),
    ("Pythagorean Major Third",  sp.Rational(81, 64)),
    ("Undecimal Diminished Fourth",  sp.Rational(14, 11)),
    ("Just Diminished Fourth",  sp.Rational(32, 25)),
    ("Forty-first Harmonic",  sp.Rational(41, 32)),
    ("Septimal Major Third",  sp.Rational(9, 7)),
    ("99th Subharmonic",  sp.Rational(128, 99)),
    ("Eighty-third Harmonic",  sp.Rational(83, 64)),
    ("Tridecimal Major Third ",  sp.Rational(13, 10)),
    ("Just Augmented Third ",  sp.Rational(125, 96)),
    ("49th Subharmonic",  sp.Rational(64, 49)),
    ("21st Harmonic",  sp.Rational(21, 16)),
    ("Wide Augmented Third",  sp.Rational(675, 512)),
    ("85th Harmonic",  sp.Rational(85, 64)),
    ("Perfect Fourth",  sp.Rational(4, 3)),
    ("Equal-tempered Perfect Fourth",  sp.Integer(2) ** sp.Rational(5, 12)),
    ("One-hundred-seventy-first Harmonic",  sp.Rational(171, 128)),
    ("Beta Scale Perfect Fourth",  sp.Rational(3, 2) ** sp.Rational(8, 11)),
    ("Forty-third Harmonic",  sp.Rational(43, 32)),
    ("5-limit Wolf Fourth",  sp.Rational(27, 20)),
    ("Pythagorean Augmented Third",  sp.Rational(177147, 131072)),
    ("Eighty-seventh Harmonic",  sp.Rational(87, 64)),
    ("Eleventh Harmonic",  sp.Rational(11, 8)),
    ("Just Augmented Fourth",  sp.Rational(25, 18)),
    ("Eighty-ninth Harmonic",  sp.Rational(89, 64)),
    ("Lesser Septimal Tritone",  sp.Rational(7, 5)),
    ("Pythagorean Diminished Fifth",  sp.Rational(1024, 729)),
    ("Just Augmented Fourth",  sp.Rational(45, 32)),
    ("Three-hundred-sixty-first Harmonic",  sp.Rational(361, 256)),
    ("Equal-tempered Tritone",  sp.Integer(2) ** sp.Rational(6, 12)),
    ("Ninety-first Harmonic",  sp.Rational(91, 64)),
    ("Just Tritone",  sp.Rational(64, 45)),
    ("Pythagorean Tritone",  sp.Rational(729, 512)),
    ("Greater Septimal Tritone",  sp.Rational(10, 7)),
    ("Twenty-third Harmonic",  sp.Rational(23, 16)),
    ("Just Diminished Fifth",  sp.Rational(36, 25)),
    ("Ninety-third Harmonic",  sp.Rational(93, 64)),
    ("Undecimal Semi-diminished Fifth",  sp.Rational(16, 11)),
    ("Forty-seventh Harmonic",  sp.Rational(47, 32)),
    ("Pythagorean Diminished Sixth",  sp.Rational(262144, 177147)),
    ("5-limit Wolf Fifth",  sp.Rational(40, 27)),
    ("Ninety-fifth Harmonic",  sp.Rational(95, 64)),
    ("12167th Harmonic",  sp.Rational(12167, 8192)),
    ("Half-comma Meantone Perfect Fifth",  sp.Rational(3,2)/(sp.Rational(81, 80)**sp.Rational(1,2))),
    ("1/3-comma Meantone Perfect Fifth",  sp.Rational(3,2)/(sp.Rational(81, 80)**sp.Rational(1,3))),
    ("2/7-comma Meantone Perfect Fifth",  sp.Rational(3,2)/(sp.Rational(81, 80)**sp.Rational(2,7))),
    ("Quarter-comma Meantone Perfect Fifth",  sp.Rational(3,2)/(sp.Rational(81, 80)**sp.Rational(1,4))),
    ("1/5-comma Meantone Perfect Fifth",  sp.Rational(3,2)/(sp.Rational(81, 80)**sp.Rational(1,5))),
    ("1/6-comma Meantone Perfect Fifth",  sp.Rational(3,2)/(sp.Rational(81, 80)**sp.Rational(1,6))),
    ("Equal-tempered Perect Fifth",  sp.Integer(2) ** sp.Rational(7, 12)),
    ("53-TET Perect Fifth",  sp.Integer(2) ** sp.Rational(31, 53)),
    ("Perfect Fifth",  sp.Rational(3, 2)),
    ("41-TET Perect Fifth",  sp.Integer(2) ** sp.Rational(24, 41)),
    ("29-TET Perect Fifth",  sp.Integer(2) ** sp.Rational(17, 29)),
    ("Ninety-seventh Harmonic",  sp.Rational(97, 64)),
    ("Narrow Diminished Sixth",  sp.Rational(1024, 675)),
    ("21st Subharmonic",  sp.Rational(32, 21)),
    ("Three-hundred-ninety-first Harmonic",  sp.Rational(391, 256)),
    ("Forty-ninth Harmonic",  sp.Rational(49, 32)),
    ("Classic Diminished Sixth",  sp.Rational(192, 125)),
    ("Ninety-ninth Harmonic",  sp.Rational(99, 64)),
    ("Septimal Minor Sixth",  sp.Rational(14, 9)),
    ("Just Augmented Fifth",  sp.Rational(25, 16)),
    ("Wallis Product",  sp.pi / sp.Integer(2)),
    ("Undecimal Minor Sixth",  sp.Rational(11, 7)),
    ("Hundred-first Harmonic",  sp.Rational(101, 64)),
    ("Pythagorean Minor Sixth",  sp.Rational(128, 81)),
    ("Two-hundred-third Harmonic",  sp.Rational(203, 128)),
    ("Equal-tempered Minor Sixth",  sp.Integer(2) ** sp.Rational(8, 12)),
    ("Fifty-first Harmonic",  sp.Rational(51, 32)),
    ("Just Minor Sixth",  sp.Rational(8, 5)),
    ("Pythagorean Augmented Fifth",  sp.Rational(6561, 4096)),
    ("Hundred-third Harmonic",  sp.Rational(103, 64)),
    ("Two-hundred-seventh Harmonic",  sp.Rational(207, 128)),
    ("Golden Ratio", sp.Integer(5) ** sp.Rational(1,2) +  sp.Rational(1, 2)),
    ("Golden Ratio Approximation", sp.Rational(233, 144)),
    ("Acute Minor Sixth", sp.Rational(81, 50)),
    ("Tridecimal Neutral Sixth", sp.Rational(13, 8)),
    ("Two-hundred-ninth Harmonic",  sp.Rational(209, 128)),
    ("Equal-tempered Neutral Sixth",  sp.Integer(2) ** sp.Rational(17, 24)),
    ("Undecimal Neutral Sixth",  sp.Integer(2) ** sp.Rational(18, 11)),
    ("Hundred-fifth Harmonic",  sp.Rational(105, 64)),
    ("Grave Major Sixth",  sp.Rational(400, 243)),
    ("Fifty-third Harmonic",  sp.Rational(53, 32)),
    ("Seventy-seventh Subharmonic",  sp.Rational(128, 77)),
    ("Pythagorean Diminished Seventh",  sp.Rational(32768, 19683)),
    ("Just Major Sixth",  sp.Rational(5, 3)),
    ("Hundred-seventh Harmonic",  sp.Rational(107, 64)),
    ("6859th Harmonic",  sp.Rational(6859, 4096)),
    ("Equal-tempered Major Sixth",  sp.Integer(2) ** sp.Rational(9, 12)),
    ("19th Subharmonic",  sp.Rational(32, 19)),
    ("Pythagorean Major Sixth",  sp.Rational(27, 16)),
    ("Hundred-ninth Harmonic",  sp.Rational(109, 64)),
    ("Just Diminished Seventh",  sp.Rational(128, 75)),
    ("Four-hundred-thirty-seventh Harmonic",  sp.Rational(437, 256)),
    ("Septimal major sixth",  sp.Rational(12, 7)),
    ("Fifty-fifth Harmonic",  sp.Rational(55, 32)),
    ("Hundred-eleventh Harmonic",  sp.Rational(111, 64)),
    ("Just Augmented Sixth",  sp.Rational(125, 72)),
    ("Septimal Minor Seventh",  sp.Rational(7, 4)),
    ("Just Augmented Sixth II",  sp.Rational(225, 128)),
    ("Hundred-thirteenth Harmonic",  sp.Rational(113, 64)),
    ("Pythagorean Minor Seventh",  sp.Rational(16, 9)),
    ("Fifty-seventh Harmonic",  sp.Rational(57, 32)),
    ("Equal-tempered Minor Seventh",  sp.Integer(2) ** sp.Rational(10, 12)),
    ("Hundred-fifteenth Harmonic",  sp.Rational(115, 64)),
    ("Greater Just Minor Seventh",  sp.Rational(9, 5)),
    ("Pythagorean Augmented Sixth",  sp.Rational(59049, 32768)),
    ("Twenty-ninth Harmonic",  sp.Rational(29, 16)),
    ("Lesser Undecimal Neutral Seventh",  sp.Rational(20, 11)),
    ("Acute Minor Seventh", sp.Rational(729, 400)),
    ("Hundred-seventeenth Harmonic",  sp.Rational(117, 64)),
    ("35th Subharmonic",  sp.Rational(64, 35)),
    ("Undecimal Neutral Seventh",  sp.Rational(11, 6)),
    ("Equal-tempered Neutral Seventh",  sp.Integer(2) ** sp.Rational(21, 24)),
    ("Fifty-ninth Harmonic",  sp.Rational(59, 32)),
    ("Grave Major Seventh",  sp.Rational(50, 27)),
    ("Hundred-nineteenth Harmonic",  sp.Rational(119, 64)),
    ("Pythagorean Diminished Octave",  sp.Rational(4096, 2187)),
    ("Just Major Seventh",  sp.Rational(15, 8)),
    ("17th Subharmonic",  sp.Rational(32, 17)),
    ("Equal-tempered Major Seventh",  sp.Integer(2) ** sp.Rational(11, 12)),
    ("Hundred-twenty-first Harmonic",  sp.Rational(121, 64)),
    ("Narrow Diminished Octave",  sp.Rational(256, 135)),
    ("Pythagorean Major Seventh",  sp.Rational(243, 128)),
    ("Sixty-first Harmonic",  sp.Rational(61, 32)),
    ("Classic Diminished Octave",  sp.Rational(48, 25)),
    ("Hundred-twenty-third Harmonic",  sp.Rational(123, 64)),
    ("Septimal Major Seventh",  sp.Rational(27, 14)),
    ("Two-hundred-forty-seventh Harmonic",  sp.Rational(247, 128)),
    ("Thirty-first Harmonic",  sp.Rational(31, 16)),
    ("Thirty-third Subharmonic",  sp.Rational(64, 33)),
    ("Septimal Supermajor Seventh",  sp.Rational(35, 18)),
    ("Just Augmented Seventh",  sp.Rational(125, 64)),
    ("Sixty-third Harmonic",  sp.Rational(63, 32)),
    ("Semi-diminished Octave",  sp.Rational(160, 81)),
    ("Two-hundred-fifty-third Harmonic",  sp.Rational(253, 128)),
    ("Hundred-twenty-seventh Harmonic",  sp.Rational(127, 64)),
    ("Octave",  sp.Rational(2, 1)),
    ("Pythagorean Augmented Seventh",  sp.Rational(531441, 262144)),
    ("Silver Ratio",  sp.Integer(2) ** sp.Rational(1, 2) + sp.Integer(1)),
    ("Just Perfect Twelfth",  sp.Rational(3, 1)),
    ("Fifteenth",  sp.Rational(4, 1)),
    ("Decade",  sp.Rational(10, 1)),
]

all_constructors = [
    (lucy_construtors, "Lu"),
    (five_limit_constructors, "Five"),
    (edo12_constructors, "12-EDO"),
]

