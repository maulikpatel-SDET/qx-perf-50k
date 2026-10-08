"""Service module 11081: business logic, no crypto."""


def calculate_total_11081(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_11081():
    return 'module 11081 handles orders and invoices'
