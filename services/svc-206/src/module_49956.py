"""Service module 49956: business logic, no crypto."""


def calculate_total_49956(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_49956():
    return 'module 49956 handles orders and invoices'
