"""Service module 41090: business logic, no crypto."""


def calculate_total_41090(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_41090():
    return 'module 41090 handles orders and invoices'
