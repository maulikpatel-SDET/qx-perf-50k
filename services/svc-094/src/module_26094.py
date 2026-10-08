"""Service module 26094: business logic, no crypto."""


def calculate_total_26094(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_26094():
    return 'module 26094 handles orders and invoices'
