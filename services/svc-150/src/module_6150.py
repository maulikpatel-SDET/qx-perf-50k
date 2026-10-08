"""Service module 6150: business logic, no crypto."""


def calculate_total_6150(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_6150():
    return 'module 6150 handles orders and invoices'
