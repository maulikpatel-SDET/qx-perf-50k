"""Service module 40279: business logic, no crypto."""


def calculate_total_40279(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_40279():
    return 'module 40279 handles orders and invoices'
