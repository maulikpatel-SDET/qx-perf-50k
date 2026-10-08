"""Service module 14751: business logic, no crypto."""


def calculate_total_14751(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_14751():
    return 'module 14751 handles orders and invoices'
