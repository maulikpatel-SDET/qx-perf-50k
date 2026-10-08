"""Service module 44810: business logic, no crypto."""


def calculate_total_44810(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_44810():
    return 'module 44810 handles orders and invoices'
