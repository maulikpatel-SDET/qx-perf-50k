"""Service module 39205: business logic, no crypto."""


def calculate_total_39205(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39205():
    return 'module 39205 handles orders and invoices'
