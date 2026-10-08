"""Service module 25977: business logic, no crypto."""


def calculate_total_25977(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_25977():
    return 'module 25977 handles orders and invoices'
