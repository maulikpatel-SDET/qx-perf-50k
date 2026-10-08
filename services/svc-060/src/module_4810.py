"""Service module 4810: business logic, no crypto."""


def calculate_total_4810(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_4810():
    return 'module 4810 handles orders and invoices'
