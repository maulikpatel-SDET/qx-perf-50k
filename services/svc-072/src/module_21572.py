"""Service module 21572: business logic, no crypto."""


def calculate_total_21572(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_21572():
    return 'module 21572 handles orders and invoices'
