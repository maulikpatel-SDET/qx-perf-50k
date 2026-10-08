"""Service module 1475: business logic, no crypto."""


def calculate_total_1475(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_1475():
    return 'module 1475 handles orders and invoices'
