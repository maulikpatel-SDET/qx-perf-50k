"""Service module 7790: business logic, no crypto."""


def calculate_total_7790(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_7790():
    return 'module 7790 handles orders and invoices'
