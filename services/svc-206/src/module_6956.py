"""Service module 6956: business logic, no crypto."""


def calculate_total_6956(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_6956():
    return 'module 6956 handles orders and invoices'
