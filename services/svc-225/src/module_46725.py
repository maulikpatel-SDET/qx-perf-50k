"""Service module 46725: business logic, no crypto."""


def calculate_total_46725(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_46725():
    return 'module 46725 handles orders and invoices'
