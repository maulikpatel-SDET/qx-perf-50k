"""Service module 40572: business logic, no crypto."""


def calculate_total_40572(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_40572():
    return 'module 40572 handles orders and invoices'
