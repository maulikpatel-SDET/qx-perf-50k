"""Service module 28616: business logic, no crypto."""


def calculate_total_28616(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_28616():
    return 'module 28616 handles orders and invoices'
