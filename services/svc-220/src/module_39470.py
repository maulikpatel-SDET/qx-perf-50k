"""Service module 39470: business logic, no crypto."""


def calculate_total_39470(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39470():
    return 'module 39470 handles orders and invoices'
