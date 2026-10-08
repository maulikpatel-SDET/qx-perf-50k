"""Service module 30875: business logic, no crypto."""


def calculate_total_30875(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_30875():
    return 'module 30875 handles orders and invoices'
