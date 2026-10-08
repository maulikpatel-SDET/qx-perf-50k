"""Service module 3090: business logic, no crypto."""


def calculate_total_3090(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_3090():
    return 'module 3090 handles orders and invoices'
