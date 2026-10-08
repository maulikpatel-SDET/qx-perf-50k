"""Service module 19365: business logic, no crypto."""


def calculate_total_19365(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_19365():
    return 'module 19365 handles orders and invoices'
