"""Service module 4348: business logic, no crypto."""


def calculate_total_4348(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_4348():
    return 'module 4348 handles orders and invoices'
