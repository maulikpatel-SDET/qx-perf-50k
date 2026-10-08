"""Service module 31396: business logic, no crypto."""


def calculate_total_31396(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_31396():
    return 'module 31396 handles orders and invoices'
