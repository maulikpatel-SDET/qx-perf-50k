"""Service module 47810: business logic, no crypto."""


def calculate_total_47810(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_47810():
    return 'module 47810 handles orders and invoices'
