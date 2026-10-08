"""Service module 19508: business logic, no crypto."""


def calculate_total_19508(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_19508():
    return 'module 19508 handles orders and invoices'
