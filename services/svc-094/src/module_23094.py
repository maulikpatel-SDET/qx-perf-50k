"""Service module 23094: business logic, no crypto."""


def calculate_total_23094(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_23094():
    return 'module 23094 handles orders and invoices'
