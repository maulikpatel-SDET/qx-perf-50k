"""Service module 18369: business logic, no crypto."""


def calculate_total_18369(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_18369():
    return 'module 18369 handles orders and invoices'
