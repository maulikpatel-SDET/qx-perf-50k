"""Service module 32976: business logic, no crypto."""


def calculate_total_32976(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_32976():
    return 'module 32976 handles orders and invoices'
