"""Service module 12475: business logic, no crypto."""


def calculate_total_12475(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12475():
    return 'module 12475 handles orders and invoices'
