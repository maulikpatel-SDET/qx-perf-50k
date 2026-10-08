"""Service module 42823: business logic, no crypto."""


def calculate_total_42823(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_42823():
    return 'module 42823 handles orders and invoices'
