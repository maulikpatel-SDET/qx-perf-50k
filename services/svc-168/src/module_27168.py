"""Service module 27168: business logic, no crypto."""


def calculate_total_27168(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_27168():
    return 'module 27168 handles orders and invoices'
