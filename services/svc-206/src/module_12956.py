"""Service module 12956: business logic, no crypto."""


def calculate_total_12956(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12956():
    return 'module 12956 handles orders and invoices'
