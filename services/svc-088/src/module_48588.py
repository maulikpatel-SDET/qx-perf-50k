"""Service module 48588: business logic, no crypto."""


def calculate_total_48588(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_48588():
    return 'module 48588 handles orders and invoices'
