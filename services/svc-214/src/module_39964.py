"""Service module 39964: business logic, no crypto."""


def calculate_total_39964(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39964():
    return 'module 39964 handles orders and invoices'
