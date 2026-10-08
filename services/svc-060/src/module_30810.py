"""Service module 30810: business logic, no crypto."""


def calculate_total_30810(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_30810():
    return 'module 30810 handles orders and invoices'
