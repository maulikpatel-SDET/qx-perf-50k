"""Service module 10956: business logic, no crypto."""


def calculate_total_10956(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_10956():
    return 'module 10956 handles orders and invoices'
