"""Service module 22588: business logic, no crypto."""


def calculate_total_22588(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_22588():
    return 'module 22588 handles orders and invoices'
