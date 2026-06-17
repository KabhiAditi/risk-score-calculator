# Risk Score Calculator

## AI Interview Monitoring System

### Overview

The Risk Score Calculator is a core component of the AI Interview Monitoring System. It acts as the final decision engine that aggregates suspicious activity events detected during an online interview and generates an overall risk score and risk level.

The module receives event counts from various monitoring subsystems such as phone detection, multiple-person detection, face monitoring, gaze tracking, and head pose analysis. Based on predefined severity weights, it calculates a cumulative risk score and classifies the interview session as Low, Medium, or High Risk.

---

## Features

* Event validation and preprocessing
* Weighted risk score calculation
* Risk level classification
* Event breakdown reporting
* Handling of missing monitoring logs
* Support for future integration with monitoring modules


---

## Project Structure

```text
risk-score-calculator/

│
├── main.py
├── config.py
├── requirements.txt
├── README.md
│
├── calculator/
│   ├── __init__.py
│   └── risk_calculator.py
│
├── models/
│   ├── __init__.py
│   └── event_model.py
│
├── utils/
│   ├── __init__.py
│   └── validator.py
│
├── tests/
│   └── test_cases.py


```

---

## Input Format

The module accepts monitoring event counts in JSON/dictionary format.

Example:

```json
{
  "phone_events": 2,
  "multiple_person_events": 1,
  "face_missing_events": 3,
  "looking_away_events": 4,
  "head_pose_events": 2
}
```

---

## Event Weights

| Event Type                | Weight |
| ------------------------- | ------ |
| Phone Detection           | 25     |
| Multiple Person Detection | 30     |
| Face Missing              | 10     |
| Looking Away              | 5      |
| Head Pose Violation       | 8      |

Risk Score Formula:

```text
Risk Score = Σ(Event Count × Event Weight)
```

The final score is capped at 100.

---

## Risk Classification

| Score Range | Risk Level |
| ----------- | ---------- |
| 0 – 29      | LOW        |
| 30 – 69     | MEDIUM     |
| 70 – 100    | HIGH       |

---

## Running the Project

### Run Main Program

```bash
python main.py
```

or

```bash
python3 main.py
```

---

### Run Test Cases

```bash
python tests/test_cases.py
```

---

## Sample Output

```text
===== RISK REPORT =====

Risk Score : 100
Risk Level : HIGH

Event Breakdown:

phone_events -> Count=2, Weight=25, Score=50
multiple_person_events -> Count=1, Weight=30, Score=30
face_missing_events -> Count=3, Weight=10, Score=30
looking_away_events -> Count=4, Weight=5, Score=20
head_pose_events -> Count=1, Weight=8, Score=8
```

---

## Edge Case Handling

### Missing Logs

If a monitoring module does not provide a particular event, the validator automatically assigns a default value of 0.

Example:

Input:

```json
{
  "phone_events": 2
}
```

Processed As:

```json
{
  "phone_events": 2,
  "multiple_person_events": 0,
  "face_missing_events": 0,
  "looking_away_events": 0,
  "head_pose_events": 0
}
```

---

### No Violations

Input:

```json
{}
```

Output:

```json
{
  "risk_score": 0,
  "risk_level": "LOW"
}
```

---

## Future Integration

The Risk Score Calculator is designed to integrate with other modules of the AI Interview Monitoring System.

Example:

```python
events = {
    "phone_events": phone_detector.phone_count,
    "multiple_person_events": person_detector.multiple_person_count,
    "face_missing_events": face_tracker.face_missing_count,
    "looking_away_events": gaze_tracker.looking_away_count,
    "head_pose_events": head_pose_detector.head_pose_count
}

result = RiskCalculator.calculate(events)
```

---

## Technologies Used

* Python 3
* JSON Processing
* Object-Oriented Programming (OOP)
* Rule-Based Risk Assessment

---

