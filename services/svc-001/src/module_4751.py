"""Service module 4751: business logic, no crypto."""


def calculate_total_4751(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_4751():
    return 'module 4751 handles orders and invoices'
