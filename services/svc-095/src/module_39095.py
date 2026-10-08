"""Service module 39095: business logic, no crypto."""


def calculate_total_39095(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39095():
    return 'module 39095 handles orders and invoices'
