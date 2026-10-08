"""Service module 32588: business logic, no crypto."""


def calculate_total_32588(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_32588():
    return 'module 32588 handles orders and invoices'
