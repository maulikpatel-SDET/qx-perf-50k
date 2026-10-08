"""Service module 25829: business logic, no crypto."""


def calculate_total_25829(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_25829():
    return 'module 25829 handles orders and invoices'
