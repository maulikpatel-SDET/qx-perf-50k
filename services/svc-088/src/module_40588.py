"""Service module 40588: business logic, no crypto."""


def calculate_total_40588(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_40588():
    return 'module 40588 handles orders and invoices'
