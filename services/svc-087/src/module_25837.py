"""Service module 25837: business logic, no crypto."""


def calculate_total_25837(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_25837():
    return 'module 25837 handles orders and invoices'
