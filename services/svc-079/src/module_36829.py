"""Service module 36829: business logic, no crypto."""


def calculate_total_36829(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_36829():
    return 'module 36829 handles orders and invoices'
