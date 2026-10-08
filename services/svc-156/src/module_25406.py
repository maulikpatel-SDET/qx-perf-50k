"""Service module 25406: business logic, no crypto."""


def calculate_total_25406(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_25406():
    return 'module 25406 handles orders and invoices'
