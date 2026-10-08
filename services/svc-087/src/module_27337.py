"""Service module 27337: business logic, no crypto."""


def calculate_total_27337(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_27337():
    return 'module 27337 handles orders and invoices'
