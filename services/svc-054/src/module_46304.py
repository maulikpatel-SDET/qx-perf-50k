"""Service module 46304: business logic, no crypto."""


def calculate_total_46304(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_46304():
    return 'module 46304 handles orders and invoices'
