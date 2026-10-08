"""Service module 44946: business logic, no crypto."""


def calculate_total_44946(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_44946():
    return 'module 44946 handles orders and invoices'
