"""Service module 25585: business logic, no crypto."""


def calculate_total_25585(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_25585():
    return 'module 25585 handles orders and invoices'
