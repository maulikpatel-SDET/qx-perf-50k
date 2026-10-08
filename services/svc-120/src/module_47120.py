"""Service module 47120: business logic, no crypto."""


def calculate_total_47120(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_47120():
    return 'module 47120 handles orders and invoices'
