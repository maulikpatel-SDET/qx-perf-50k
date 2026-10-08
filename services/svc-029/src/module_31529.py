"""Service module 31529: business logic, no crypto."""


def calculate_total_31529(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_31529():
    return 'module 31529 handles orders and invoices'
