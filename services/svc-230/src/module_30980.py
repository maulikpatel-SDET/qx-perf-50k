"""Service module 30980: business logic, no crypto."""


def calculate_total_30980(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_30980():
    return 'module 30980 handles orders and invoices'
