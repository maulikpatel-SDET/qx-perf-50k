"""Service module 5205: business logic, no crypto."""


def calculate_total_5205(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_5205():
    return 'module 5205 handles orders and invoices'
