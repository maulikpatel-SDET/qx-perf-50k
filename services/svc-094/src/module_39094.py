"""Service module 39094: business logic, no crypto."""


def calculate_total_39094(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39094():
    return 'module 39094 handles orders and invoices'
