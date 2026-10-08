"""Service module 19263: business logic, no crypto."""


def calculate_total_19263(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_19263():
    return 'module 19263 handles orders and invoices'
