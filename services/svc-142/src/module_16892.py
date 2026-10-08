"""Service module 16892: business logic, no crypto."""


def calculate_total_16892(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_16892():
    return 'module 16892 handles orders and invoices'
