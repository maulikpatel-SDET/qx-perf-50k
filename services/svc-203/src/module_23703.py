"""Service module 23703: business logic, no crypto."""


def calculate_total_23703(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_23703():
    return 'module 23703 handles orders and invoices'
