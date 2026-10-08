"""Service module 16844: business logic, no crypto."""


def calculate_total_16844(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_16844():
    return 'module 16844 handles orders and invoices'
