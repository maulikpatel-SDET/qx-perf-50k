"""Service module 15475: business logic, no crypto."""


def calculate_total_15475(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_15475():
    return 'module 15475 handles orders and invoices'
