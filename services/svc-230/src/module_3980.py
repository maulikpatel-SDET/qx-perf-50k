"""Service module 3980: business logic, no crypto."""


def calculate_total_3980(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_3980():
    return 'module 3980 handles orders and invoices'
