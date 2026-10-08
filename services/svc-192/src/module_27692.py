"""Service module 27692: business logic, no crypto."""


def calculate_total_27692(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_27692():
    return 'module 27692 handles orders and invoices'
