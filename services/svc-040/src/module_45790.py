"""Service module 45790: business logic, no crypto."""


def calculate_total_45790(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_45790():
    return 'module 45790 handles orders and invoices'
