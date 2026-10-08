"""Service module 45947: business logic, no crypto."""


def calculate_total_45947(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_45947():
    return 'module 45947 handles orders and invoices'
