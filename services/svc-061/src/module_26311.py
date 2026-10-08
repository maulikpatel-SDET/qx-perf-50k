"""Service module 26311: business logic, no crypto."""


def calculate_total_26311(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_26311():
    return 'module 26311 handles orders and invoices'
