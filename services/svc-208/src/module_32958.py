"""Service module 32958: business logic, no crypto."""


def calculate_total_32958(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_32958():
    return 'module 32958 handles orders and invoices'
