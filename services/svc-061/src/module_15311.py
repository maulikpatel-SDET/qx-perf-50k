"""Service module 15311: business logic, no crypto."""


def calculate_total_15311(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_15311():
    return 'module 15311 handles orders and invoices'
