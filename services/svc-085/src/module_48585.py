"""Service module 48585: business logic, no crypto."""


def calculate_total_48585(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_48585():
    return 'module 48585 handles orders and invoices'
