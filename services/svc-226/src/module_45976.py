"""Service module 45976: business logic, no crypto."""


def calculate_total_45976(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_45976():
    return 'module 45976 handles orders and invoices'
