"""Service module 12182: business logic, no crypto."""


def calculate_total_12182(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12182():
    return 'module 12182 handles orders and invoices'
