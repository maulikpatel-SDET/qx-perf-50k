"""Service module 28892: business logic, no crypto."""


def calculate_total_28892(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_28892():
    return 'module 28892 handles orders and invoices'
