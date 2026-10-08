"""Service module 25268: business logic, no crypto."""


def calculate_total_25268(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_25268():
    return 'module 25268 handles orders and invoices'
