All the fields are TAB delimited

Filed# Filed Name                     Data Type/Size                 Comments
----------------------------------------------------------------------------------------------------------------------------
1      MAKE                           CHAR(25)                       Vehicle Make
2      MODEL                          CHAR(50)                       Vehicle Model
3      MODEL_YR                       NUMBER                         Vehicle Model Year
4      BODY_STYLE                     CHAR(30)                       Vehicle Body Style
5      VEHICLE_TYPE                   CHAR(30)                       Vehicle Type
6      DRIVE_TRAIN                    CHAR(10)                       Vehicle Drive Train
7      PRODUCTION_RELEASE             NUMBER                         Vehicle Release 1=Early Release, 2=Later Release, 3=Latest Release.
8      VEHICLE_CLASS                  CHAR(15)                       Vehicle Class
9      BODY_FRAME                     CHAR(14)                       Vehicle Uni-body or body on frame
10     NUM_OF_SEATING                 CHAR(30)                       Number of Seating
11     SEAT_LOC                       CHAR(120)                      Seat Locations
12     SEAT_LOC_COMMENTS              CHAR(120)                      Seating Locations Comments
13     MIN_GROSS_WEIGHT               NUMBER                         Vehicle Minimum Gross Weight (lbs)
14     MAX_GROSS_WEIGHT               NUMBER                         Vehicle Maximum Gross Weight (lbs)
15     UPPER_BELT_ANCHORAGE           CHAR(10)                       Adjustable Upper Shoulder Belt Anchorages
16     UPPER_BELT_ANCHORAGE_LOC       CHAR(70)                       Adjustable Upper Shoulder Belt Anchorages Locations
17     SEAT_BELT_PRETENSIONER         CHAR(10)                       Seat Belt Pretensioners
18     SEAT_BELT_PRETENSIONER_LOC     CHAR(50)                       Seat Belt Pretensioners Locations
19     LOAD_LIMITERS                  CHAR(10)                       Seat Belt Load Limiters
20     LOAD_LIMITERS_LOC              CHAR(16)                       Seat Belt Load Limiters Locations
21     FRNT_BELT_INDICATOR            CHAR(10)                       Front Seat Belt Indicators
22     FRNT_BELT_LOC                  CHAR(40)                       Front Seat Belt Indicators Locations
23     REAR_BELT_INDICATOR            CHAR(15)                       Rear Seat Belt Indicators
24     LATCH_REAR_POSITION            CHAR(60)                       LATCH Rear Seating Position
25     HEAD_SAB                       CHAR(100)                      Head Side Air Bag
26     HEAD_SAB_TYPE                  CHAR(20)                       Head Side Air Bag Type
27     HEAD_SAB_LOC                   CHAR(50)                       Head Side Air Bag Locations
28     HEAD_SAB_MOUNT_LOC             CHAR(10)                       Head Side Air Bag Mount Location
29     HEAD_SAB_MEET_REQUIREMENTS     CHAR(60)                       Head Side Airbags Meet TWG OOP
30     HEAD_SAB_DEPLOY_IN_ROLLOVER    CHAR(5)                        Head Side Air Bag deployable in a rollover
31     TORSO_SAB                      CHAR(30)                       Torso Side Air Bag
32     TORSO_SAB_TYPE                 CHAR(25)                       Torso Side Air Bag Type
33     TORSO_SAB_LOC                  CHAR(30)                       Torso Side Air Bag Locations
34     TORSO_SAB_MOUNT_LOC            CHAR(20)                       Torso Side Air Bag Mount Location
35     KNEE_BOLSTERS                  CHAR(10)                       Knee Bolsters
36     KNEE_BOLSTERS_LOC              CHAR(10)                       Knee Bolsters Locations
37     ADL                            CHAR(30)                       Automatic Door Locking System
38     HEAD_RESTRAINT_IND             CHAR(100)                      Head Restraints Indicate Locations
39     DYNAMIC_HEAD_RESTRAINT_IND     CHAR(50)                       Dynamic Head Restraints, Indicate Location
40     BETI                           CHAR(10)                       BETI
41     BLIND_SPOT_DETECTION           CHAR(50)                       Blind Spot Detection System
42     DAY_RUN_LIGHTS                 CHAR(70)                       Daytime Running Headlights
43     ADAPTIVE_CRUISE_CONTROL        CHAR(60)                       Adaptive Cruise Control
44     ABS                            CHAR(30)                       Antilock Braking System
45     ARS                            CHAR(50)                       Window Auto-Reverse System
46     ARS_LOC                        CHAR(50)                       Window Auto-Reverse System Locations
47     AUTO_CRASH_NOTIFICATION        CHAR(10)                       Automatic Crash Notification
48     CRASH_DATA_RECORDER            CHAR(10)                       Crash Data Recorder
49     ANTI_THEFT_DEVICE              CHAR(30)                       Anti-theft Device
50     ANTI_THEFT_DEVICE_TYPE         CHAR(100)                      Anti-theft Device Type
51     FRNT_COLLISION_WARNING         CHAR(15)                       Indicates if a vehicle is equipped with FCW
52     NHTSA_FRNT_COLLISION_WARNING   CHAR(20)                       MY2022 and prior: Indicates if a vehicle is equipped with FCW AND meets NHTSA's FCW performance criteria.MY2023 and beyond: Indicates if a vehicle is equipped with FCW (same as FRNT_COLLISION_WARNING)
53     NHTSA_FCW_EVALUATION           CHAR(50)                       MY2023 and beyond: Indicates if a vehicle meets NHTSA's FCW performance criteria
54     LANE_DEPARTURE_WARNING         CHAR(15)                       Indicates if a vehicle is equipped with LDW
55     NHTSA_LANE_DEPARTURE_WARNING   CHAR(20)                       MY2022 and prior: Indicates if a vehicle is equipped with LDW AND meets NHTSA's LDW performance criteria. MY2023 and beyond: Indicates if a vehicle is equipped with LDW (same as LANE_DEPARTURE_WARNING)
56     NHTSA_LDW_EVALUATION           CHAR(50)                       MY2023 and beyond: Indicates if a vehicle meets NHTSA's LDW performance criteria
57     CRASH_IMMINENT_BRAKE           CHAR(15)                       Indicates if a vehicle is equipped with CIB
58     NHTSA_CRASH_IMMINENT_BRAKE     CHAR(20)                       MY2022 and prior: Indicates if a vehicle is equipped with CIB AND meets NHTSA's CIB performance criteria. MY2023 and beyond: Indicates if a vehicle is equipped with CIB (same as CRASH_IMMINENT_BRAKE)
59     NHTSA_CIB_EVALUATION           CHAR(50)                       MY2023 and beyond: Indicates if a vehicle meets NHTSA's CIB performance criteria
60     DYNAMIC_BRAKE_SUPPORT          CHAR(15)                       Indicates if a vehicle is equipped with DBS
61     NHTSA_DYNAMIC_BRAKE_SUPPORT    CHAR(20)                       MY2022 and prior: Indicates if a vehicle is equipped with DBS AND meets NHTSA's DBS performance criteria.MY2023 and beyond: Indicates if a vehicle is equipped with DBS (same as DYNAMIC_BRAKE_SUPPORT)
62     NHTSA_DBS_EVALUATION           CHAR(50)                       MY2023 and beyond: Indicates if a vehicle meets NHTSA's DBS performance criteria
63     NHTSA_ESC                      CHAR(8)                        Meets NHTSA Electronic Stability Control Criteria
64     PELVIS_SAB                     CHAR(30)                       Pelvis Side Air Bag
65     PELVIS_SAB_TYPE                CHAR(25)                       Pelvis Side Air Bag Type
66     PELVIS_SAB_LOC                 CHAR(30)                       Pelvis Side Air Bag Locations
67     PELVIS_SAB_MOUNT_LOC           CHAR(20)                       Pelvis Side Air Bag Mount Location
68     OVERALL_STARS                  CHAR(40)                       Overall Stars Rating
69     FRNT_TEST_NO                   NUMBER                         Frontal Impact Test Number
70     FRNT_VIN                       CHAR(17)                       Frontal Impact Vehicle VIN Number
71     FRNT_DRIV_STARS                CHAR(40)                       Frontal Impact Driver Stars Rating
72     FRNT_PASS_STARS                CHAR(40)                       Frontal Impact Passenger Stars Rating
73     FRNT_SAFETY_CONCERN_DRIV       CHAR(500)                      Frontal Impact Driver Safety Concern
74     FRNT_SAFETY_CONCERN_PASS       CHAR(500)                      Frontal Impact Passenger Safety Concern
75     FRNT_FOOT_NOTES                CHAR(1000)                     Frontal Impact Driver Foot Notes
76     FRNT_FOOT_NOTES_PASS           CHAR(1000)                     Frontal Impact Passenger Foot Notes
77     OVERALL_FRNT_STARS             CHAR(40)                       Frontal Impact Overall Stars Rating
78     CURB_WEIGHT                    CHAR(40)                       Tested Vehicle Curb Weight (lbs)
79     FRNT_TESTED_WITH               CHAR(155)                      Frontal Impact Airbags
80     HIC15_DRIV                     NUMBER (10,5)                  Frontal Impact Driver HIC15
81     CHEST_DEFL_DRIV                NUMBER (10,5)                  Frontal Impact Driver Chest Deceleration
82     LEFT_FEMUR_DRIV                NUMBER (10,5)                  Frontal Impact Driver Left Femur Load
83     RIGHT_FEMUR_DRIV               NUMBER (10,5)                  Frontal Impact Driver Right Femur Load
84     NIJ_DRIV                       NUMBER (10,5)                  Frontal Impact Driver NIJ
85     NECK_TENS_DRIV                 NUMBER (10,5)                  Frontal Impact Driver Neck Tension
86     NET_COMP_DRIV                  NUMBER (10,5)                  Frontal Impact Driver Neck Compression
87     HIC15_PASS                     NUMBER (10,5)                  Frontal Impact Passenger HIC15
88     CHEST_DEFL_PASS                NUMBER (10,5)                  Frontal Impact Passenger Chest Deceleration
89     LEFT_FEMUR_PASS                NUMBER (10,5)                  Frontal Impact Passenger Left Femur Load
90     RIGHT_FEMUR_PASS               NUMBER (10,5)                  Frontal Impact Passenger Right Femur Load
91     NIJ_PASS                       NUMBER (10,5)                  Frontal Impact Passenger NIJ
92     NECK_TENS_PASS                 NUMBER (10,5)                  Frontal Impact Passenger Neck Tension
93     NET_COMP_PASS                  NUMBER (10,5)                  Frontal Impact Passenger Neck Compression
94     SIDE_TEST_NO                   NUMBER                         Side Impact Test Number
95     SIDE_VIN                       CHAR(17)                       Side Impact Vehicle VIN Number
96     SIDE_DRIV_STARS                CHAR(40)                       Side Impact Driver Stars Rating
97     SIDE_PASS_STARS                CHAR(40)                       Side Impact Passenger Stars Rating
98     SIDE_BARRIER_STAR              CHAR(40)                       Side Impact Barrier Stars Rating
99     COMB_FRNT_STAR                 CHAR(40)                       Side Impact Combined Front Stars Rating
100    COMB_REAR_STAR                 CHAR(40)                       Side Impact Combined Rear Stars Rating
101    SIDE_SAFETY_CONCERN_DRIV       CHAR(500)                      Side Impact Driver Safety Concern
102    SIDE_SAFETY_CONCERN_PASS       CHAR(500)                      Side Impact Passenger Safety Concern
103    SIDE_FOOT_NOTES                CHAR(1000)                     Side Impact Driver Foot Notes
104    SIDE_FOOT_NOTES_PASS           CHAR(1000)                     Side Impact Passenger Foot Notes
105    OVERALL_SIDE_STARS             CHAR(40)                       Side Impact Overall Stars Rating
106    SIDE_TESTED_WITH               CHAR(155)                      Side Impact Airbags
107    SIDE_HIC_36_DRIV               NUMBER (10,5)                  Side Impact Driver HIC36
108    RIB_DEFLECTION_DRIV            NUMBER (10,5)                  Side Impact Driver Max Thorax Rib Deflection
109    ABDOMEN_FORCE_DRIV             NUMBER (10,5)                  Side Impact Driver Total Abdomen Force
110    SYMPHYSIS_FORCE_DRIV           NUMBER (10,5)                  Side Impact Driver Public Symphysis Force
111    SIDE_HIC_36_PASS               NUMBER (10,5)                  Side Impact Passenger HIC36
112    PELVIC_FORCE_PASS              NUMBER (10,5)                  Side Impact Passenger Total Pelvic Force
113    POLE_TEST_NO                   NUMBER                         Pole Impact Test Number
114    POLE_VIN                       CHAR(17)                       Pole Impact Vehicle VIN Number
115    SIDE_POLE_STARS                CHAR(40)                       Side Pole Impact Driver Star Rating
116    POLE_SAFETY_CONCERN            CHAR(500)                      Side Pole Impact Driver Safety Concern
117    POLE_FOOT_NOTES                CHAR(600)                      Side Pole Impact Driver Foot Notes
118    POLE_TESTED_WITH               CHAR(155)                      Pole Impact Airbags
119    POLE_HIC_36_DRIV               NUMBER (10,5)                  Pole Impact Driver HIC36
120    PELVIC_FORCE                   NUMBER (10,5)                  Pole Impact Driver Total Pelvic Force
121    ROLLOVER_POSSIBILITY           NUMBER                         Vehicle Rollover Possibility
122    STATIC_STABI_FACTOR            NUMBER                         Static Stability Factor
123    TIP                            CHAR(10)                       Dynamic Test Result
124    ROLL_SAFETY_CONCERN            CHAR(500)                      Rollover Impact Safety Concern
125    ROLL_FOOT_NOTES                CHAR(500)                      Rollover Impact Foot Notes
126    ROLLOVER_STARS                 CHAR(40)                       Rollover Impact Star Rating
127    NHTSA_BACKUP_CAMERA            CHAR(8)                        Meets NHTSA Approved Rearview Video systems
128    BACKUP_CAMERA                  CHAR(8)                        Available Rearview Video systems
