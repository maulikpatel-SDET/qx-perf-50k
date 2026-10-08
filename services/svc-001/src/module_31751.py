"""Service module 31751: business logic, no crypto."""


def calculate_total_31751(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_31751():
    return 'module 31751 handles orders and invoices'
