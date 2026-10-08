"""Service module 24588: business logic, no crypto."""


def calculate_total_24588(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_24588():
    return 'module 24588 handles orders and invoices'
