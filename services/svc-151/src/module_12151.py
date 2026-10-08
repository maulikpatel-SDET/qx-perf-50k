"""Service module 12151: business logic, no crypto."""


def calculate_total_12151(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12151():
    return 'module 12151 handles orders and invoices'
