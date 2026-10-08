"""Service module 27778: business logic, no crypto."""


def calculate_total_27778(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_27778():
    return 'module 27778 handles orders and invoices'
