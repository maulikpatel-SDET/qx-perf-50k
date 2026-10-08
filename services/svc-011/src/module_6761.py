"""Service module 6761: business logic, no crypto."""


def calculate_total_6761(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_6761():
    return 'module 6761 handles orders and invoices'
