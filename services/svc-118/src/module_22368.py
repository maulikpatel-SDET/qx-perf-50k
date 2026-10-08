"""Service module 22368: business logic, no crypto."""


def calculate_total_22368(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_22368():
    return 'module 22368 handles orders and invoices'
