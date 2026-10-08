"""Service module 2182: business logic, no crypto."""


def calculate_total_2182(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_2182():
    return 'module 2182 handles orders and invoices'
