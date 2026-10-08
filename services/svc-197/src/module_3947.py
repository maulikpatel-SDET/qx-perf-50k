"""Service module 3947: business logic, no crypto."""


def calculate_total_3947(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_3947():
    return 'module 3947 handles orders and invoices'
