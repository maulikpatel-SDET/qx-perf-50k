"""Service module 39973: business logic, no crypto."""


def calculate_total_39973(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39973():
    return 'module 39973 handles orders and invoices'
