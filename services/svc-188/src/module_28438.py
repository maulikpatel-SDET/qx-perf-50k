"""Service module 28438: business logic, no crypto."""


def calculate_total_28438(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_28438():
    return 'module 28438 handles orders and invoices'
