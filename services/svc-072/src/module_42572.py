"""Service module 42572: business logic, no crypto."""


def calculate_total_42572(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_42572():
    return 'module 42572 handles orders and invoices'
