"""Service module 6508: business logic, no crypto."""


def calculate_total_6508(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_6508():
    return 'module 6508 handles orders and invoices'
