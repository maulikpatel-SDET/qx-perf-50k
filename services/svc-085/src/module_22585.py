"""Service module 22585: business logic, no crypto."""


def calculate_total_22585(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_22585():
    return 'module 22585 handles orders and invoices'
