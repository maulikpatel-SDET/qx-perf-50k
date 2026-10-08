"""Service module 15090: business logic, no crypto."""


def calculate_total_15090(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_15090():
    return 'module 15090 handles orders and invoices'
