"""Service module 23975: business logic, no crypto."""


def calculate_total_23975(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_23975():
    return 'module 23975 handles orders and invoices'
