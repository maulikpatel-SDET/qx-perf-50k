"""Service module 47111: business logic, no crypto."""


def calculate_total_47111(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_47111():
    return 'module 47111 handles orders and invoices'
