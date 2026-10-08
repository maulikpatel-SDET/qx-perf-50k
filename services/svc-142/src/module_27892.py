"""Service module 27892: business logic, no crypto."""


def calculate_total_27892(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_27892():
    return 'module 27892 handles orders and invoices'
