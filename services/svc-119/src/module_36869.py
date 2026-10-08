"""Service module 36869: business logic, no crypto."""


def calculate_total_36869(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_36869():
    return 'module 36869 handles orders and invoices'
