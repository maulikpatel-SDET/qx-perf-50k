"""Service module 20199: business logic, no crypto."""


def calculate_total_20199(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_20199():
    return 'module 20199 handles orders and invoices'
