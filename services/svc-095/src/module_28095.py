"""Service module 28095: business logic, no crypto."""


def calculate_total_28095(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_28095():
    return 'module 28095 handles orders and invoices'
