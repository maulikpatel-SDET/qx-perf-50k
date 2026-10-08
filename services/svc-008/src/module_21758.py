"""Service module 21758: business logic, no crypto."""


def calculate_total_21758(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_21758():
    return 'module 21758 handles orders and invoices'
