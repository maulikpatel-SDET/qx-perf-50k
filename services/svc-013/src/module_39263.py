"""Service module 39263: business logic, no crypto."""


def calculate_total_39263(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39263():
    return 'module 39263 handles orders and invoices'
