"""Service module 47716: business logic, no crypto."""


def calculate_total_47716(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_47716():
    return 'module 47716 handles orders and invoices'
