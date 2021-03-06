from cereal import car
from selfdrive.car import dbc_dict

AudibleAlert = car.CarControl.HUDControl.AudibleAlert
VisualAlert = car.CarControl.HUDControl.VisualAlert

# Car button codes
class CruiseButtons:
  RES_ACCEL   = 4
  DECEL_SET   = 3
  CANCEL      = 2
  MAIN        = 1

#car chimes: enumeration from dbc file. Chimes are for alerts and warnings
class CM:
  MUTE = 0
  SINGLE = 3
  DOUBLE = 4
  REPEATED = 1
  CONTINUOUS = 2

#car beeps: enumeration from dbc file. Beeps are for engage and disengage
class BP:
  MUTE = 0
  SINGLE = 3
  TRIPLE = 2
  REPEATED = 1

AUDIO_HUD = {
  AudibleAlert.none: (BP.MUTE, CM.MUTE),
  AudibleAlert.chimeEngage: (BP.SINGLE, CM.MUTE),
  AudibleAlert.chimeDisengage: (BP.SINGLE, CM.MUTE),
  AudibleAlert.chimeError: (BP.MUTE, CM.DOUBLE),
  AudibleAlert.chimePrompt: (BP.MUTE, CM.SINGLE),
  AudibleAlert.chimeWarning1: (BP.MUTE, CM.DOUBLE),
  AudibleAlert.chimeWarning2: (BP.MUTE, CM.REPEATED),
  AudibleAlert.chimeWarningRepeat: (BP.MUTE, CM.REPEATED)}

class AH:
  #[alert_idx, value]
  # See dbc files for info on values"
  NONE           = [0, 0]
  FCW            = [1, 1]
  STEER          = [2, 1]
  BRAKE_PRESSED  = [3, 10]
  GEAR_NOT_D     = [4, 6]
  SEATBELT       = [5, 5]
  SPEED_TOO_HIGH = [6, 8]

VISUAL_HUD = {
  VisualAlert.none: AH.NONE,
  VisualAlert.fcw: AH.FCW,
  VisualAlert.steerRequired: AH.STEER,
  VisualAlert.brakePressed: AH.BRAKE_PRESSED,
  VisualAlert.wrongGear: AH.GEAR_NOT_D,
  VisualAlert.seatbeltUnbuckled: AH.SEATBELT,
  VisualAlert.speedTooHigh: AH.SPEED_TOO_HIGH}

class CAR:
  ACCORD = "HONDA ACCORD 2018 SPORT 2T"
  ACCORD_15 = "HONDA ACCORD 2018 LX 1.5T"
  ACCORDH = "HONDA ACCORD 2018 HYBRID TOURING"
  CIVIC = "HONDA CIVIC 2016 TOURING"
  CIVIC_BOSCH = "HONDA CIVIC HATCHBACK 2017 SEDAN/COUPE 2019"
  ACURA_ILX = "ACURA ILX 2016 ACURAWATCH PLUS"
  CRV = "HONDA CR-V 2016 TOURING"
  CRV_5G = "HONDA CR-V 2017 EX"
  ODYSSEY = "HONDA ODYSSEY 2018 EX-L"
  ACURA_RDX = "ACURA RDX 2018 ACURAWATCH PLUS"
  PILOT = "HONDA PILOT 2017 TOURING"
  PILOT_2019 = "HONDA PILOT 2019 ELITE"
  RIDGELINE = "HONDA RIDGELINE 2017 BLACK EDITION"
  P_308_2018 = "Peugeot 308 SW 2018"
  Captur_2018 = "Renault Captur 2018"
  Clio_IV_2018 = "Renault Clio IV 2018"

FINGERPRINTS = {
  CAR.ACCORD: [{
    148: 8, 228: 5, 304: 8, 330: 8, 344: 8, 380: 8, 399: 7, 419: 8, 420: 8, 427: 3, 432: 7, 441: 5, 446: 3, 450: 8, 464: 8, 477: 8, 479: 8, 495: 8, 545: 6, 662: 4, 773: 7, 777: 8, 780: 8, 804: 8, 806: 8, 808: 8, 829: 5, 862: 8, 884: 8, 891: 8, 927: 8, 929: 8, 1302: 8, 1600: 5, 1601: 8, 1652: 8
  }],
  CAR.ACCORD_15: [{
    148: 8, 228: 5, 304: 8, 330: 8, 344: 8, 380: 8, 399: 7, 401: 8, 420: 8, 427: 3, 432: 7, 441: 5, 446: 3, 450: 8, 464: 8, 477: 8, 479: 8, 495: 8, 545: 6, 662: 4, 773: 7, 777: 8, 780: 8, 804: 8, 806: 8, 808: 8, 829: 5, 862: 8, 884: 8, 891: 8, 927: 8, 929: 8, 1302: 8, 1600: 5, 1601: 8, 1652: 8
  }],
  CAR.ACCORDH: [{
    148: 8, 228: 5, 304: 8, 330: 8, 344: 8, 380: 8, 387: 8, 388: 8, 399: 7, 419: 8, 420: 8, 427: 3, 432: 7, 441: 5, 450: 8, 464: 8, 477: 8, 479: 8, 495: 8, 525: 8, 545: 6, 662: 4, 773: 7, 777: 8, 780: 8, 804: 8, 806: 8, 808: 8, 829: 5, 862: 8, 884: 8, 891: 8, 927: 8, 929: 8, 1302: 8, 1600: 5, 1601: 8, 1652: 8
  }],
  CAR.ACURA_ILX: [{
    57: 3, 145: 8, 228: 5, 304: 8, 316: 8, 342: 6, 344: 8, 380: 8, 398: 3, 399: 7, 419: 8, 420: 8, 422: 8, 428: 8, 432: 7, 464: 8, 476: 4, 490: 8, 506: 8, 512: 6, 513: 6, 542: 7, 545: 4, 597: 8, 660: 8, 773: 7, 777: 8, 780: 8, 800: 8, 804: 8, 808: 8, 819: 7, 821: 5, 829: 5, 882: 2, 884: 7, 887: 8, 888: 8, 892: 8, 923: 2, 929: 4, 983: 8, 985: 3, 1024: 5, 1027: 5, 1029: 8, 1030: 5, 1034: 5, 1036: 8, 1039: 8, 1057: 5, 1064: 7, 1108: 8, 1365: 5,
  }],
  # Acura RDX w/ Added Comma Pedal Support (512L & 513L)
  CAR.ACURA_RDX: [{
    57: 3, 145: 8, 229: 4, 308: 5, 316: 8, 342: 6, 344: 8, 380: 8, 392: 6, 398: 3, 399: 6, 404: 4, 420: 8, 422: 8, 426: 8, 432: 7, 464: 8, 474: 5, 476: 4, 487: 4, 490: 8, 506: 8, 512: 6, 513: 6, 542: 7, 545: 4, 597: 8, 660: 8, 773: 7, 777: 8, 780: 8, 800: 8, 804: 8, 808: 8, 819: 7, 821: 5, 829: 5, 882: 2, 884: 7, 887: 8, 888: 8, 892: 8, 923: 2, 929: 4, 963: 8, 965: 8, 966: 8, 967: 8, 983: 8, 985: 3, 1024: 5, 1027: 5, 1029: 8, 1033: 5, 1034: 5, 1036: 8, 1039: 8, 1057: 5, 1064: 7, 1108: 8, 1365: 5, 1424: 5, 1729: 1
  }],
  CAR.CIVIC: [{
    57: 3, 148: 8, 228: 5, 304: 8, 330: 8, 344: 8, 380: 8, 399: 7, 401: 8, 420: 8, 427: 3, 428: 8, 432: 7, 450: 8, 464: 8, 470: 2, 476: 7, 487: 4, 490: 8, 493: 5, 506: 8, 512: 6, 513: 6, 545: 6, 597: 8, 662: 4, 773: 7, 777: 8, 780: 8, 795: 8, 800: 8, 804: 8, 806: 8, 808: 8, 829: 5, 862: 8, 884: 8, 891: 8, 892: 8, 927: 8, 929: 8, 985: 3, 1024: 5, 1027: 5, 1029: 8, 1036: 8, 1039: 8, 1108: 8, 1302: 8, 1322: 5, 1361: 5, 1365: 5, 1424: 5, 1633: 8,
  }],
  CAR.CIVIC_BOSCH: [{
  # 2017 Civic Hatchback EX and 2019 Civic Sedan Touring Canadian
    57: 3, 148: 8, 228: 5, 304: 8, 330: 8, 344: 8, 380: 8, 399: 7, 401: 8, 420: 8, 427: 3, 428: 8, 432: 7, 441: 5, 450: 8, 464: 8, 470: 2, 476: 7, 477: 8, 479: 8, 490: 8, 493: 5, 495: 8, 506: 8, 545: 6, 597: 8, 662: 4, 773: 7, 777: 8, 780: 8, 795: 8, 800: 8, 804: 8, 806: 8, 808: 8, 829: 5, 862: 8, 884: 8, 891: 8, 892: 8, 927: 8, 929: 8, 985: 3, 1024: 5, 1027: 5, 1029: 8, 1036: 8, 1039: 8, 1108: 8, 1302: 8, 1322: 5, 1361: 5, 1365: 5, 1424: 5, 1600: 5, 1601: 8, 1633: 8,
  }],
  CAR.CRV: [{
    57: 3, 145: 8, 316: 8, 340: 8, 342: 6, 344: 8, 380: 8, 398: 3, 399: 6, 401: 8, 404: 4, 420: 8, 422: 8, 426: 8, 432: 7, 464: 8, 474: 5, 476: 4, 487: 4, 490: 8, 493: 3, 506: 8, 507: 1, 512: 6, 513: 6, 542: 7, 545: 4, 597: 8, 660: 8, 661: 4, 773: 7, 777: 8, 780: 8, 800: 8, 804: 8, 808: 8, 829: 5, 882: 2, 884: 7, 888: 8, 891: 8, 892: 8, 923: 2, 929: 8, 983: 8, 985: 3, 1024: 5, 1027: 5, 1029: 8, 1033: 5, 1036: 8, 1039: 8, 1057: 5, 1064: 7, 1108: 8, 1125: 8, 1296: 8, 1365: 5, 1424: 5, 1600: 5, 1601: 8,
  }],
  CAR.CRV_5G: [{
    57: 3, 148: 8, 199: 4, 228: 5, 231: 5, 232: 7, 304: 8, 330: 8, 340: 8, 344: 8, 380: 8, 399: 7, 401: 8, 420: 8, 423: 2, 427: 3, 428: 8, 432: 7, 441: 5, 446: 3, 450: 8, 464: 8, 467: 2, 469: 3, 470: 2, 474: 8, 476: 7, 477: 8, 479: 8, 490: 8, 493: 5, 495: 8, 507: 1, 545: 6, 597: 8, 661: 4, 662: 4, 773: 7, 777: 8, 780: 8, 795: 8, 800: 8, 804: 8, 806: 8, 808: 8, 814: 4, 815: 8, 817: 4, 825: 4, 829: 5, 862: 8, 881: 8, 882: 4, 884: 8, 888: 8, 891: 8, 927: 8, 918: 7, 929: 8, 983: 8, 985: 3, 1024: 5, 1027: 5, 1029: 8, 1036: 8, 1039: 8, 1064: 7, 1108: 8, 1092: 1, 1115: 4, 1125: 8, 1127: 2, 1296: 8, 1302: 8, 1322: 5, 1361: 5, 1365: 5, 1424: 5, 1600: 5, 1601: 8, 1618: 5, 1633: 8, 1670: 5
  }],
  # 2018 Odyssey w/ Added Comma Pedal Support (512L & 513L)
  CAR.ODYSSEY: [{
    57: 3, 148: 8, 228: 5, 229: 4, 316: 8, 342: 6, 344: 8, 380: 8, 399: 7, 411: 5, 419: 8, 420: 8, 427: 3, 432: 7, 450: 8, 463: 8, 464: 8, 476: 4, 490: 8, 506: 8, 512: 6, 513: 6, 542: 7, 545: 6, 597: 8, 662: 4, 773: 7, 777: 8, 780: 8, 795: 8, 800: 8, 804: 8, 806: 8, 808: 8, 817: 4, 819: 7, 821: 5, 825: 4, 829: 5, 837: 5, 856: 7, 862: 8, 871: 8, 881: 8, 882: 4, 884: 8, 891: 8, 892: 8, 905: 8, 923: 2, 927: 8, 929: 8, 963: 8, 965: 8, 966: 8, 967: 8, 983: 8, 985: 3, 1029: 8, 1036: 8, 1052: 8, 1064: 7, 1088: 8, 1089: 8, 1092: 1, 1108: 8, 1110: 8, 1125: 8, 1296: 8, 1302: 8, 1600: 5, 1601: 8, 1612: 5, 1613: 5, 1614: 5, 1615: 8, 1616: 5, 1619: 5, 1623: 5, 1668: 5
  },
  # 2018 Odyssey Elite w/ Added Comma Pedal Support (512L & 513L)
  {
    57: 3, 148: 8, 228: 5, 229: 4, 304: 8, 342: 6, 344: 8, 380: 8, 399: 7, 411: 5, 419: 8, 420: 8, 427: 3, 432: 7, 440: 8, 450: 8, 463: 8, 464: 8, 476: 4, 490: 8, 506: 8, 507: 1, 542: 7, 545: 6, 597: 8, 662: 4, 773: 7, 777: 8, 780: 8, 795: 8, 800: 8, 804: 8, 806: 8, 808: 8, 817: 4, 819: 7, 821: 5, 825: 4, 829: 5, 837: 5, 856: 7, 862: 8, 871: 8, 881: 8, 882: 4, 884: 8, 891: 8, 892: 8, 905: 8, 923: 2, 927: 8, 929: 8, 963: 8, 965: 8, 966: 8, 967: 8, 983: 8, 985: 3, 1029: 8, 1036: 8, 1052: 8, 1064: 7, 1088: 8, 1089: 8, 1092: 1, 1108: 8, 1110: 8, 1125: 8, 1296: 8, 1302: 8, 1600: 5, 1601: 8, 1612: 5, 1613: 5, 1614: 5, 1616: 5, 1619: 5, 1623: 5, 1668: 5
  }],
  # 2017 Pilot Touring AND 2016 Pilot EX-L w/ Added Comma Pedal Support (512L & 513L)
  CAR.PILOT: [{
    57: 3, 145: 8, 228: 5, 229: 4, 308: 5, 316: 8, 334: 8, 339: 7, 342: 6, 344: 8, 379: 8, 380: 8, 392: 6, 399: 7, 419: 8, 420: 8, 422: 8, 425: 8, 426: 8, 427: 3, 432: 7, 463: 8, 464: 8, 476: 4, 490: 8, 506: 8, 507: 1, 512: 6, 513: 6, 538: 3, 542: 7, 545: 5, 546: 3, 597: 8, 660: 8, 773: 7, 777: 8, 780: 8, 795: 8, 800: 8, 804: 8, 808: 8, 819: 7, 821: 5, 829: 5, 837: 5, 856: 7, 871: 8, 882: 2, 884: 7, 891: 8, 892: 8, 923: 2, 929: 8, 963: 8, 965: 8, 966: 8, 967: 8, 983: 8, 985: 3, 1027: 5, 1029: 8, 1036: 8, 1039: 8, 1064: 7, 1088: 8, 1089: 8, 1108: 8, 1125: 8, 1296: 8, 1424: 5, 1600: 5, 1601: 8, 1612: 5, 1613: 5, 1616: 5, 1618: 5, 1668: 5
  }],
  CAR.PILOT_2019: [{
    57: 3, 145: 8, 228: 5, 308: 5, 316: 8, 334: 8, 342: 6, 344: 8, 379: 8, 380: 8, 399: 7, 411: 5, 419: 8, 420: 8, 422: 8, 425: 8, 426: 8, 427: 3, 432: 7, 463: 8, 464: 8, 476: 4, 490: 8, 506: 8, 538: 3, 542: 7, 545: 5, 546: 3, 597: 8, 660: 8, 773: 7, 777: 8, 780: 8, 795: 8, 800: 8, 804: 8, 808: 8, 817: 4, 819: 7, 821: 5, 825: 4, 829: 5, 837: 5, 856: 7, 871: 8, 881: 8, 882: 2, 884: 7, 891: 8, 892: 8, 923: 2, 927: 8, 929: 8, 983: 8, 985: 3, 1029: 8, 1052: 8, 1064: 7, 1088: 8, 1089: 8, 1092: 1, 1108: 8, 1110: 8, 1125: 8, 1296: 8, 1424: 5, 1445: 8, 1600: 5, 1601: 8, 1612: 5, 1613: 5, 1614: 5, 1615: 8, 1616: 5, 1617: 8, 1618: 5, 1623: 5, 1668: 5
  },
  # 2019 Pilot EX-L
  {
    57: 3, 145: 8, 228: 5, 229: 4, 308: 5, 316: 8, 339: 7, 342: 6, 344: 8, 380: 8, 392: 6, 399: 7, 411: 5, 419: 8, 420: 8, 422: 8, 425: 8, 426: 8, 427: 3, 432: 7, 464: 8, 476: 4, 490: 8, 506: 8, 542: 7, 545: 5, 546: 3, 597: 8, 660: 8, 773: 7, 777: 8, 780: 8, 795: 8, 800: 8, 804: 8, 808: 8, 817: 4, 819: 7, 821: 5, 829: 5, 871: 8, 881: 8, 882: 2, 884: 7, 891: 8, 892: 8, 923: 2, 927: 8, 929: 8, 963: 8, 965: 8, 966: 8, 967: 8, 983: 8, 985: 3, 1027: 5, 1029: 8, 1039: 8, 1064: 7, 1088: 8, 1089: 8, 1092: 1, 1108: 8, 1125: 8, 1296: 8, 1424: 5, 1445: 8, 1600: 5, 1601: 8, 1612: 5, 1613: 5, 1616: 5, 1617: 8, 1618: 5, 1623: 5, 1668: 5
  }],
  # Ridgeline w/ Added Comma Pedal Support (512L & 513L)
  CAR.RIDGELINE: [{
    57: 3, 145: 8, 228: 5, 229: 4, 308: 5, 316: 8, 339: 7, 342: 6, 344: 8, 380: 8, 392: 6, 399: 7, 419: 8, 420: 8, 422: 8, 425: 8, 426: 8, 427: 3, 432: 7, 464: 8, 471: 3, 476: 4, 490: 8, 506: 8, 512: 6, 513: 6, 545: 5, 546: 3, 597: 8, 660: 8, 773: 7, 777: 8, 780: 8, 795: 8, 800: 8, 804: 8, 808: 8, 819: 7, 821: 5, 829: 5, 871: 8, 882: 2, 884: 7, 892: 8, 923: 2, 927: 8, 929: 8, 963: 8, 965: 8, 966: 8, 967: 8, 983: 8, 985: 3, 1027: 5, 1029: 8, 1036: 8, 1039: 8, 1064: 7, 1088: 8, 1089: 8, 1108: 8, 1125: 8, 1296: 8, 1365: 5, 1424: 5, 1600: 5, 1601: 8, 1613: 5, 1616: 5, 1618: 5, 1668: 5, 2015: 3
  },
  # 2019 Ridgeline
  {
    57: 3, 145: 8, 229: 4, 308: 5, 316: 8, 339: 7, 342: 6, 344: 8, 380: 8, 392: 6, 399: 7, 419: 8, 420: 8, 422:8, 425: 8, 426: 8, 427: 3, 432: 7, 464: 8, 476: 4, 490: 8, 545: 5, 546: 3, 597: 8, 660: 8, 773: 7, 777: 8, 795: 8, 800: 8, 804: 8, 808: 8, 819: 7, 821: 5, 871: 8, 882: 2, 884: 7, 892: 8, 923: 2, 929: 8, 963: 8, 965: 8, 966: 8, 967: 8, 983: 8, 985: 3, 1027: 5, 1029: 8, 1036: 8, 1039: 8, 1064: 7, 1088: 8, 1089: 8, 1092: 1, 1108: 8, 1125: 8, 1296: 8, 1365: 5, 424: 5, 1613: 5, 1616: 5, 1618: 5, 1623: 5, 1668: 5
  }],
  CAR.P_308_2018: [{
    114: 5, 168: 5, 228: 5, 264: 8, 269: 8, 274: 8, 277: 8, 488: 8, 512: 6, 513: 6, 520: 8, 552: 8, 649: 8, 743: 1, 749: 7, 757: 7, 773: 7, 781: 8, 813: 8, 840: 8, 845: 8, 909: 8, 968: 2, 973: 8, 1010: 8, 1037: 8, 1042: 8, 1069: 4, 1074: 8, 1080: 8, 1101: 8, 1106: 6, 1128: 8, 1134: 2, 1160: 8, 1166: 4, 1170: 6, 1173: 4, 1202: 8, 1230: 8, 1234: 3, 1266: 8, 1293: 8, 1294: 8, 1326: 8, 1330: 5, 1358: 8, 1362: 8, 1390: 6, 1394: 8, 1400: 4, 1416: 8, 1422: 8, 1426: 8, 1432: 4, 1448: 7, 1454: 5, 1458: 8, 1464: 8, 1486: 3, 1490: 3, 1496: 6, 1517: 3, 1518: 4, 1528: 5, 1554: 8, 1928: 8, 1933: 8, 1938: 8, 1941: 6, 1960: 4
  },
  {
    114: 5, 168: 5, 264: 8, 269: 8, 274: 8, 277: 8, 488: 8, 512: 6, 513: 6, 520: 8, 552: 8, 649: 8, 743: 1, 749: 7, 757: 7, 773: 7, 781: 8, 813: 8, 840: 8, 845: 8, 909: 8, 968: 2, 973: 8, 1010: 8, 1037: 8, 1042: 8, 1069: 4, 1074: 8, 1080: 8, 1101: 8, 1106: 6, 1128: 8, 1134: 2, 1160: 8, 1166: 4, 1170: 6, 1173: 4, 1202: 8, 1230: 8, 1234: 3, 1266: 8, 1293: 8, 1294: 8, 1326: 8, 1330: 5, 1358: 8, 1362: 8, 1390: 6, 1394: 8, 1400: 4, 1416: 8, 1422: 8, 1426: 8, 1432: 4, 1448: 7, 1454: 5, 1458: 8, 1464: 8, 1486: 3, 1490: 3, 1496: 6, 1517: 3, 1518: 4, 1528: 5, 1554: 8, 1928: 8, 1933: 8, 1938: 8, 1941: 6, 1960: 4
  },
  {
    114: 5, 168: 5, 264: 8, 269: 8, 274: 8, 277: 8, 488: 8, 513: 6, 520: 8, 552: 8, 649: 8, 743: 1, 749: 7, 757: 7, 773: 7, 781: 8, 813: 8, 840: 8, 845: 8, 909: 8, 968: 2, 973: 8, 1010: 8, 1037: 8, 1042: 8, 1069: 4, 1074: 8, 1080: 8, 1101: 8, 1106: 6, 1128: 8, 1134: 2, 1160: 8, 1166: 4, 1170: 6, 1173: 4, 1202: 8, 1230: 8, 1234: 3, 1266: 8, 1293: 8, 1294: 8, 1326: 8, 1330: 5, 1358: 8, 1362: 8, 1390: 6, 1394: 8, 1400: 4, 1416: 8, 1422: 8, 1426: 8, 1432: 4, 1448: 7, 1454: 5, 1458: 8, 1464: 8, 1486: 3, 1490: 3, 1496: 6, 1517: 3, 1518: 4, 1528: 5, 1554: 8, 1928: 8, 1933: 8, 1938: 8, 1941: 6, 1960: 4
  },
  {
    114: 5, 488: 8, 513: 6, 520: 8, 552: 8, 649: 8, 743: 1, 749: 7, 757: 7, 773: 7, 781: 8, 813: 8, 840: 8, 845: 8, 909: 8, 968: 2, 973: 8, 1010: 8, 1037: 8, 1042: 8, 1069: 4, 1074: 8, 1080: 8, 1101: 8, 1106: 6, 1128: 8, 1134: 2, 1160: 8, 1166: 4, 1170: 6, 1173: 4, 1202: 8, 1230: 8, 1234: 3, 1266: 8, 1293: 8, 1294: 8, 1326: 8, 1330: 5, 1358: 8, 1362: 8, 1390: 6, 1394: 8, 1400: 4, 1416: 8, 1422: 8, 1426: 8, 1432: 4, 1448: 7, 1454: 5, 1458: 8, 1464: 8, 1486: 3, 1490: 3, 1496: 6, 1517: 3, 1518: 4, 1528: 5, 1554: 8, 1928: 8, 1933: 8, 1938: 8, 1941: 6, 1960: 4
  },
  # Autre essai (69 ids) tel que mesure
  {
    114: 5, 168: 5, 264: 8, 269: 8, 274: 8, 277: 8, 488: 8, 513: 6, 520: 8, 552: 8, 649: 8, 743: 1, 749: 7, 757: 7, 773: 7, 781: 8, 813: 8, 840: 8, 845: 8, 909: 8, 968: 2, 973: 8, 1010: 8, 1037: 8, 1042: 8, 1069: 4, 1074: 8, 1080: 8, 1101: 8, 1106: 6, 1128: 8, 1134: 2, 1160: 8, 1166: 4, 1170: 6, 1173: 4, 1202: 8, 1230: 8, 1234: 3, 1266: 8, 1293: 8, 1294: 8, 1326: 8, 1330: 5, 1358: 8, 1362: 8, 1390: 6, 1394: 8, 1400: 4, 1416: 8, 1422: 8, 1426: 8, 1432: 4, 1448: 7, 1454: 5, 1458: 8, 1464: 8, 1486: 3, 1490: 3, 1496: 6, 1517: 3, 1518: 4, 1528: 5, 1554: 8, 1928: 8, 1933: 8, 1938: 8, 1941: 6, 1960: 4
  }],
  # Renault Clio IV
  CAR.Clio_IV_2018: [{
    144: 5, 198: 8, 302: 8, 390: 7, 394: 6, 413: 8, 416: 1, 432: 4, 502: 8, 516: 3, 529: 8, 532: 2, 535: 8, 536: 1, 578: 8, 666: 8, 668: 8, 679: 8, 681: 1, 695: 5, 700: 8, 710: 6, 771: 7, 848: 8, 850: 4, 852: 8, 855: 5, 878: 4, 914: 5, 951: 8, 1018: 2, 1050: 4, 1053: 4, 1075: 8, 1076: 2, 1116: 6, 1188: 8, 1196: 5, 1246: 3, 1272: 8, 1274: 2, 1280: 5, 1285: 4, 1297: 7, 1362: 2, 1373: 8, 1379: 2, 1380: 2, 1397: 2, 1409: 4, 1486: 3, 1495: 7, 1498: 8, 1502: 8, 1503: 3, 1513: 8, 1580: 1, 1606: 8, 1608: 8, 1619: 4, 1623: 2, 1628: 3, 1637: 8, 1638: 4, 1640: 2, 1642: 8, 1649: 2, 1675: 6, 1689: 8, 1695: 4, 1787: 8
  },
  {
    144: 5, 198: 8, 228: 5, 302: 8, 390: 7, 394: 6, 413: 8, 416: 1, 432: 4, 502: 8, 512: 6, 513: 6, 516: 3, 529: 8, 532: 2, 535: 8, 536: 1, 578: 8, 649: 8, 666: 8, 668: 8, 679: 8, 681: 1, 695: 5, 700: 8, 710: 6, 771: 7, 848: 8, 850: 4, 852: 8, 855: 5, 878: 4, 914: 5, 951: 8, 1018: 2, 1050: 4, 1053: 4, 1075: 8, 1076: 2, 1116: 6, 1188: 8, 1196: 5, 1246: 3, 1272: 8, 1274: 2, 1280: 5, 1285: 4, 1297: 7, 1362: 2, 1373: 8, 1379: 2, 1380: 2, 1397: 2, 1409: 4, 1486: 3, 1495: 7, 1498: 8, 1502: 8, 1503: 3, 1513: 8, 1580: 1, 1606: 8, 1608: 8, 1619: 4, 1623: 2, 1628: 3, 1637: 8, 1638: 4, 1640: 2, 1642: 8, 1649: 2, 1675: 6, 1689: 8, 1695: 4, 1787: 8
  },
  {
    144: 5, 198: 8, 302: 8, 390: 7, 394: 6, 413: 8, 416: 1, 432: 4, 502: 8, 513: 6, 516: 3, 535: 8, 578: 8, 649: 8, 666: 8, 668: 8, 681: 1, 695: 5, 700: 8, 710: 6, 771: 7, 848: 8, 850: 4, 852: 8, 855: 5, 914: 5, 951: 8, 1018: 2, 1050: 4, 1053: 4, 1075: 8, 1076: 2, 1116: 6, 1188: 8, 1196: 5, 1246: 3, 1272: 8, 1280: 5,  1379: 2, 1381297: 7, 1362: 2, 1373: 8, 1379: 2, 1380: 2, 1397: 2, 1486: 3, 1495: 7, 1498: 8, 1502: 8, 1503: 3, 1513: 8, 1: 2, 1628: 3,580: 1, 1606: 8, 1608: 8, 1619: 4, 1623: 2, 1628: 3, 1637: 8, 1638: 4, 1642: 8, 1675: 6, 1695: 4, 1787: 8
  },
  {
    144: 5, 198: 8, 228:5, 302: 8, 390: 7, 394: 6, 413: 8, 416: 1, 432: 4, 502: 8, 512: 6, 513: 6, 516: 3, 535: 8, 578: 8, 649: 8, 666: 8, 668: 8, 681: 1, 695: 5, 700: 8, 710: 6, 771: 7, 848: 8, 850: 4, 852: 8, 855: 5, 914: 5, 951: 8, 1018: 2, 1050: 4, 1053: 4, 1075: 8, 1076: 2, 1116: 6, 1188: 8, 1196: 5, 1246: 3, 1272: 8, 1280: 5, 1379: 2, 1381297: 7, 1362: 2, 1373: 8, 1379: 2, 1380: 2, 1397: 2, 1486: 3, 1495: 7, 1498: 8, 1502: 8, 1503: 3, 1513: 8, 1: 2, 1628: 3,580: 1, 1606: 8, 1608: 8, 1619: 4, 1623: 2, 1628: 3, 1637: 8, 1638: 4, 1642: 8, 1675: 6, 1695: 4, 1787: 8
  },
  {
    144: 5, 198: 8, 302: 8, 390: 7, 394: 6, 413: 8, 416: 1, 432: 4, 502: 8, 513: 6, 516: 3, 535: 8, 578: 8, 649: 8, 666: 8, 668: 8, 681: 1, 695: 5, 700: 8, 710: 6, 771: 7, 848: 8, 850: 4, 852: 8, 855: 5, 878: 4, 914: 4, 951: 8, 1018: 2, 1050: 4, 1053: 4, 1075: 8, 1076: 2, 1116: 6, 1188: 8, 1196: 5, 1246: 3, 1272: 8, 1280: 5, 1285: 4, 1297: 7, 1362: 2, 1373: 8, 1379: 2, 1380: 2, 1397: 2, 1409: 4, 1486: 3, 1495: 7, 1498: 8, 1502: 8, 1503: 3, 1513: 8, 1580: 1, 1606: 8, 1608: 8, 1619: 4, 1623: 2, 1628: 3, 1637: 8, 1638: 4, 1642: 8, 1675: 6, 1695: 4, 1787: 8
  }]
}

DBC = {
  CAR.ACCORD: dbc_dict('honda_accord_s2t_2018_can_generated', None),
  CAR.ACCORD_15: dbc_dict('honda_accord_lx15t_2018_can_generated', None),
  CAR.ACCORDH: dbc_dict('honda_accord_s2t_2018_can_generated', None),
  CAR.ACURA_ILX: dbc_dict('acura_ilx_2016_can_generated', 'acura_ilx_2016_nidec'),
  CAR.ACURA_RDX: dbc_dict('acura_rdx_2018_can_generated', 'acura_ilx_2016_nidec'),
  CAR.CIVIC: dbc_dict('honda_civic_touring_2016_can_generated', 'acura_ilx_2016_nidec'),
  CAR.CIVIC_BOSCH: dbc_dict('honda_civic_hatchback_ex_2017_can_generated', None),
  CAR.CRV: dbc_dict('honda_crv_touring_2016_can_generated', 'acura_ilx_2016_nidec'),
  CAR.CRV_5G: dbc_dict('honda_crv_ex_2017_can_generated', None),
  CAR.ODYSSEY: dbc_dict('honda_odyssey_exl_2018_generated', 'acura_ilx_2016_nidec'),
  CAR.PILOT: dbc_dict('honda_pilot_touring_2017_can_generated', 'acura_ilx_2016_nidec'),
  CAR.PILOT_2019: dbc_dict('honda_pilot_touring_2017_can_generated', 'acura_ilx_2016_nidec'),
  CAR.RIDGELINE: dbc_dict('honda_ridgeline_black_edition_2017_can_generated', 'acura_ilx_2016_nidec'),
  CAR.P_308_2018: dbc_dict('honda_P308_2018_can_generated', None),
  CAR.Clio_IV_2018: dbc_dict('honda_Clio_IV_2018_can_generated', None),
}

STEER_THRESHOLD = {
  CAR.ACCORD: 1200,
  CAR.ACCORD_15: 1200,
  CAR.ACCORDH: 1200,
  CAR.ACURA_ILX: 1200,
  CAR.ACURA_RDX: 400,
  CAR.CIVIC: 1200,
  CAR.CIVIC_BOSCH: 1200,
  CAR.CRV: 1200,
  CAR.CRV_5G: 1200,
  CAR.ODYSSEY: 1200,
  CAR.PILOT: 1200,
  CAR.PILOT_2019: 1200,
  CAR.RIDGELINE: 1200,
  CAR.P_308_2018: 1200,  # potentiellement a modifier pour essayer d'aller au dessus
  CAR.Clio_IV_2018: 1200,
}

SPEED_FACTOR = {
  CAR.ACCORD: 1.,
  CAR.ACCORD_15: 1.,
  CAR.ACCORDH: 1.,
  CAR.ACURA_ILX: 1.,
  CAR.ACURA_RDX: 1.,
  CAR.CIVIC: 1.,
  CAR.CIVIC_BOSCH: 1.,
  CAR.CRV: 1.025,
  CAR.CRV_5G: 1.025,
  CAR.ODYSSEY: 1.,
  CAR.PILOT: 1.,
  CAR.PILOT_2019: 1.,
  CAR.RIDGELINE: 1.,
  CAR.P_308_2018: 1.,
  CAR.Clio_IV_2018: 1.,
}

# TODO: get these from dbc file
HONDA_BOSCH = [CAR.ACCORD, CAR.ACCORD_15, CAR.ACCORDH, CAR.CIVIC_BOSCH, CAR.CRV_5G]
