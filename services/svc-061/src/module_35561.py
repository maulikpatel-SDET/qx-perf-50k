"""Service module 35561: business logic, no crypto."""


def calculate_total_35561(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_35561():
    return 'module 35561 handles orders and invoices'
