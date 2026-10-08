"""Service module 3572: business logic, no crypto."""


def calculate_total_3572(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_3572():
    return 'module 3572 handles orders and invoices'
