"""Service module 5372: business logic, no crypto."""


def calculate_total_5372(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_5372():
    return 'module 5372 handles orders and invoices'
