import requests

baseURL = 'https://cdn.destiny.gg/2.31.4/emotes/'

emoteFileName = {
    'Abathur': '5c2bbb92c428e.png',
    'AMAZIN': '5d2de6f9879d5.png',
    'AngelThump': '5c2bbb9fa8ab2.png',
    'ApeHands': '5fad9768d877a.png',
    'Askers': '604fa56f679e0.png',
    'ASLAN': '5c2bbba3d610e.png',
    'ATAB': '5e0e86da24387.png',
    'AYAYA': '5c9a2d62d1465.png',
    'AYYYLMAO': '5c2bbbebf33af.png',
    'BasedGod': '5c2bbbefacf96.png',
    'BASEDWATM8': '5c2bbbf49150d.png',
    'BERN': '5e75ea9259721.png',
    'BibleThump': '5dbc28c9aaf11.png',
    'BLADE': '5dbc2afb17f2d.png',
    'Blesstiny': '5c853d5386bb4.png',
    'Blubstiny': '5c2bbc044e883.png',
    'BOGGED': '5c2bbe828f06f.png',
    'BOOMER': '5c2bbe46e0902.png',
    'BoomerSippy': '5c2bbd9876df6.png',
    'catJAM': '5f9325d81e730.png',
    'CheekerZ': '5c2bbc135d59a.png',
    'ChibiDesti': '5c2bbc1735d07.png',
    'Clap': '5fcdbf43b5737.png',
    'COGGERS': '5e739f2779b87.png',
    'ComfyAYA': '5fad97de7a0ef.png',
    'ComfyDog': '5fad97ff5f13f.png',
    'ComfyFerret': '5fad983ac8f92.png',
    'ComfyMel': '60ce44850fa13.png',
    'COOMER': '5deeb1be854b5.png',
    'Copium': '60629a078e75a.png',
    'CROPSTINY': '5f77e4b4b1478.png',
    'CuckCrab': '5fc5b4b8d0924.png',
    'Cutestiny': '5d4cae6357857.png',
    'CUX': '5fad984e24378.png',
    'DaFeels': '5c2bbc1b2e160.png',
    'DAFUK': '5c2bbc1fcce8b.png',
    'DANKMEMES': '5c2bbc2900791.png',
    'DappaKappa': '5c2bbc2da711b.png',
    'DatGeoff': '5c2bbc3390e35.png',
    'DCOLON': '6002196ce1fcd.png',
    'DEATH': '6090e31923c29.png',
    'Depresstiny': '5d9bcc0703318.png',
    'Derpstiny': '5c2bbc4182b70.png',
    'DestiSenpaii': '5c2bbc4667163.png',
    'dggL': '60bf90f646882.png',
    'Disgustiny': '5c2bbc4a7f469.png',
    'Dravewin': '5c2bbc53f0c1f.png',
    'DuckerZ': '5c2bbc5803fc3.png',
    'DURRSTINY': '5c2bbc5d7c463.png',
    'ECH': '5fad98908092e.png',
    'FeedNathan': '5c2bbc6606d88.png',
    'FeelsAmazingMan': '5c9d7ec48797a.png',
    'FeelsBadMan': '5c2bbc80871dc.png',
    'FeelsBirthdayMan': '5e43385064e0b.png',
    'FeelsDankMan': '60358531515f7.png',
    'FeelsGimiMan': '5fad989c70b44.png',
    'FeelsGoodMan': '5c2bbc841b91d.png',
    'FeelsOkayMan': '5fc940888e8d3.png',
    'FeelsPeekMan': '5f8047548c667.png',
    'FeelsStrongMan': '6042d7a113ac4.png',
    'FeelsWeirdMan': '5c64580edcbfc.png',
    'FerretLOL': '5c2bbc8b86ce5.png',
    'FiveHead': '5fa1f1d6e4f61.png',
    'ForYou': '5ca12d317a726.png',
    'FourHead': '5d2a2db890ef3.png',
    'FrankerZ': '5c2bbc9643ba6.png',
    'gachiGASM': '5c2bbc9ac1396.png',
    'GameOfThrows': '5c2bbc9fe6f55.png',
    'GODSTINY': '5c2bbca645afb.png',
    'GRUG': '5ca9105b77062.png',
    'GRUGingOverIt': '5ff681331f147.png',
    'HACKERMAN': '5ea07dfa1b6be.png',
    'haHAA': '5c64578911392.png',
    'Heimerdonger': '5c2bbcb48c4b5.png',
    'Hhhehhehe': '5c2bbcb8555ca.png',
    'HmmStiny': '5c2bbcc8ec75b.png',
    'INFESTINY': '5c2bbccd35834.png',
    'JAMSTINY': '5cb1a46530730.png',
    'Kappa': '5c2bbcd46c08e.png',
    'KappaRoss': '5c2bbcd93ac09.png',
    'KING': '5c097d4f0ffdc.png',
    'Klappa': '5e78eb181cc2b.png',
    'LeRuse': '5c2bbcebab235.png',
    'LIES': '5c2bbcf1cd4b9.png',
    'LOVE': '5cc0cc2a87ca8.png',
    'LUL': '5c2bbcfe2ba44.png',
    'LULW': '5ca69cfac2c36.png',
    'MALARKEY': '5fa6b9f31acce.png',
    'MASTERB8': '5c2bbd0253815.png',
    'Memegasm': '5d6d427ea12da.png',
    'Milkerino': '5d49e3877c9af.png',
    'miyanobird': '60bf94cfac994.png',
    'MiyanoHype': '5fad98c878487.png',
    'MLADY': '5c2bbd0b9b6b6.png',
    'MMMM': '6042d72d587b3.png',
    'monkaS': '5bd0b9a7c59aa.png',
    'monkaSMEGA': '5fad990aab084.png',
    'monkaVirus': '6084a59c0fa32.png',
    'MotherFuckinGame': '5c2bbd1553bd6.png',
    'Nappa': '5c2bbd1be9ad4.png',
    'nathanAYAYA': '5bd0bba836b06.png',
    'nathanBlub': '5c40a5e35d35f.png',
    'nathanBogged': '5bd0bcdeb3dd7.png',
    'nathanBoomer': '5bd45c4de2c7c.png',
    'nathanD': 'nathanD.png',
    'nathanDank': 'nathanDank.png',
    'nathanDerp': '5bd45dec0ab38.png',
    'nathanEZ': '5bd45c36a122d.png',
    'nathanF': 'nathanF.png',
    'nathanFeels': '5bd45ccae347b.png',
    'nathanGG': '5eb83e6d3f994.png',
    'nathanGod1': '5bd45e03eb2ea.png',
    'nathanGod2': '5bd45e139076a.png',
    'nathanGod3': '5bd45e23f0cee.png',
    'nathanGod4': '5bd45f3c6eae7.png',
    'nathanGodstiny': '5bd45e470b2b8.png',
    'nathanNotears': 'nathanNotears.png',
    'nathanObject': '5bd0bcedca931.png',
    'nathanOOO': '5e558e36bda2f.png',
    'nathanPrime': '5dc57113d5ff5.png',
    'nathanRuse': '5bd45e56accb7.png',
    'nathanRustle': 'nathanRustle.png',
    'nathanSenpai': '5bd45e659afb6.png',
    'nathanShroom': '5bd0bcf95cda3.png',
    'nathanThinking': 'nathanThinking.png',
    'nathanTiny1': '5bd0bd1f207f0.png',
    'nathanTiny2': '5e86473432d97.png',
    'nathanTiny2_OG': '5bd45e7198b76.png',
    'nathanTowel': 'nathanTowel.png',
    'nathanW': '5ced892bca560.png',
    'nathanWat': 'nathanWat.png',
    'nathanWeeb': 'nathanWeeb.png',
    'nathanYee': 'nathanYee.png',
    'nathanYikes': '5bd0bd13411c5.png',
    'nathanZoomer': '5bd45c615cf17.png',
    'NiceMeMe': '5fad994ca9712.png',
    'NOBULLY': '5dbcecfab8366.png',
    'NODDERS': '6042d80da1e42.gif',
    'NOPERS': '6042d81691e39.gif',
    'NoTears': '5c2bbd3411c78.png',
    'NOTMYTEMPO': '5c2bbd3815115.png',
    'OhKrappa': '5c2bbd42b7813.png',
    'OhMyDog': '5c2bbd616693b.png',
    'OMEGALUL': '5dc74d7a33e54.png',
    'OOOO': '5e75f1c3a21a1.png',
    'OverRustle': '5c2bbd65ae0bd.png',
    'Painstiny': '5c46adc6a005a.png',
    'PARDNER': '5dbc29955bf02.png',
    'peepoRiot': '5e9a25016d376.png',
    'PEPE': '5c2bbd6a7a9fc.png',
    'PepeHands': '5ca5346a0d73e.png',
    'PepeLaugh': '5e0e8cda1adc5.png',
    'PepeMods': '5d3661812359a.png',
    'pepeSteer': '5fc5c2f5071e9.png',
    'pepeW': '60bf8cd6ceb0c.gif',
    'PepoComfy': '5fad9970a3544.png',
    'PepoG': '5e371219bb105.png',
    'PepOk': '5fad997f9451d.png',
    'PepoThink': '5c2bbd6f0d004.png',
    'PepoTurkey': '5dde917989efa.png',
    'PepoWant': '5fad998c3e160.png',
    'PICNIC': '5c2bbda28a6aa.png',
    'Pog': '5c6455a35f292.png',
    'POGGERS': '5f9e8d17d1522.png',
    'POTATO': '5c2bbd73eb062.png',
    'RapThis': '60bf9011b7631.gif',
    'RaveDoge': '603e0f856ad93.png',
    'REE': '5c2bbd7a53a86.png',
    'Shroomstiny': '5e6c71ea21901.png',
    'Shrugstiny': '5e8666ff1b079.png',
    'SICKO': '5cd7fac3af988.png',
    'Sippy': '60404aaaa5bf3.png',
    'SLEEPSTINY': '5c2bbdc90339b.png',
    'Slugstiny': '5c9a717b39342.png',
    'Slumlord': '5c2bbd81423bf.png',
    'SMASHit': '604fa4fa5ca3d.png',
    'SNAP': '5c5b9c9ba430a.png',
    'SoDoge': '5c2bbdcf33df8.png',
    'SOTRIGGERED': '5f53c4e3d30f4.png',
    'SOY': '5f453cebbe54a.png',
    'SpookerZ': '5c2bbddae0132.png',
    'SURPRISE': '5c2bbde674ef2.png',
    'SWEATSTINY': '5c2bbdeb24b1c.png',
    'TeddyPepe': '604f812273559.png',
    'tf': '5f53c57e5b1c2.png',
    'tonyW': '5feeaf97de293.png',
    'TRIAD': '5fc0682f0c354.png',
    'triHarder': '5d261f7e6b602.png',
    'TRUMPED': '5fa349ea693b6.png',
    'UNLUCKY': '6007623b6f68c.png',
    'UWOTM8': '5c2bbe1b619af.png',
    'WEOW': '5fad99b90d06e.png',
    'WhoahDude': '5c2bbe2630ff0.png',
    'widepeepoHappy': '5f77e553b6db7.png',
    'WOOF': '5f77ea04722e5.png',
    'WooYeah': '603cdf2fc0c2f.png',
    'WORTH': '5c2bbe2aa9b81.png',
    'Wowee': '5c2bbe2e9c2f2.png',
    'YAM': '5f8046606285d.png',
    'YEE': '5c2bbe330b357.png',
    'YEEHAW': '5dbc2978ba71b.png',
    'YeeLaugh': '5f80473a678f3.png',
    'YeeMods': '5f80481978dc9.png',
    'Yoda1': '5f355485bebee.png',
    'ZOOMER': '5c2bbe3c34dab.png',
}