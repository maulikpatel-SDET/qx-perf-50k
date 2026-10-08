"""Service module 17790: business logic, no crypto."""


def calculate_total_17790(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_17790():
    return 'module 17790 handles orders and invoices'
