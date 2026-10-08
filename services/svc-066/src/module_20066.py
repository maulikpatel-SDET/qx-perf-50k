"""Service module 20066: business logic, no crypto."""


def calculate_total_20066(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_20066():
    return 'module 20066 handles orders and invoices'
