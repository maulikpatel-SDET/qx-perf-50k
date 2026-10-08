"""Service module 8182: business logic, no crypto."""


def calculate_total_8182(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_8182():
    return 'module 8182 handles orders and invoices'
