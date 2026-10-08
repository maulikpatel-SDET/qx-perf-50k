"""Service module 17111: business logic, no crypto."""


def calculate_total_17111(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_17111():
    return 'module 17111 handles orders and invoices'
