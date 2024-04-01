
multi_thread_test = {"enron": {
    "single_thread": [0.0447604],

    "std::thread": [0.0466771, 0.0352848, 0.0257682, 0.0174631, 0.0138795, 0.011244, 0.0115998, 0.0108549, 0.0145421],

    "openMP": [0.045768, 0.0350442, 0.0246813, 0.0254324, 0.0132738, 0.0148617, 0.0103104, 0.012333, 0.0135794]
    },

    "SocialEvo": {
        "single_thread": [2.52553],

        "std::thread": [2.64261, 1.39641, 0.724006, 0.463454, 0.395307, 0.41798, 0.439435, 0.429184, 1.12296],

        "openMP": [2.53957, 1.31414, 0.724218, 0.492544, 0.422692, 0.422254, 0.376572, 0.343189, 0.347057]
    },

    "wikipedia": {
        "single_thread": [0.0067389],

        "std::thread": [0.0050003, 0.0050375, 0.0038346, 0.0031765, 0.0034774, 0.0019182, 0.0024183, 0.0024883, 0.002572],

        "openMP": [0.0069488, 0.0059902, 0.0045915, 0.0031638, 0.0056765, 0.0036073, 0.0043271, 0.0047385, 0.0055852]
    },

    "UNvote": {
        "single_thread": [3.44516],

        "std::thread": [4.88065, 2.55776, 1.34523, 0.873556, 0.836175, 0.855919, 0.878923, 1.11323, 0.869884],

        "openMP": [3.88881, 2.1664, 1.1644, 0.742651, 0.713325, 0.667296, 0.665877, 0.670454, 0.671273]
    },

    "CanParl": {
        "single_thread": [0.202469],

        "std::thread": [0.2326, 0.142349, 0.0818866, 0.069803, 0.0588929, 0.0518759, 0.0422494, 0.0536643, 0.0466783],

        "openMP": [0.207983, 0.12207, 0.0667316, 0.0709501, 0.0485417, 0.0525752, 0.0381819, 0.0430255, 0.0413479]
    },

    "reddit": {
        "single_thread": [0.0427858],

        "std::thread": [0.0426916, 0.0244, 0.018392, 0.0130496, 0.0109217, 0.0103585, 0.0109805, 0.0113693, 0.0107279],

        "openMP": [0.0427734, 0.0297063, 0.0140645, 0.0142104, 0.0155966, 0.0116079, 0.0111757, 0.0139867, 0.0121145]
    },

    "lastfm": {
        "single_thread": [0.122308],

        "std::thread": [0.116784, 0.0757908, 0.0473578, 0.03861, 0.0392556, 0.0306224, 0.0226002, 0.0291552, 0.0232138],

        "openMP": [0.117559, 0.0751007, 0.0484628, 0.0416427, 0.0374093, 0.0279097, 0.0275754, 0.026371, 0.0328069]
    },

    "Flights": {
        "single_thread": [14.4169],

        "std::thread": [15.0804, 14.3232, 12.0755, 7.6103, 6.22797, 4.96541, 4.5452, 3.35103, 3.23034],

        "openMP": [14.5833, 13.7618, 11.7541, 7.42146, 6.03305, 4.83162, 4.40371, 3.433, 3.13565,]
    },

    "tgbl_review": {
        "single_thread": [9.80499],

        "std::thread": [9.80361, 5.57482, 3.83126, 2.21772, 1.77745, 1.68261, 1.60565, 1.58825, 1.50429],

        "openMP": [9.76086, 5.92736, 3.77548, 2.18009, 1.74402, 1.5213, 1.33973, 1.27413, 1.24964]
    }
}

num_threads = [1, 2, 4, 8, 12, 18, 24, 36, 48]