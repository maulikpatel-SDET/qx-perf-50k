"""Service module 47947: business logic, no crypto."""


def calculate_total_47947(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_47947():
    return 'module 47947 handles orders and invoices'
