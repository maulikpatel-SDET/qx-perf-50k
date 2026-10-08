"""Service module 30095: business logic, no crypto."""


def calculate_total_30095(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_30095():
    return 'module 30095 handles orders and invoices'
