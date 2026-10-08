"""Service module 6572: business logic, no crypto."""


def calculate_total_6572(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_6572():
    return 'module 6572 handles orders and invoices'
