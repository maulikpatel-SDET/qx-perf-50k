"""Service module 40980: business logic, no crypto."""


def calculate_total_40980(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_40980():
    return 'module 40980 handles orders and invoices'
