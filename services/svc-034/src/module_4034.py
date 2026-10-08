"""Service module 4034: business logic, no crypto."""


def calculate_total_4034(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_4034():
    return 'module 4034 handles orders and invoices'
