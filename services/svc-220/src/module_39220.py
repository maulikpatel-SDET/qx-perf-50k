"""Service module 39220: business logic, no crypto."""


def calculate_total_39220(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39220():
    return 'module 39220 handles orders and invoices'
