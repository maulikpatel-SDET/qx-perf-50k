"""Service module 947: business logic, no crypto."""


def calculate_total_947(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_947():
    return 'module 947 handles orders and invoices'
