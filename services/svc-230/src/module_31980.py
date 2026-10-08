"""Service module 31980: business logic, no crypto."""


def calculate_total_31980(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_31980():
    return 'module 31980 handles orders and invoices'
