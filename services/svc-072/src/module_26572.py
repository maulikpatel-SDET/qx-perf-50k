"""Service module 26572: business logic, no crypto."""


def calculate_total_26572(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_26572():
    return 'module 26572 handles orders and invoices'
