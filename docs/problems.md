## Problem Brief

Sensor data should be monitored. To do this, it implemented a monitoring system with IoT-type devices.

The system is made up of a set of devices whose ID, description, display zone (an alphanumeric value) and location are known, formed by latitude and longitude coordinates. Each coordinate will be a real number.

Each device has a set of associated sensors type. Currently, the devices support a maximum of 256 sensors. Devices can have more than one sensor of the same type working.

Each sensor has an ID, a sensor type, a unit of measure, as well as the maximum and minimum ranges of the values of each sensor.

Initially the available sensors will be 6, whose technical characteristics are detailed below. More sensors may be incorporated in the future.

![img.png](img.png)

## Problems

Imagine that you are writing a device admin tool. Please complete the following tasks. Use the database schema and API documentation as a reference.

The config file from device is en `conf/conf.csv`. The data sensor from device is in `conf/sensors.csv` 

1. Create a script that will consume data from the HTTP API endpoints described below and output sensor data to **stdout** in [JSON Lines format](https://jsonlines.org/). NOTE: You are **not** expected to create your own server backend. Although the data is mocked, use the provided endpoints as though they serve real data.

      Each line should contain:
    - The device data from config file.
    - An additional value, `date_time`, which contain the current date time in ISO 8601 UTC **date time** (i.e. "2021-09-06 17:01:07)
    - An additional value, `sensor_data`, which contain all data load from de sensors:
      Each `sensor_data` line should contain:
      - id sensor value as key.  
      - Sensor type, sensor value and sensor unit and sensor status.
        The sensor value can be a real number between sensor range.
        The sensor status will be: `OK` if data is between the sensor ranges, `NA` if sensor can't be read, `SE` if there are a sensor error or `OoR` if sensor data is out of range. 
2. Add a new field named `dew_point`. This is a calculated valued. See formula bellow. You can find the ids of sensor to combinate to make these calculations in `conf/sensor_to_calculate.csv` 
      Each line should contain:
    - The device data from config file.

Note: all real number output must be a JSON Number.

## Simple HTTP API Service

This section details the kind of data objects and HTTP Service endpoints that provide access to them. Access each service endpoint using an **HTTP GET request**.

The call must be using the base http address plus the number of sensor that you're looking for. Sensor number is from sensors.csv file.

#### HTTP Base URL: https://my-json-server.typicode.com/VulturARG/test_exercice_01

##### Example sensor id: 0: https://my-json-server.typicode.com/VulturARG/test_exercice_01/0

### Sensors
* type (string)
* first (0 to 255 integer)
* second (0 to 255 integer)

```json
{
  "type": "DBT",
  "first": 4,
  "second": 26
}
```

- If `first` or `second`value have a value greater than `255` a `SE` error must be displayed.
- If `first` and `second`value are `255` a `SE` error must be displayed.

Calculate real sensor data:
`sensor_data = first * 256 + second`

- Temperature is in decimal celsius degree (ºC * 10). Valid range for positive temperature from 0 to 700. Negative temperature valid range from 1001 to 1400.
- Humidity is in decimal percent (% * 10). Valid range is 0 to 1000. Equivalent to 0% to 100%.
- Pressure is in decimal hPa (pressure * 10). Valid range is from 3000 to 11000. Equivalent to 300 hPa to 1100 hPa.
- Wind velocity is in centesimal part of kmh. (kmh * 100). Valid range is from 0 to 25000. Equivalent to 0 to 250 kmh.
- Wind direction is en degrees.

Example 1. Temp = 26ºC:
* `first = 1`
* `second = 4`
* `sensor_data = 1 * 256 + 4`
* `sensor_data = 260 = 26ºC`

Example 2. Temp = -5ºC:
* `first = 4`
* `second = 26`
* `sensor_data = 4 * 256 + 26`
* `sensor_data = 1050 = -5ºC`

Example 3. Humidity = 84%:
* `first = 3`
* `second = 72`
* `sensor_data = 3 * 256 + 72`
* `sensor_data = 840 = 84%`

Example 4. Pressure = 970.7 hPa:
* `first = 37`
* `second = 235`
* `sensor_data = 37 * 256 + 235`
* `sensor_data = 9707 = 970.7 hPa`

Example 5. Wind speed = 170.73 kmh:
* `first = 66`
* `second = 177`
* `sensor_data = 66 * 256 + 177`
* `sensor_data = 17073 = 170.73 kmh`

Example 6. Wing direction = 357º:
* `first = 1`
* `second = 101`
* `sensor_data = 1 * 256 + 101`
* `sensor_data = 357 = 357º`

### Dew point calculation

Dew point (Pr) simplificate method is: 
![img_1.png](img_1.png)

Where:
* H is humidity in %.
* T is temperature in celsius degree.
