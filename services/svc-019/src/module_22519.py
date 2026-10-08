"""Service module 22519: business logic, no crypto."""


def calculate_total_22519(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_22519():
    return 'module 22519 handles orders and invoices'
