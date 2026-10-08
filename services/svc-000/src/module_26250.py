"""Service module 26250: business logic, no crypto."""


def calculate_total_26250(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_26250():
    return 'module 26250 handles orders and invoices'
