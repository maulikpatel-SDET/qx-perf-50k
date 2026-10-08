"""Service module 48182: business logic, no crypto."""


def calculate_total_48182(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_48182():
    return 'module 48182 handles orders and invoices'
