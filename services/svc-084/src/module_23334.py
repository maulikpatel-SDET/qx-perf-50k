"""Service module 23334: business logic, no crypto."""


def calculate_total_23334(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_23334():
    return 'module 23334 handles orders and invoices'
