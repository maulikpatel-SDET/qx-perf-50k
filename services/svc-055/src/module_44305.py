"""Service module 44305: business logic, no crypto."""


def calculate_total_44305(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_44305():
    return 'module 44305 handles orders and invoices'
