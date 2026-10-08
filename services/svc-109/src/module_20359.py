"""Service module 20359: business logic, no crypto."""


def calculate_total_20359(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_20359():
    return 'module 20359 handles orders and invoices'
