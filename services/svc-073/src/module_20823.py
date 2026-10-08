"""Service module 20823: business logic, no crypto."""


def calculate_total_20823(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_20823():
    return 'module 20823 handles orders and invoices'
