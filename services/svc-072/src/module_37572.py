"""Service module 37572: business logic, no crypto."""


def calculate_total_37572(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_37572():
    return 'module 37572 handles orders and invoices'
