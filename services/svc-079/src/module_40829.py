"""Service module 40829: business logic, no crypto."""


def calculate_total_40829(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_40829():
    return 'module 40829 handles orders and invoices'
