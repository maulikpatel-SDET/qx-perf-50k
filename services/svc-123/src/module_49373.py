"""Service module 49373: business logic, no crypto."""


def calculate_total_49373(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_49373():
    return 'module 49373 handles orders and invoices'
