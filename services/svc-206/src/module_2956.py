"""Service module 2956: business logic, no crypto."""


def calculate_total_2956(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_2956():
    return 'module 2956 handles orders and invoices'
