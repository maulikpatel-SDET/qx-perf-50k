"""Service module 10158: business logic, no crypto."""


def calculate_total_10158(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_10158():
    return 'module 10158 handles orders and invoices'
