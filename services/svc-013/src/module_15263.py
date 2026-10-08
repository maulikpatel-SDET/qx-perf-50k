"""Service module 15263: business logic, no crypto."""


def calculate_total_15263(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_15263():
    return 'module 15263 handles orders and invoices'
