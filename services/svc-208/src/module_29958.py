"""Service module 29958: business logic, no crypto."""


def calculate_total_29958(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_29958():
    return 'module 29958 handles orders and invoices'
