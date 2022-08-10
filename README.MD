# Project: JSON2CSV
This project is specifically for hands-on experience for involving Front-End
Development and possibly Back-End Development.
Below are the minimum requirement for the app features.
- [ ] User can paste JSON syntax into a text box
- [ ] User can click a 'Convert' button to validate the JSON text box and convert it to CSV
- [ ] User can see the converted CSV in another text box
- [ ] User can see an warning message if the JSON text box is empty or if it doesn't contain valid JSON
- [ ] User can click a 'Clear' button to clear the contents of both the JSON and CSV text boxes.
---
Project Idea comes from [here](https://github.com/florinpop17/app-ideas/blob/master/Projects/1-Beginner/JSON2CSV-App.md "Link")

---
10/8/22
* Like always, I forgot to update this README.md once I've done with updating code.
* Rework on json_2_csv.py by splitting logic into 4 functions:
  - get_json()
  - detect_csv_header()
  - convert_to_csv()
  - save_to_csv()
* Re-develop unit testing to accommodate new functions for cases with:
  - single json object with multiple keys:
  ```javascript
  {
      "Id": 1,
      "UserName": "Sam Smith",
      "email": "sam.smith@gmail.com",
      "Country": "UK",
      "Job":"Singer"
  }
  ```
  - single json list with multiple objects:
  ```javascript
  [
      {
        "Id": 1,
        "UserName": "Sam Smith"
      },
      {
        "Id": 2,
        "UserName": "Samsonite"
      },
      {
        "Id": 3,
        "UserName": "Sammy"
      }
  ]
  ```
  - same as above but with varying keys in each object elements:
  ```javascript
  [
      {
          "name": "Tom",
          "age": 10
      },
      {
          "name": "Mark",
          "age": 5,
          "height":4
      },
      {
          "name": "Pam",
          "age": 7,
          "weight":90
      }
  ]
  ```
---