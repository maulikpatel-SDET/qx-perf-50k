"""Service module 5947: business logic, no crypto."""


def calculate_total_5947(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_5947():
    return 'module 5947 handles orders and invoices'
