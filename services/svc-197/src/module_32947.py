"""Service module 32947: business logic, no crypto."""


def calculate_total_32947(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_32947():
    return 'module 32947 handles orders and invoices'
