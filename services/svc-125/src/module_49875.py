"""Service module 49875: business logic, no crypto."""


def calculate_total_49875(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_49875():
    return 'module 49875 handles orders and invoices'
