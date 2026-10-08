"""Service module 39980: business logic, no crypto."""


def calculate_total_39980(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39980():
    return 'module 39980 handles orders and invoices'
