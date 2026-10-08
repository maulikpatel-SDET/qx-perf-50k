"""Service module 19304: business logic, no crypto."""


def calculate_total_19304(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_19304():
    return 'module 19304 handles orders and invoices'
