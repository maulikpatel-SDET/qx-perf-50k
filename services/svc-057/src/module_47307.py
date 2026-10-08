"""Service module 47307: business logic, no crypto."""


def calculate_total_47307(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_47307():
    return 'module 47307 handles orders and invoices'
