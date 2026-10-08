"""Service module 40575: business logic, no crypto."""


def calculate_total_40575(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_40575():
    return 'module 40575 handles orders and invoices'
