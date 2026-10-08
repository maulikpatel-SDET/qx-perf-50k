"""Service module 10947: business logic, no crypto."""


def calculate_total_10947(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_10947():
    return 'module 10947 handles orders and invoices'
