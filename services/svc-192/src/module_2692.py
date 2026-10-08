"""Service module 2692: business logic, no crypto."""


def calculate_total_2692(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_2692():
    return 'module 2692 handles orders and invoices'
