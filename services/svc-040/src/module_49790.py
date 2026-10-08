"""Service module 49790: business logic, no crypto."""


def calculate_total_49790(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_49790():
    return 'module 49790 handles orders and invoices'
