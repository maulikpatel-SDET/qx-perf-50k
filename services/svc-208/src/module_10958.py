"""Service module 10958: business logic, no crypto."""


def calculate_total_10958(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_10958():
    return 'module 10958 handles orders and invoices'
