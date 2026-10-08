"""Service module 47748: business logic, no crypto."""


def calculate_total_47748(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_47748():
    return 'module 47748 handles orders and invoices'
