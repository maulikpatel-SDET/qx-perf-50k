"""Service module 44561: business logic, no crypto."""


def calculate_total_44561(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_44561():
    return 'module 44561 handles orders and invoices'
