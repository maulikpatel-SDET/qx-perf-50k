"""Service module 8320: business logic, no crypto."""


def calculate_total_8320(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_8320():
    return 'module 8320 handles orders and invoices'
