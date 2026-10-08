"""Service module 24572: business logic, no crypto."""


def calculate_total_24572(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_24572():
    return 'module 24572 handles orders and invoices'
