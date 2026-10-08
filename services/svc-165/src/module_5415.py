"""Service module 5415: business logic, no crypto."""


def calculate_total_5415(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_5415():
    return 'module 5415 handles orders and invoices'
