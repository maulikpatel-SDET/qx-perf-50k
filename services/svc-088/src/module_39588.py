"""Service module 39588: business logic, no crypto."""


def calculate_total_39588(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39588():
    return 'module 39588 handles orders and invoices'
