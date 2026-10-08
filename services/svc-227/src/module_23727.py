"""Service module 23727: business logic, no crypto."""


def calculate_total_23727(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_23727():
    return 'module 23727 handles orders and invoices'
