from pymongo import MongoClient
cluster = MongoClient("mongodb+srv://rahime:1234@cluster0.zgvso.mongodb.net/myFirstDatabase?retryWrites=true&w=majority",connect = False)

db = cluster["vehicle"]
collection  = db["B"]

data = [
  {
    "Time": "10:50",
    "Latitude": 59.4855,
    "Longtitude": 18.286,
    "vehicleId": 3
  },
  {
    "Time": "10:54",
    "Latitude": 59.4859,
    "Longtitude": 18.2863,
    "vehicleId": 3
  },
  {
    "Time": "10:57",
    "Latitude": 59.4863,
    "Longtitude": 18.2869,
    "vehicleId": 3
  },
  {
    "Time": "11:00",
    "Latitude": 59.4865,
    "Longtitude": 18.2872,
    "vehicleId": 3
  },
  {
    "Time": "11:01",
    "Latitude": 59.4867,
    "Longtitude": 18.2875,
    "vehicleId": 3
  },
  {
    "Time": "11:04",
    "Latitude": 59.4872,
    "Longtitude": 18.2879,
    "vehicleId": 3
  },
  {
    "Time": "11:12",
    "Latitude": 59.489,
    "Longtitude": 18.2892,
    "vehicleId": 3
  },
  {
    "Time": "11:15",
    "Latitude": 59.4896,
    "Longtitude": 18.2896,
    "vehicleId": 3
  },
  {
    "Time": "11:17",
    "Latitude": 59.4901,
    "Longtitude": 18.2901,
    "vehicleId": 3
  },
  {
    "Time": "11:19",
    "Latitude": 59.4905,
    "Longtitude": 18.2905,
    "vehicleId": 3
  },
  {
    "Time": "11:20",
    "Latitude": 59.4906,
    "Longtitude": 18.2908,
    "vehicleId": 3
  },
  {
    "Time": "23:45",
    "Latitude": 59.3467,
    "Longtitude": 18.0307,
    "vehicleId": 4
  },
  {
    "Time": "23:47",
    "Latitude": 59.3472,
    "Longtitude": 18.0309,
    "vehicleId": 4
  },
  {
    "Time": "23:50",
    "Latitude": 59.3477,
    "Longtitude": 18.0315,
    "vehicleId": 4
  },
  {
    "Time": "23:53",
    "Latitude": 59.3481,
    "Longtitude": 18.0319,
    "vehicleId": 4
  },
  {
    "Time": "23:55",
    "Latitude": 59.3484,
    "Longtitude": 18.0324,
    "vehicleId": 4
  },
  {
    "Time": "23:59",
    "Latitude": 59.3492,
    "Longtitude": 18.0328,
    "vehicleId": 4
  },
  {
    "Time": "00:00",
    "Latitude": 59.3496,
    "Longtitude": 18.0333,
    "vehicleId": 4
  },
  {
    "Time": "00:06",
    "Latitude": 59.3499,
    "Longtitude": 18.0338,
    "vehicleId": 4
  },
  {
    "Time": "00:08",
    "Latitude": 59.3503,
    "Longtitude": 18.0341,
    "vehicleId": 4
  },
  {
    "Time": "00:11",
    "Latitude": 59.3507,
    "Longtitude": 18.0344,
    "vehicleId": 4
  },
  {
    "Time": "00:14",
    "Latitude": 59.3512,
    "Longtitude": 18.0349,
    "vehicleId": 4
  },
  {
    "Time": "00:15",
    "Latitude": 59.3516,
    "Longtitude": 18.0353,
    "vehicleId": 4
  }
]
r = collection.insert_many(data)
print(r)