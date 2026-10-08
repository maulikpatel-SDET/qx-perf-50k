"""Service module 13508: business logic, no crypto."""


def calculate_total_13508(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_13508():
    return 'module 13508 handles orders and invoices'
