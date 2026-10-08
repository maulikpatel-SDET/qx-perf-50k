"""Service module 39720: business logic, no crypto."""


def calculate_total_39720(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39720():
    return 'module 39720 handles orders and invoices'
