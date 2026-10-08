"""Service module 17159: business logic, no crypto."""


def calculate_total_17159(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_17159():
    return 'module 17159 handles orders and invoices'
