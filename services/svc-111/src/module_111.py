"""Service module 111: business logic, no crypto."""


def calculate_total_111(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_111():
    return 'module 111 handles orders and invoices'
