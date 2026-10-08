"""Service module 17561: business logic, no crypto."""


def calculate_total_17561(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_17561():
    return 'module 17561 handles orders and invoices'
