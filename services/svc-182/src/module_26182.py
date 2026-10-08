"""Service module 26182: business logic, no crypto."""


def calculate_total_26182(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_26182():
    return 'module 26182 handles orders and invoices'
