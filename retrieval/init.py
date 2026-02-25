import os

# Ensure the 'retrieval' directory exists
os.makedirs('retrieval', exist_ok=True)

# Create an empty '__init__.py' file in the 'retrieval' directory
with open('retrieval/__init__.py', 'w') as f:
	pass