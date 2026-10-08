"""Service module 45751: business logic, no crypto."""


def calculate_total_45751(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_45751():
    return 'module 45751 handles orders and invoices'
