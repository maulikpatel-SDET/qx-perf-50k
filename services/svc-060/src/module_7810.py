"""Service module 7810: business logic, no crypto."""


def calculate_total_7810(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_7810():
    return 'module 7810 handles orders and invoices'
