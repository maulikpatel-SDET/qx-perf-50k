"""Service module 42320: business logic, no crypto."""


def calculate_total_42320(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_42320():
    return 'module 42320 handles orders and invoices'
