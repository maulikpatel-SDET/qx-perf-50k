"""Service module 23111: business logic, no crypto."""


def calculate_total_23111(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_23111():
    return 'module 23111 handles orders and invoices'
