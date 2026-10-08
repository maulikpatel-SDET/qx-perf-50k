"""Service module 25577: business logic, no crypto."""


def calculate_total_25577(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_25577():
    return 'module 25577 handles orders and invoices'
