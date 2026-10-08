"""Service module 23346: business logic, no crypto."""


def calculate_total_23346(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_23346():
    return 'module 23346 handles orders and invoices'
