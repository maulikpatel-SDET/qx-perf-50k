"""Service module 38790: business logic, no crypto."""


def calculate_total_38790(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_38790():
    return 'module 38790 handles orders and invoices'
