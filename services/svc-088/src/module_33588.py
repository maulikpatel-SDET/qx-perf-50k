"""Service module 33588: business logic, no crypto."""


def calculate_total_33588(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_33588():
    return 'module 33588 handles orders and invoices'
