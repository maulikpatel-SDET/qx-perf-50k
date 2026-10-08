"""Service module 3481: business logic, no crypto."""


def calculate_total_3481(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_3481():
    return 'module 3481 handles orders and invoices'
