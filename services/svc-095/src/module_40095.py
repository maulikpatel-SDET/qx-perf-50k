"""Service module 40095: business logic, no crypto."""


def calculate_total_40095(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_40095():
    return 'module 40095 handles orders and invoices'
