"""Service module 21616: business logic, no crypto."""


def calculate_total_21616(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_21616():
    return 'module 21616 handles orders and invoices'
