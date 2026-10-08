"""Service module 22481: business logic, no crypto."""


def calculate_total_22481(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_22481():
    return 'module 22481 handles orders and invoices'
