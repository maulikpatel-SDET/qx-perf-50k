"""Service module 31572: business logic, no crypto."""


def calculate_total_31572(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_31572():
    return 'module 31572 handles orders and invoices'
