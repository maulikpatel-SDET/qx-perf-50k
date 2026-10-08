"""Service module 16205: business logic, no crypto."""


def calculate_total_16205(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_16205():
    return 'module 16205 handles orders and invoices'
