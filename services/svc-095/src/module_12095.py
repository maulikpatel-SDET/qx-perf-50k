"""Service module 12095: business logic, no crypto."""


def calculate_total_12095(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12095():
    return 'module 12095 handles orders and invoices'
