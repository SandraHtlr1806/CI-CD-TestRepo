Für lokale Tests:

# Circle CI
pip install -r requirements.txt
pytest
flake8 .

# Woodpecker CI
pip install -r requirements.txt
pytest

# Concourse CI
pip install -r requirements.txt
pytest