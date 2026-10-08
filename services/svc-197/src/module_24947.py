"""Service module 24947: business logic, no crypto."""


def calculate_total_24947(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_24947():
    return 'module 24947 handles orders and invoices'
