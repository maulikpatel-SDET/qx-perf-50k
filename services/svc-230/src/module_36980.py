"""Service module 36980: business logic, no crypto."""


def calculate_total_36980(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_36980():
    return 'module 36980 handles orders and invoices'
