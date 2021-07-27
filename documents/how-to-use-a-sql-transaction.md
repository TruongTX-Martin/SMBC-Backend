## How to use a SQL transaction


## How to use?

Call transaction context in your code
```python
from app.contexts import transaction

 with transaction():
    assessment = self.assessment_repository.create(fields)

    for item in indicators:
        # use ORM here to ensure that transaction works
        assessment_indicator = AssessmentIndicator(
            indicator_id=int(item.get('indicatorId')),
            indicator_option_id=int(item.get('indicatorOptionId')))
        assessment.assessment_indicators.append(assessment_indicator)
```

## Detail design of transaction

- [database/__init__.py](../app/database/__init__.py)
- [transaction.py](../app/contexts/transaction.py)
- [base_repostiory.py](../app/repositories/base_repository.py)
