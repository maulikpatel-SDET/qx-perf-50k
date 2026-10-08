"""Service module 19111: business logic, no crypto."""


def calculate_total_19111(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_19111():
    return 'module 19111 handles orders and invoices'
