"""Service module 38755: business logic, no crypto."""


def calculate_total_38755(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_38755():
    return 'module 38755 handles orders and invoices'
