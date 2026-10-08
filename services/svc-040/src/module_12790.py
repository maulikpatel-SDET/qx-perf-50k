"""Service module 12790: business logic, no crypto."""


def calculate_total_12790(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12790():
    return 'module 12790 handles orders and invoices'
