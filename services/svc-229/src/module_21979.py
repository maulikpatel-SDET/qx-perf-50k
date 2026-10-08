"""Service module 21979: business logic, no crypto."""


def calculate_total_21979(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_21979():
    return 'module 21979 handles orders and invoices'
