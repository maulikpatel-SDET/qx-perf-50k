"""Service module 16572: business logic, no crypto."""


def calculate_total_16572(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_16572():
    return 'module 16572 handles orders and invoices'
