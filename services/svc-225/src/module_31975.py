"""Service module 31975: business logic, no crypto."""


def calculate_total_31975(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_31975():
    return 'module 31975 handles orders and invoices'
