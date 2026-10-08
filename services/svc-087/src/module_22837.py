"""Service module 22837: business logic, no crypto."""


def calculate_total_22837(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_22837():
    return 'module 22837 handles orders and invoices'
