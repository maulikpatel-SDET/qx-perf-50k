"""Service module 31656: business logic, no crypto."""


def calculate_total_31656(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_31656():
    return 'module 31656 handles orders and invoices'
