"""Service module 26692: business logic, no crypto."""


def calculate_total_26692(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_26692():
    return 'module 26692 handles orders and invoices'
