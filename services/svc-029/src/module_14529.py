"""Service module 14529: business logic, no crypto."""


def calculate_total_14529(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_14529():
    return 'module 14529 handles orders and invoices'
