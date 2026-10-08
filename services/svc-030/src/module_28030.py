"""Service module 28030: business logic, no crypto."""


def calculate_total_28030(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_28030():
    return 'module 28030 handles orders and invoices'
