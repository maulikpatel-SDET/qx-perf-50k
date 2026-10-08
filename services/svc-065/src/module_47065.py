"""Service module 47065: business logic, no crypto."""


def calculate_total_47065(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_47065():
    return 'module 47065 handles orders and invoices'
