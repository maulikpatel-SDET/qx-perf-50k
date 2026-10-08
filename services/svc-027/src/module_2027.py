"""Service module 2027: business logic, no crypto."""


def calculate_total_2027(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_2027():
    return 'module 2027 handles orders and invoices'
