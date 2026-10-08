"""Service module 5023: business logic, no crypto."""


def calculate_total_5023(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_5023():
    return 'module 5023 handles orders and invoices'
