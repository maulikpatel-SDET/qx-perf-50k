"""Service module 49066: business logic, no crypto."""


def calculate_total_49066(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_49066():
    return 'module 49066 handles orders and invoices'
