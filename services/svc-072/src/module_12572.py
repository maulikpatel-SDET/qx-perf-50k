"""Service module 12572: business logic, no crypto."""


def calculate_total_12572(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12572():
    return 'module 12572 handles orders and invoices'
