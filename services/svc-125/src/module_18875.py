"""Service module 18875: business logic, no crypto."""


def calculate_total_18875(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_18875():
    return 'module 18875 handles orders and invoices'
