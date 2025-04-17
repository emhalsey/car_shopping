import pandas as pd
import get_data

pd.set_option('display.max_columns', None)

safety_df = get_data.find("NHTSA.csv")
fuel_df = get_data.find("fuelecon_data.csv")

if safety_df is None or fuel_df is None:
    print("Whoops! Couldn't find the files you were looking for. Please check the spelling and try again.")
    exit()

# ========================== STANDARDIZATION ==========================
# check field names to see what you can use as a key

# make a merged column to act as the key
safety_df['car_key'] = (
        safety_df['MODEL_YR'].map(str) + ' ' + safety_df['MAKE'].map(str.upper) + ' ' + safety_df['MODEL'].map(
    str.upper))
fuel_df['car_key'] = (
        fuel_df['year'].map(str) + ' ' + fuel_df['make'].map(str.upper) + ' ' + fuel_df['baseModel'].map(str.upper))

# check the field names to see if it worked (comment out after confirming)
# print(safety_df.columns)
# print(fuel_df.columns)

# merging the fields on the new key
merged_df = pd.merge(safety_df, fuel_df, on='car_key', how='outer')

# deleting duplicate and unnecessary fields
merged_df = merged_df.drop(
    columns=[
        'MAKE', 'MODEL', 'MODEL_YR','VEHICLE_CLASS',
        'PRODUCTION_RELEASE',
        'BODY_FRAME',
        'SEAT_LOC',
        'SEAT_LOC_COMMENTS',
        'MIN_GROSS_WEIGHT',
        'MAX_GROSS_WEIGHT',
        'UPPER_BELT_ANCHORAGE',
        'UPPER_BELT_ANCHORAGE_LOC',
        'SEAT_BELT_PRETENSIONER',
        'SEAT_BELT_PRETENSIONER_LOC',
        'LOAD_LIMITERS',
        'LOAD_LIMITERS_LOC',
        'FRNT_BELT_INDICATOR',
        'FRNT_BELT_LOC',
        'REAR_BELT_INDICATOR',
        'LATCH_REAR_POSITION',
        'HEAD_SAB',
        'HEAD_SAB_TYPE',
        'HEAD_SAB_LOC',
        'HEAD_SAB_MOUNT_LOC',
        'HEAD_SAB_MEET_REQUIREMENTS',
        'HEAD_SAB_DEPLOY_IN_ROLLOVER',
        'TORSO_SAB',
        'TORSO_SAB_TYPE',
        'TORSO_SAB_LOC',
        'TORSO_SAB_MOUNT_LOC',
        'KNEE_BOLSTERS',
        'KNEE_BOLSTERS_LOC',
        'ADL',
        'HEAD_RESTRAINT_IND',
        'DYNAMIC_HEAD_RESTRAINT_IND',
        'BETI',
        'BLIND_SPOT_DETECTION',
        'DAY_RUN_LIGHTS',
        'ADAPTIVE_CRUISE_CONTROL',
        'ABS',
        'ARS',
        'ARS_LOC',
        'AUTO_CRASH_NOTIFICATION',
        'CRASH_DATA_RECORDER',
        'ANTI_THEFT_DEVICE',
        'ANTI_THEFT_DEVICE_TYPE',
        'FRNT_COLLISION_WARNING',
        'NHTSA_FRNT_COLLISION_WARNING',
        'NHTSA_FCW_EVALUATION',
        'LANE_DEPARTURE_WARNING',
        'NHTSA_LANE_DEPARTURE_WARNING',
        'NHTSA_LDW_EVALUATION',
        'CRASH_IMMINENT_BRAKE',
        'NHTSA_CRASH_IMMINENT_BRAKE',
        'NHTSA_CIB_EVALUATION',
        'DYNAMIC_BRAKE_SUPPORT',
        'NHTSA_DYNAMIC_BRAKE_SUPPORT',
        'NHTSA_DBS_EVALUATION',
        'NHTSA_ESC',
        'PELVIS_SAB',
        'PELVIS_SAB_TYPE',
        'PELVIS_SAB_LOC',
        'PELVIS_SAB_MOUNT_LOC',
        'FRNT_TEST_NO',
        'FRNT_VIN',
        'FRNT_DRIV_STARS',
        'FRNT_PASS_STARS',
        'FRNT_SAFETY_CONCERN_DRIV',
        'FRNT_SAFETY_CONCERN_PASS',
        'FRNT_FOOT_NOTES',
        'FRNT_FOOT_NOTES_PASS',
        'OVERALL_FRNT_STARS',
        'CURB_WEIGHT',
        'FRNT_TESTED_WITH',
        'HIC15_DRIV',
        'CHEST_DEFL_DRIV',
        'LEFT_FEMUR_DRIV',
        'RIGHT_FEMUR_DRIV',
        'NIJ_DRIV',
        'NECK_TENS_DRIV',
        'NET_COMP_DRIV',
        'HIC15_PASS',
        'CHEST_DEFL_PASS',
        'LEFT_FEMUR_PASS',
        'RIGHT_FEMUR_PASS',
        'NIJ_PASS',
        'NECK_TENS_PASS',
        'NET_COMP_PASS',
        'SIDE_TEST_NO',
        'SIDE_VIN',
        'SIDE_DRIV_STARS',
        'SIDE_PASS_STARS',
        'SIDE_BARRIER_STAR',
        'COMB_FRNT_STAR',
        'COMB_REAR_STAR',
        'SIDE_SAFETY_CONCERN_DRIV',
        'SIDE_SAFETY_CONCERN_PASS',
        'SIDE_FOOT_NOTES',
        'SIDE_FOOT_NOTES_PASS',
        'OVERALL_SIDE_STARS',
        'SIDE_TESTED_WITH',
        'SIDE_HIC_36_DRIV',
        'RIB_DEFLECTION_DRIV',
        'ABDOMEN_FORCE_DRIV',
        'SYMPHYSIS_FORCE_DRIV',
        'SIDE_HIC_36_PASS',
        'PELVIC_FORCE_PASS',
        'POLE_TEST_NO',
        'POLE_VIN',
        'SIDE_POLE_STARS',
        'POLE_SAFETY_CONCERN',
        'POLE_FOOT_NOTES',
        'POLE_TESTED_WITH',
        'POLE_HIC_36_DRIV',
        'PELVIC_FORCE',
        'STATIC_STABI_FACTOR',
        'TIP',
        'ROLL_SAFETY_CONCERN',
        'ROLL_FOOT_NOTES',
        'NHTSA_BACKUP_CAMERA',
        'BACKUP_CAMERA',
        'barrels08',
        'barrelsA08',
        'charge120',
        'charge240',
        'city08',
        'city08U',
        'cityA08',
        'cityA08U',
        'cityCD',
        'cityE',
        'cityUF',
        'co2',
        'co2A',
        'co2TailpipeAGpm',
        'co2TailpipeGpm',
        'comb08U',
        'combA08',
        'combA08U',
        'combE',
        'combinedCD',
        'combinedUF',
        'eng_dscr',
        'feScore',
        'fuelCost08',
        'fuelCostA08',
        'fuelType1',
        'ghgScore',
        'ghgScoreA',
        'highway08',
        'highway08U',
        'highwayA08',
        'highwayA08U',
        'highwayCD',
        'highwayE',
        'highwayUF',
        'hlv',
        'hpv',
        'id',
        'lv2',
        'lv4',
        'displ',
        'drive',
        'engId',
        'mpgData',
        'phevBlended',
        'pv2',
        'pv4',
        'range',
        'rangeCity',
        'rangeCityA',
        'rangeHwy',
        'rangeHwyA',
        'UCity',
        'UCityA',
        'UHighway',
        'UHighwayA',
        'trans_dscr',
        'tCharger',
        'sCharger',
        'atvType',
        'fuelType2',
        'rangeA',
        'evMotor',
        'mfrCode',
        'c240Dscr',
        'charge240b',
        'c240bDscr',
        'createdOn',
        'modifiedOn',
        'startStop',
        'phevCity',
        'phevHwy',
        'phevComb'
    ])

# check if it worked (comment out after confirming)
# print(merged_df)

# ========================== FILTERING ==========================
merged_df = merged_df[
    (merged_df['DRIVE_TRAIN'].str.contains(r"\bAWD\b|\b4WD\b|\b4x4\b", case=False, na=False)) &
    # safety rating
    (merged_df['OVERALL_STARS'].between(4, 5)) &
    # combined mpg
    (merged_df['comb08'] > 22) &
    # includes gas & hybrid
    (merged_df['fuelType'].str.contains("Regular", case=False, na=False)) &
    (merged_df['VClass'].str.contains(r"\bSUV\b|\bSport Utility Vehicle\b", case=False, na=False)) &
    (merged_df['year'].between(2017, 2024)) &
    # gas tax by EPA
    (~merged_df['guzzler'].str.contains("G|T", case=False, na=False))
    ]

# Data integrity - check for expected columns. This line was written with the help of ChatGPT
expected_columns = ['DRIVE_TRAIN', 'OVERALL_STARS', 'comb08', 'fuelType', 'VClass', 'year', 'guzzler']
if not all(col in merged_df.columns for col in expected_columns):
    print(f"Missing columns: {set(expected_columns) - set(merged_df.columns)}")
    exit()

    # export cleaned data to output folder
filtered = get_data.export("data", "filtered_govdata.csv")
merged_df.to_csv(filtered, index=False)
