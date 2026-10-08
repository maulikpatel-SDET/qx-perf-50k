"""Service module 2034: business logic, no crypto."""


def calculate_total_2034(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_2034():
    return 'module 2034 handles orders and invoices'
