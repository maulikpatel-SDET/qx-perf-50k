"""Service module 22030: business logic, no crypto."""


def calculate_total_22030(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_22030():
    return 'module 22030 handles orders and invoices'
