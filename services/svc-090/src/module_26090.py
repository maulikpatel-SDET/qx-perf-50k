"""Service module 26090: business logic, no crypto."""


def calculate_total_26090(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_26090():
    return 'module 26090 handles orders and invoices'
