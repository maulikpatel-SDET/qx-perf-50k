"""Service module 34757: business logic, no crypto."""


def calculate_total_34757(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_34757():
    return 'module 34757 handles orders and invoices'
