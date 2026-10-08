"""Service module 43720: business logic, no crypto."""


def calculate_total_43720(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_43720():
    return 'module 43720 handles orders and invoices'
