"""Service module 16849: business logic, no crypto."""


def calculate_total_16849(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_16849():
    return 'module 16849 handles orders and invoices'
