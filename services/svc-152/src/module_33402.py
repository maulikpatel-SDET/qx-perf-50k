"""Service module 33402: business logic, no crypto."""


def calculate_total_33402(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_33402():
    return 'module 33402 handles orders and invoices'
