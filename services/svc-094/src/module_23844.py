"""Service module 23844: business logic, no crypto."""


def calculate_total_23844(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_23844():
    return 'module 23844 handles orders and invoices'
