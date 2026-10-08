"""Service module 31790: business logic, no crypto."""


def calculate_total_31790(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_31790():
    return 'module 31790 handles orders and invoices'
