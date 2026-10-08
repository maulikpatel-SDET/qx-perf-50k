"""Service module 38311: business logic, no crypto."""


def calculate_total_38311(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_38311():
    return 'module 38311 handles orders and invoices'
