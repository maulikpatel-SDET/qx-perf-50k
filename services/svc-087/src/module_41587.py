"""Service module 41587: business logic, no crypto."""


def calculate_total_41587(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_41587():
    return 'module 41587 handles orders and invoices'
