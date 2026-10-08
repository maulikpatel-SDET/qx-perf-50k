"""Service module 33976: business logic, no crypto."""


def calculate_total_33976(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_33976():
    return 'module 33976 handles orders and invoices'
