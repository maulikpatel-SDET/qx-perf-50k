"""Service module 4976: business logic, no crypto."""


def calculate_total_4976(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_4976():
    return 'module 4976 handles orders and invoices'
