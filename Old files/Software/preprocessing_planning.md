# Planning for data pre-processing

## Details
- Target rate of trasmission (1 set of raw data) = 50Hz
- Interval = 1s / 50Hz = 20ms
- Target rate of result = Target rate of displaying result on server = 1Hz
  - Readable and responsive enough for end user
- Sets of raw data available to play with = 50Hz / 1Hz = 50 sets

## Calibration phase

- User stands still in rest position (arms at sides)
  - System verifies if values are:
    - Stable (sensors not giving fluctuating readings)
    - Within specified range (to check if correctly worn)
- System saves values as the neutral position to calibrate sensors

## Live phase

- Neutral position data will be subtracted from each reading
  - i.e. `x1.1 = x1.1 - neutralx1`, `x1.2 = x1.2 - neutralx1` 
  - Thus do not require accelerometers itself to be calibrated -> user can easily swap accelerometers without worrying about hardware calibration
- Pass in all 40 sets into Classifier => 40 sets * 12 values each = 480 values
- Classifier returns result which is saved
- Result that is repeated at least 4 times in the past 5 consecutive results is considered confident result and shown
