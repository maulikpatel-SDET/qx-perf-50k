"""Service module 49090: business logic, no crypto."""


def calculate_total_49090(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_49090():
    return 'module 49090 handles orders and invoices'
