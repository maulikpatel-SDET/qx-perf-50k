"""Service module 22143: business logic, no crypto."""


def calculate_total_22143(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_22143():
    return 'module 22143 handles orders and invoices'
