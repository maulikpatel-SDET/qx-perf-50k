"""Service module 49095: business logic, no crypto."""


def calculate_total_49095(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_49095():
    return 'module 49095 handles orders and invoices'
