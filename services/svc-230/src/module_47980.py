"""Service module 47980: business logic, no crypto."""


def calculate_total_47980(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_47980():
    return 'module 47980 handles orders and invoices'
