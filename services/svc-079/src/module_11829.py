"""Service module 11829: business logic, no crypto."""


def calculate_total_11829(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_11829():
    return 'module 11829 handles orders and invoices'
