"""Service module 40320: business logic, no crypto."""


def calculate_total_40320(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_40320():
    return 'module 40320 handles orders and invoices'
