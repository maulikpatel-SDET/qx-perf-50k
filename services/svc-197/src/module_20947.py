"""Service module 20947: business logic, no crypto."""


def calculate_total_20947(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_20947():
    return 'module 20947 handles orders and invoices'
