"""Service module 21778: business logic, no crypto."""


def calculate_total_21778(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_21778():
    return 'module 21778 handles orders and invoices'
