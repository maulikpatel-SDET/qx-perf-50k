"""Service module 28976: business logic, no crypto."""


def calculate_total_28976(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_28976():
    return 'module 28976 handles orders and invoices'
