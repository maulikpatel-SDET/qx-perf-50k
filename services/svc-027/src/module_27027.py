"""Service module 27027: business logic, no crypto."""


def calculate_total_27027(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_27027():
    return 'module 27027 handles orders and invoices'
