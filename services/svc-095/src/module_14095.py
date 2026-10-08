"""Service module 14095: business logic, no crypto."""


def calculate_total_14095(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_14095():
    return 'module 14095 handles orders and invoices'
