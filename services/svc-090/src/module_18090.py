"""Service module 18090: business logic, no crypto."""


def calculate_total_18090(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_18090():
    return 'module 18090 handles orders and invoices'
