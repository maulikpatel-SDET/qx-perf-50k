"""Service module 25090: business logic, no crypto."""


def calculate_total_25090(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_25090():
    return 'module 25090 handles orders and invoices'
