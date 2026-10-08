"""Service module 25263: business logic, no crypto."""


def calculate_total_25263(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_25263():
    return 'module 25263 handles orders and invoices'
