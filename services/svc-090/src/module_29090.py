"""Service module 29090: business logic, no crypto."""


def calculate_total_29090(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_29090():
    return 'module 29090 handles orders and invoices'
