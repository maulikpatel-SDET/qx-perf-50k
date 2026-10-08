"""Service module 30263: business logic, no crypto."""


def calculate_total_30263(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_30263():
    return 'module 30263 handles orders and invoices'
