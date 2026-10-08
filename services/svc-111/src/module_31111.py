"""Service module 31111: business logic, no crypto."""


def calculate_total_31111(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_31111():
    return 'module 31111 handles orders and invoices'
