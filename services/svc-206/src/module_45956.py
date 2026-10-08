"""Service module 45956: business logic, no crypto."""


def calculate_total_45956(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_45956():
    return 'module 45956 handles orders and invoices'
