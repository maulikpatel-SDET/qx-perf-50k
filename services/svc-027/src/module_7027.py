"""Service module 7027: business logic, no crypto."""


def calculate_total_7027(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_7027():
    return 'module 7027 handles orders and invoices'
