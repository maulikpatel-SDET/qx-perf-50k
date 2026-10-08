"""Service module 1095: business logic, no crypto."""


def calculate_total_1095(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_1095():
    return 'module 1095 handles orders and invoices'
