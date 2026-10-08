"""Service module 3975: business logic, no crypto."""


def calculate_total_3975(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_3975():
    return 'module 3975 handles orders and invoices'
