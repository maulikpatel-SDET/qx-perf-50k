"""Service module 26656: business logic, no crypto."""


def calculate_total_26656(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_26656():
    return 'module 26656 handles orders and invoices'
