"""Service module 18790: business logic, no crypto."""


def calculate_total_18790(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_18790():
    return 'module 18790 handles orders and invoices'
