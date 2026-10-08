"""Service module 13588: business logic, no crypto."""


def calculate_total_13588(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_13588():
    return 'module 13588 handles orders and invoices'
