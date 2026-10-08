"""Service module 29892: business logic, no crypto."""


def calculate_total_29892(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_29892():
    return 'module 29892 handles orders and invoices'
