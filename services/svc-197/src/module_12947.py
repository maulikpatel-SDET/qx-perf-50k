"""Service module 12947: business logic, no crypto."""


def calculate_total_12947(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12947():
    return 'module 12947 handles orders and invoices'
