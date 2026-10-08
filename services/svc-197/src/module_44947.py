"""Service module 44947: business logic, no crypto."""


def calculate_total_44947(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_44947():
    return 'module 44947 handles orders and invoices'
