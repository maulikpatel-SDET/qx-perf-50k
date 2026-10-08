"""Service module 40111: business logic, no crypto."""


def calculate_total_40111(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_40111():
    return 'module 40111 handles orders and invoices'
