"""Service module 37094: business logic, no crypto."""


def calculate_total_37094(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_37094():
    return 'module 37094 handles orders and invoices'
