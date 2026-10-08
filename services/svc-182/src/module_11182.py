"""Service module 11182: business logic, no crypto."""


def calculate_total_11182(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_11182():
    return 'module 11182 handles orders and invoices'
