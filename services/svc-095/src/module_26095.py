"""Service module 26095: business logic, no crypto."""


def calculate_total_26095(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_26095():
    return 'module 26095 handles orders and invoices'
