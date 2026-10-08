"""Service module 22980: business logic, no crypto."""


def calculate_total_22980(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_22980():
    return 'module 22980 handles orders and invoices'
