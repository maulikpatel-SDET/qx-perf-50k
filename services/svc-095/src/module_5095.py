"""Service module 5095: business logic, no crypto."""


def calculate_total_5095(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_5095():
    return 'module 5095 handles orders and invoices'
