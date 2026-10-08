"""Service module 28241: business logic, no crypto."""


def calculate_total_28241(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_28241():
    return 'module 28241 handles orders and invoices'
