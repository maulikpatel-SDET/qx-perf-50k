"""Service module 8459: business logic, no crypto."""


def calculate_total_8459(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_8459():
    return 'module 8459 handles orders and invoices'
