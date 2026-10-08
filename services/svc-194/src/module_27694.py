"""Service module 27694: business logic, no crypto."""


def calculate_total_27694(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_27694():
    return 'module 27694 handles orders and invoices'
