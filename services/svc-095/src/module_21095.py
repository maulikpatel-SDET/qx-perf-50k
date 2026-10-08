"""Service module 21095: business logic, no crypto."""


def calculate_total_21095(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_21095():
    return 'module 21095 handles orders and invoices'
