"""Service module 36481: business logic, no crypto."""


def calculate_total_36481(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_36481():
    return 'module 36481 handles orders and invoices'
