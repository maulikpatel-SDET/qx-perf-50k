"""Service module 14415: business logic, no crypto."""


def calculate_total_14415(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_14415():
    return 'module 14415 handles orders and invoices'
