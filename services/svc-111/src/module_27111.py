"""Service module 27111: business logic, no crypto."""


def calculate_total_27111(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_27111():
    return 'module 27111 handles orders and invoices'
