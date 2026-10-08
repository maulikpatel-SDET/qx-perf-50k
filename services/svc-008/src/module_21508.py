"""Service module 21508: business logic, no crypto."""


def calculate_total_21508(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_21508():
    return 'module 21508 handles orders and invoices'
