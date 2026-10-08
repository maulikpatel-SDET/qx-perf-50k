"""Service module 31481: business logic, no crypto."""


def calculate_total_31481(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_31481():
    return 'module 31481 handles orders and invoices'
