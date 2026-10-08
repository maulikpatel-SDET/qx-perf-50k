"""Service module 49475: business logic, no crypto."""


def calculate_total_49475(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_49475():
    return 'module 49475 handles orders and invoices'
