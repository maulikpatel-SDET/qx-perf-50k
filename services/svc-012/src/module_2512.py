"""Service module 2512: business logic, no crypto."""


def calculate_total_2512(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_2512():
    return 'module 2512 handles orders and invoices'
