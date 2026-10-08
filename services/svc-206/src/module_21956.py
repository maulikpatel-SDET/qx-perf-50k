"""Service module 21956: business logic, no crypto."""


def calculate_total_21956(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_21956():
    return 'module 21956 handles orders and invoices'
