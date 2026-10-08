"""Service module 18334: business logic, no crypto."""


def calculate_total_18334(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_18334():
    return 'module 18334 handles orders and invoices'
