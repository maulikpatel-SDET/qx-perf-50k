"""Service module 49336: business logic, no crypto."""


def calculate_total_49336(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_49336():
    return 'module 49336 handles orders and invoices'
