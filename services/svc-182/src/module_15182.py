"""Service module 15182: business logic, no crypto."""


def calculate_total_15182(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_15182():
    return 'module 15182 handles orders and invoices'
