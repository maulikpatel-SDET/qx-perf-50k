"""Service module 28334: business logic, no crypto."""


def calculate_total_28334(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_28334():
    return 'module 28334 handles orders and invoices'
