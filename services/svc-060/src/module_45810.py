"""Service module 45810: business logic, no crypto."""


def calculate_total_45810(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_45810():
    return 'module 45810 handles orders and invoices'
