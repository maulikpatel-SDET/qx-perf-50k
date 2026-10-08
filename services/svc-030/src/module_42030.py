"""Service module 42030: business logic, no crypto."""


def calculate_total_42030(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_42030():
    return 'module 42030 handles orders and invoices'
