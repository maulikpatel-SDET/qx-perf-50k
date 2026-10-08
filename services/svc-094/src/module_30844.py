"""Service module 30844: business logic, no crypto."""


def calculate_total_30844(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_30844():
    return 'module 30844 handles orders and invoices'
