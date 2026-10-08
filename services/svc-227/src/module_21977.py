"""Service module 21977: business logic, no crypto."""


def calculate_total_21977(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_21977():
    return 'module 21977 handles orders and invoices'
