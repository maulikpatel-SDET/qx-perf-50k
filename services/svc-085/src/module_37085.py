"""Service module 37085: business logic, no crypto."""


def calculate_total_37085(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_37085():
    return 'module 37085 handles orders and invoices'
