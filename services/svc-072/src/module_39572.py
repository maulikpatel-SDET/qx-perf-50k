"""Service module 39572: business logic, no crypto."""


def calculate_total_39572(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39572():
    return 'module 39572 handles orders and invoices'
