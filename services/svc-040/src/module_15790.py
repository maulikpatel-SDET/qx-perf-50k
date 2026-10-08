"""Service module 15790: business logic, no crypto."""


def calculate_total_15790(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_15790():
    return 'module 15790 handles orders and invoices'
