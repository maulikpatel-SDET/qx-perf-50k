"""Service module 20751: business logic, no crypto."""


def calculate_total_20751(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_20751():
    return 'module 20751 handles orders and invoices'
