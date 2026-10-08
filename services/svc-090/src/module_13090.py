"""Service module 13090: business logic, no crypto."""


def calculate_total_13090(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_13090():
    return 'module 13090 handles orders and invoices'
