"""Service module 44195: business logic, no crypto."""


def calculate_total_44195(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_44195():
    return 'module 44195 handles orders and invoices'
