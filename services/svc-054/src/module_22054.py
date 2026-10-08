"""Service module 22054: business logic, no crypto."""


def calculate_total_22054(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_22054():
    return 'module 22054 handles orders and invoices'
