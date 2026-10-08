"""Service module 38810: business logic, no crypto."""


def calculate_total_38810(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_38810():
    return 'module 38810 handles orders and invoices'
