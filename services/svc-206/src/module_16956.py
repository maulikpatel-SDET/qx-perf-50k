"""Service module 16956: business logic, no crypto."""


def calculate_total_16956(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_16956():
    return 'module 16956 handles orders and invoices'
