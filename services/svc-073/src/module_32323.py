"""Service module 32323: business logic, no crypto."""


def calculate_total_32323(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_32323():
    return 'module 32323 handles orders and invoices'
