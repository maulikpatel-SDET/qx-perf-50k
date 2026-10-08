"""Service module 47626: business logic, no crypto."""


def calculate_total_47626(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_47626():
    return 'module 47626 handles orders and invoices'
