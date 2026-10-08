"""Service module 47731: business logic, no crypto."""


def calculate_total_47731(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_47731():
    return 'module 47731 handles orders and invoices'
