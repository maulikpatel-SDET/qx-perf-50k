"""Service module 21110: business logic, no crypto."""


def calculate_total_21110(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_21110():
    return 'module 21110 handles orders and invoices'
