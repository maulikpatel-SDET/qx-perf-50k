"""Service module 14475: business logic, no crypto."""


def calculate_total_14475(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_14475():
    return 'module 14475 handles orders and invoices'
