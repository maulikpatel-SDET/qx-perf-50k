"""Service module 10095: business logic, no crypto."""


def calculate_total_10095(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_10095():
    return 'module 10095 handles orders and invoices'
